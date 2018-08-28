from color import cprint as colorPrint

class Cube:
	
	colors = ('w','r','g','o','b','y',)
	
	def __init__(self,sideLength,sides = 6):
		self.sideLength = sideLength
		self.sides = sides
		self.faces = []
		self.generate()
		print("Initialised a solved %s cube." %(3*("x%s" %(sideLength)))[1:])
		self.display()
	
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
	
	def display(self):
		for face in self.faces:
			for line in face:
				print(" ",end="")
				for tile in line:
					colorPrint("  ",tile)
					print(" ",end="")
				print("\n")
			print("")
rubik = Cube(3)