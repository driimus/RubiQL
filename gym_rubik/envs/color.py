code = {
	'w' : '\33[7m',
	'r' : '\33[41m',
	'g' : "\33[42m",
	'b' : "\33[44m",
	'o' : "\33[43m",
	'y' : "\33[103m",
}
cend = '\33[0m'
def cprint(message,color,newLine = False):
	coloredMessage = code[color] + message + cend
	
	if newLine:
		print(coloredMessage)
	else:
		print(coloredMessage,end="")
	

if __name__ == "__main__":
	x = 0
	for i in range(24):
		colors = ""
		for j in range(5):
			code = str(x+j)
			colors = colors + "\33[" + code + "m\\33[" + code + "m\033[0m "
		print(colors)
		x=x+5