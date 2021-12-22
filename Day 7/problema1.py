from numpy import sort, median, mean

def readPositions(positions):
	f = open("input.txt", "r")
	for line in f:
		for num in line.split(','):
			positions.append(int(num))


def calculateFuel(positions, posHor):
	suma = 0
	for num in positions:
		suma += abs(num-posHor)
	return suma


if __name__ == '__main__':
	positions = []
	readPositions(positions)
	#positions = sort(positions)
	medNum = mean(positions)
	print(medNum)

	#print(calculateFuel(positions, medNum))