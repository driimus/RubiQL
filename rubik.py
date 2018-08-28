from color import cprint as colorPrint

class Cube:
	
	colors = ('w','r','g','o','b','y',)
	
	def __init__(self,sideLength,sides = 6):
		self.sideLength = sideLength
		self.sides = sides
		self.faces = []
		self.generate()
		print("Initialised a solved %s cube." %(3*("x%s" %(sideLength)))[1:])
		self.niceDisplay()
	
	def generate(self):
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
		
		
	def scramble(self):
		pass
	
	def solve(self):
		pass
				
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
		print("\n")
		
rubik = Cube(3)