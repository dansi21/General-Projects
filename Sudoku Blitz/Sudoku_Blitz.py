

def readIn():

	fileIn = open("test.txt","r")

	board = []

	line = fileIn.read()
	count = 0

	boardList = []
	for i in line:
		boardList.append(int(i))
		count = count+1
		if count == 9:
			count = 0
			board.append(boardList)
			boardList = []
	return board



def forwardCheckingDegreeH(board):
	max = []
	maxNum = 0
	for i in range(9):
		for j in range(9):
			if (((9-len(getValues(board,i,j))) > maxNum) & (board[i][j] == 0)):
				maxNum = (9-len(getValues(board,i,j)))
				max.clear()
				max.append(i)
				max.append(j)
	return max


def getValues(boarded,x,y):
	listValues = []
	for i in range(9):
		listValues.append(i+1)
	for i in range(9):
		if((boarded[x][i] != 0) & (boarded[x][i] in listValues)):
			listValues.remove(boarded[x][i])
	for i in range(9):
		 if ((boarded[i][y] != 0) & (boarded[i][y] in listValues)):
		 	listValues.remove(boarded[i][y])
	for i in range(3*(x//3),(3*(x//3))+3):
		for j in range(3*(y//3),3*(y//3)+3):
			if boarded[i][j] in listValues:
				listValues.remove(boarded[i][j])
	return listValues



def checkValidity(board, x, y, value):
	for i in range(9):
		if((board[x][i] == value) or (board[i][y] == value)):
			return False
	for i in range((3 *(x//3)),(3 *(x//3))+3):
		for j in range(3*(y//3),3*(y//3)+3):
			if board[i][j] == value:
				return False
	return True

def algorithm(board):
	check = True
	for x in range(9):
		for y in range(9):
			if board[x][y] == 0:
				check = False


	if check:
		endAlgo(board)
		return True
	coordinates = forwardCheckingDegreeH(board)
	possibleValues = getValues(board, coordinates[0], coordinates[1])

	for value in possibleValues:
		board[coordinates[0]][coordinates[1]] = value
		if algorithm(board):
			return True
		board[coordinates[0]][coordinates[1]] = 0

	return False

def endAlgo(board):
	file = open("output.txt","w")
	file.write("/n")
	file.write(str(board))



def runAll():

	board = readIn()
	algorithm(board)

runAll()




