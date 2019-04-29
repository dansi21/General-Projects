userGeneratedSize = int(input("Please Enter Grid Width/Length: "))
queensToAdd = int(input("Please Enter # Of Queens: "))
queenList = []


for i in range(userGeneratedSize):
	temp = []
	for j in range(userGeneratedSize):
		temp.append(0)
	queenList.append(temp)

	
def printBoard():
	for i in range(userGeneratedSize):
		print(queenList[i])

def recursiveBacktracing(QueensLeft):
	if QueensLeft == 0:
		return True
	for x in range(userGeneratedSize):
		for y in range(userGeneratedSize):
			if(queenList[x][y]!=1):
				if checkBoard(x,y):
					queenList[x][y]=1
					if recursiveBacktracing(QueensLeft-1):
						return True
					queenList[x][y] = 0			
	return False#fail

def checkBoard(x,y):
	for i in range(userGeneratedSize):
		if queenList[i][y]==1 or queenList[x][i]==1:
			return False#Board is not safe
	for i in range(userGeneratedSize):
		for g in range(userGeneratedSize):
			if ((i-g==x-y) or (x+y==g+i)):#(1,2) = 3 and (2,1) = 3. Diagonals always share the same additive value
				if queenList[i][g]==1:
					return False
	return True#Board is safe


print(recursiveBacktracing(queensToAdd))
printBoard()
