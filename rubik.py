from color import cprint as colorPrint
import time
from random import randrange
class Cube:
	
	colors = ('w','r','g','o','b','y',)
	
	def __init__(self,sideLength,sides = 6):
		self.sideLength = sideLength
		self.sides = sides
		self.faces = []
		self.indexes = [i for i in range(sides)]
		self.evens = []
		self.odds = []
		self.moves = []
		self.__generate__()
		print("Initialised a solved %s cube." %(3*("x%s" %(sideLength)))[1:])
		self.niceDisplay()
		
	def __indexate__(self):
		for i in range(sides):
			if i==0 or i%2==1:
				odds.append(i)
			else:
				evens.append(i)
	
	def handleInput(self,msg):
		if msg=="X":
			self.rotateXaxis()
		if msg=="X'":
			self.counterRotateXaxis()
		if msg=="Y":
			self.rotateYaxis()
		if msg=="Y'":
			self.counterRotateYaxis()
		if msg=="Z":
			self.rotateZaxis()
		if msg=="Z'":
			self.counterRotateZaxis()
			
		if msg=="U":
			self.moveU()
		if msg=="U'":
			self.revU()
		if msg=="M":
			self.moveM()
		if msg=="M'":
			self.revM()
		if msg=="D":
			self.moveD()
		if msg=="D'":
			self.revD()
		if msg=="R":
			self.moveR()
		if msg=="R'":
			self.revR()
		if msg=="L":
			self.moveL()
		if msg=="L'":
			self.revL()
		if msg=="F":
			self.moveF()
		if msg=="F'":
			self.revF()
		if msg=="solve":
			self.solve()
		if msg=="scramble":
			self.scramble()

	def __generate__(self):
		self.faces.clear()
		for face in range(self.sides):
# 			color for that respective solved face
			color = Cube.colors[face]
			
			faceList = []
			for line in range(self.sideLength):
				lineList = []
				for tile in range(self.sideLength):
					lineList.append(color)
				faceList.append(lineList)
			self.faces.append(faceList)
	
	def addMove(self,move):
		move+="'"
		self.moves.append(move)


	def scramble(self,moveCount=10):
		moveset = ["R","U","L","D","F","B"]
		for count in range(moveCount):
			move = moveset[randrange(len(moveset))]
			self.addMove(move)
			self.handleInput(move)
			time.sleep(0.5)
			self.niceDisplay()
		
		print("Scrambled the cube %s times" %(moveCount))
		
	def new(self):
		self.__generate__()

	def isSolved(self):
		return all(x == self.moves[0] for x in self.moves)

	def solve(self):
		self.moves.reverse()
		for move in self.moves:
			self.handleInput(move)
			time.sleep(randrange(3))
			print("Found move %s ... " %move)
			self.niceDisplay()
		print("All the faces are now solved")
				
	def display(self,faces):
		print("")
		
		for line in range(self.sideLength):
			for face in faces: #loop all the sides
				print(" ",end="")
				for tile in face[line]:
					colorPrint("  ",tile)
					print(" ",end="")
				print("  ",end="")
			print("\n")
	
	def niceDisplay(self):		
		self.display(self.faces[0:1])
		self.display(self.faces[1:-1])
		self.display(self.faces[-1:])
		
	def __spinYline__(self,faceIndex,topIndex,line):
		start = self.faces[faceIndex][line].copy()
		self.faces[faceIndex][line] = self.faces[faceIndex+1][line]
		self.faces[faceIndex+1][line] = self.faces[faceIndex+2][line]
		self.faces[faceIndex+2][line] = self.faces[faceIndex+3][line]
		self.faces[faceIndex+3][line] = start
		
	def __reverseSpinYline__(self,faceIndex,topIndex,line):
		start = self.faces[faceIndex+3][line].copy()
		self.faces[faceIndex+3][line] = self.faces[faceIndex+2][line]
		self.faces[faceIndex+2][line] = self.faces[faceIndex+1][line]
		self.faces[faceIndex+1][line] = self.faces[faceIndex][line]
		self.faces[faceIndex][line] = start
		
# '''
# -------------------- MADE FOR ROTATING A SINGLE FACE -------------------
# '''
	
	def __rotateFace__(self,faceIndex):
		newFace = []
		for vLine in range(self.sideLength):
			newLine = []
			for line in self.faces[faceIndex][::-1]:
				newLine.append(line[vLine])
			newFace.append(newLine)
		self.faces[faceIndex] = newFace
		
	def __counterRotateFace__(self,faceIndex):
		newFace = []
		for vLine in range(self.sideLength-1,-1,-1):
			newLine = []
			for line in self.faces[faceIndex]:
				newLine.append(line[vLine])
			newFace.append(newLine)
		self.faces[faceIndex] = newFace
	
