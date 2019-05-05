import random

numberOfIterations = int(input("Number Of Iterations"))

def generateList():
	returnable = []

	for i in range(32):
		addToReturn = []
		for x in range(8):
			addToReturn.append(random.randint(0,1))
		returnable.append(addToReturn)
	return returnable


def fitIndividual(x):
	count = 0
	for y in x:
		if(y == 1):
			count = count+1
	if(count == 8):
		return True
	return False

def mutate(x):

	x[random.randint(0,len(x)-1)] = random.randint(0,1)
	return x


def fitAndReproduce(population):
	totalFitness = 0
	randArray = []
	index = 0
	for x in population:
		index = index+1
		for y in x:
			count = 0
			if(y == 1):
				totalFitness = totalFitness + 1
				count = count+1
			for z in range(0,count):
				randArray.append(index)


	x1 = population[random.choice(randArray)-1][:4]
	x2 = population[random.choice(randArray)-1][:4]

	child = x1+x2


	return child
	



def geneticAlgorithm(numberOfIterations, initialPopulation):
	population = initialPopulation
	while((numberOfIterations != 0) & (fitIndividual(population) == False)):
		numberOfIterations = numberOfIterations - 1
		newPop = []
		for x in range(len(population)):
			child = fitAndReproduce(population)
			if(random.randint(0,50) == 49):
				child = mutate(child)
			newPop.append(child)
		population = newPop
	return findBestCandidate(population)


def findBestCandidate(pop):
	best = []
	bestCount = 0
	for x in pop:
		count = 0
		for y in x:
			if(y == 1):
				count = count + 1
		if(count>bestCount):
			bestCount = count
			best = x

	return best

def runAll():
	population = generateList()
	printable = geneticAlgorithm(numberOfIterations,population)
	print(printable)


runAll()



	
