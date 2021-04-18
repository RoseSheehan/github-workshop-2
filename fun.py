  
# a fun little program

# prints the numbers 1 through 9
def printNums():
	for x in range(1, 10):
		print(x)

# prints myString on subsequent lines from 1 to n times
def duplicateStrings (myString, n):
	for x in range(1, n):
		print(myString * x)

printNums()
duplicateStrings("cat", 5)