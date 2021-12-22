from numpy import sort, median

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
		#combustible: valor absoulto de la diferencia entre la posicion en la que esta el cangrejo (num) y a donde tiene que ir (posHor)
		suma += abs(num-posHor)
	return suma

#main de ejecucion
if __name__ == '__main__':
	positions = []
	#leemos las posiciones
	readPositions(positions)
	#las ordenamos ascendientemente
	positions = sort(positions)
	#cogemos el valor medio 
	medNum = median(positions)
	#calculamos el combustible respecto ese valor
	print(calculateFuel(positions, medNum))
