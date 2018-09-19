import numpy
from math import *
from quat import *

import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *


axis_verts = (
    (-7.5, 0.0, 0.0),
    ( 7.5, 0.0, 0.0),
    ( 0.0,-7.5, 0.0),
    ( 0.0, 7.5, 0.0),
    ( 0.0, 0.0,-7.5),
    ( 0.0, 0.0, 7.5)
    )

axes = (
    (0,1),
    (2,3),
    (4,5)
    )

axis_colors = (
    (1.0,0.0,0.0), # Red
    (0.0,1.0,0.0), # Green
    (0.0,0.0,1.0)  # Blue
    )


'''
       5____________6
       /           /|
      /           / |
    1/__________2/  |
    |           |   |
    |           |   |
    |           |   7
    |           |  /
    |           | /
    0___________3/
'''

cube_verts = (
    (-3.0,-3.0, 3.0),
    (-3.0, 3.0, 3.0),
    ( 3.0, 3.0, 3.0),
    ( 3.0,-3.0, 3.0),
    (-3.0,-3.0,-3.0),
    (-3.0, 3.0,-3.0),
    ( 3.0, 3.0,-3.0),
    ( 3.0,-3.0,-3.0)
    )

cube_edges = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,6),
    (5,1),
    (5,4),
    (5,6),
    (7,3),
    (7,4),
    (7,6)
    )

cube_surfaces = (
    (0,1,2,3), # Front
    (3,2,6,7), # Right
    (7,6,5,4), # Left
    (4,5,1,0), # Back
    (1,5,6,2), # Top
    (4,0,3,7)  # Bottom
    )

cube_colors = (
    (0.769,0.118,0.227), # Red
    (  0.0,0.318,0.729), # Blue
    (  1.0,0.345,  0.0), # Orange
    (  0.0, 0.62,0.376), # Green
    (  1.0,  1.0,  1.0), # White
    (  1.0,0.835,  0.0)  # Yellow
    )


def Axis():
    glBegin(GL_LINES)
    for color,axis in zip(axis_colors,axes):
        glColor3fv(color)
        for point in axis:
            glVertex3fv(axis_verts[point])
    glEnd()

def Cube():
    glBegin(GL_QUADS)
    for color,surface in zip(cube_colors,cube_surfaces):
        glColor3fv(color)
        for vertex in surface:
            glVertex3fv(cube_verts[vertex])
    glEnd()

    glBegin(GL_LINES)
    glColor3fv((0.0,0.0,0.0))
    for edge in cube_edges:
        for vertex in edge:
            glVertex3fv(cube_verts[vertex])
    glEnd()

def main():
    pygame.init()
    display = (1800,1718)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    # Using depth test to make sure closer colors are shown over further ones
    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LESS)

    # Default view
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, (display[0]/display[1]), 0.5, 40)
    glTranslatef(0.0,0.0,-17.5)


    inc_x = 0
    inc_y = 0
    accum = (1,0,0,0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                #Rotating about the x axis
                if event.key == pygame.K_UP:
                    inc_x =  pi/100
                if event.key == pygame.K_DOWN:
                    inc_x = -pi/100

                # Rotating about the y axis
                if event.key == pygame.K_LEFT:
                    inc_y =  pi/100
                if event.key == pygame.K_RIGHT:
                    inc_y = -pi/100

                # Reset to default view
                if event.key == pygame.K_SPACE:
                    accum = (1,0,0,0)

            if event.type == pygame.KEYUP:
                # Stoping rotation
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    inc_x = 0.0
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    inc_y = 0.0

        rot_x = normalize(axisangle_to_q((1.0,0.0,0.0), inc_x))
        rot_y = normalize(axisangle_to_q((0.0,1.0,0.0), inc_y))
        accum = q_mult(accum,rot_x)
        accum = q_mult(accum,rot_y)

        glMatrixMode(GL_MODELVIEW)
        glLoadMatrixf(q_to_mat4(accum))

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Cube()
        Axis()
        pygame.display.flip()
        pygame.time.wait(10)

main()