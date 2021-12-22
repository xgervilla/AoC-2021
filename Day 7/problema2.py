from numpy import mean

#leemos las diferentes posiciones horizontales de los cangrejos
def readPositions(positions):
	f = open("input.txt", "r")
	for line in f:
		for num in line.split(','):
			positions.append(int(num))

#calculamos el combustible que hay que gastar
def calculateFuel(positions, posHor):
	suma = 0
	for num in positions:
		#combustible: cada nivel de diferencia aumenta en 1 (1,2,3..) --> equivalente a N * (N-1) / 2
		dif = abs(num-posHor)
		suma+= dif*(dif+1)/2
	return suma


#main de ejecucion
if __name__ == '__main__':
	positions = []
	#leemos las posiciones
	readPositions(positions)
	#cogemos el valor medio de todas las posiciones
	medNum = int(mean(positions))
	#calculamos el combustible respecto ese valor
	print(calculateFuel(positions, medNum))