# '''
# ------------------------------------------------------------------------
# '''
# '''
# ---------------- ROTATING THE CUBE ON IT's AXIS ------------------------
# '''
# 	CLOCKWISE ROTATIONS
	def __spinEnds__(self,topIndex,bottomIndex):
		'''function takes as input indedex of the faces found at 
		the edges of an axis and spins them'''
		self.__rotateFace__(topIndex) #top spins clockwise
		self.__counterRotateFace__(bottomIndex) #bottom spins counterclockwise
	
	def faceSwap(self,iList=[],reverse=False):
		if reverse:
			iList.reverse()
		start = self.faces[iList[0]].copy()
		for index in range(len(iList)-1):
			self.faces[iList[index]] = self.faces[iList[index+1]]
		self.faces[iList[-1]] = start
		
			
	def rotateXaxis(self,topIndex=2,bottomIndex=4,back=3,r=False):
		self.__spinEnds__(topIndex,bottomIndex)
		
		f= [0,1,5,3]
		self.__rotateFace__(back)
		self.__rotateFace__(back)
		
		self.faceSwap(f,r)
		

	
	def rotateYaxis(self,topIndex=0,bottomIndex=5,lastIndex=4,firstIndex=1):
		self.__spinEnds__(topIndex,bottomIndex)
		self.faces.insert(lastIndex,self.faces.pop(firstIndex))

		
	def rotateZaxis(self,topIndex=1,bottomIndex=3,reverse=False):
		self.counterRotateYaxis()
		if not reverse:
			self.rotateXaxis()
		else:
			self.counterRotateXaxis()
		
		self.rotateYaxis()
		
	
# 	COUNTERCLOCKWISE ROTATIONS
	
	def counterRotateXaxis(self,topIndex=4,bottomIndex=2,back=5):
		self.rotateXaxis(topIndex,bottomIndex,back,True)
	
	def counterRotateYaxis(self,topIndex=4,bottomIndex=2):
		self.rotateYaxis(5,0,1,4)
		
	def counterRotateZaxis(self):
		self.rotateZaxis(3,1,True)
# '''
# ------------------------------------------------------------------------
# '''
# 	############ MOVES THAT CAN BE PERFORMED ##################
# ''' moves on the Y axis '''
	def moveU(self,faceIndex=1,topIndex=0,line=0):
		self.__spinYline__(faceIndex,topIndex,line)
		self.__rotateFace__(topIndex)
		
	def moveM(self,faceIndex=1,topIndex=0,line=1):
		self.__spinYline__(faceIndex,topIndex,line)
		
	def moveD(self,faceIndex=1,bottomIndex=5,line=2):
		self.__spinYline__(faceIndex,bottomIndex,line)
		self.__counterRotateFace__(bottomIndex)
		
	def moveR(self,reverse=False,faceIndex=1,bottomIndex=5,line=2):
		self.counterRotateZaxis()
		if reverse:
			self.revU()
		else:
			self.moveU()
		self.rotateZaxis()
		
	def moveL(self,reverse=False):
		self.rotateYaxis()
		self.rotateYaxis()
		
		if not reverse:
			self.moveR()
		else:
			self.revR()
			
		self.rotateYaxis()
		self.rotateYaxis()


	def moveF(self,reverse=False):
		self.rotateXaxis()
		if not reverse:
			self.moveU()
		else:
			self.revU()
		self.counterRotateXaxis()
	
	def revU(self,faceIndex=1,topIndex=0,line=0):
		self.__reverseSpinYline__(faceIndex,topIndex,line)
		self.__counterRotateFace__(topIndex)
		
	def revM(self,faceIndex=1,topIndex=0,line=1):
		self.__reverseSpinYline__(faceIndex,topIndex,line)

	def revD(self,faceIndex=1,bottomIndex=5,line=2):
		self.__reverseSpinYline__(faceIndex,bottomIndex,line)
		self.__rotateFace__(bottomIndex)

	def revR(self):
		self.moveR(True)
	
	def revL(self):
		self.moveL(True)
		
	def revF(self):
		self.moveF(True)


if __name__ == "__main__":
	rubik = Cube(3)

	move = input("move:")
	while move:
		rubik.handleInput(move)
		rubik.niceDisplay()
		move = input("move:")
		
		