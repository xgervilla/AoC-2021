#leemos el mapa de alturas
def readDigits(heightmap):
	f = open("input.txt", "r")
	for line in f:
		line = line.rstrip('\n')
		newLine = []
		for num in list(line):
			newLine.append(int(num))
		heightmap.append(newLine)

#devuelve si es esquina, en caso positivo devuelve que tipo
def esEsquina(row, col, esquinas):
	minRow, maxRow = esquinas[0], esquinas[1]
	minCol, maxCol = esquinas[2], esquinas[3]
	#superior izquierda
	if (row == minRow and col == minCol):
		return 1
	#superior derecha
	elif (row == minRow and col == maxCol):
		return 2
	#inferior izquierda
	elif (row == maxRow and col == minCol):
		return 3
	#inferior derecha
	elif (row == maxRow and col == maxCol):
		return 4
	#no es esquina
	return -1

#devuelve si es borde, en caso positivo devuelve que tipo
def esBorde(row, col, bordes):
	up, down, left, right = bordes[0], bordes[1], bordes[2], bordes[3]
	#borde izquierdo
	if col == left:
		return 1
	#borde derecho
	elif col == right:
		return 2
	#borde superior
	elif row == up:
		return 3
	#borde inferior
	elif row == down:
		return 4
	#no es borde
	return -1

#cogemos los puntos adyacentes a [row][col]
def getAdjacents(row, col, heightmap):
	#guardamos los limites del mapa
	minRow, maxRow = 0, len(heightmap)-1
	minCol, maxCol = 0, len(heightmap[0])-1

	#si el punto es esquina -> solo tiene 2 adyacentes (depende del tipo de esquina que sea)
	typeEsq = esEsquina(row, col, [minRow, maxRow, minCol, maxCol])
	if typeEsq > 0:
		#superior izquierda
		if typeEsq == 1:
			right = heightmap[row][col+1]
			down = heightmap[row+1][col]
			return [right, down]
		#superior derecha
		elif typeEsq == 2:
			left = heightmap[row][col-1]
			down = heightmap[row+1][col]
			return [left, down]
		#inferior izquierda
		elif typeEsq == 3:
			right = heightmap[row][col+1]
			up = heightmap[row-1][col]
			return [right, up]
		#inferior derecha
		else:
			left = heightmap[row][col-1]
			up = heightmap[row-1][col]
			return [left, up]
	#si no es esquina
	else:
		#si es borde -> solo tiene 3 adyacentes (depende del tipo de borde que sea)
		typeBorde = esBorde(row, col, [minRow, maxRow, minCol, maxCol])
		if typeBorde > 0:
			#izquierda
			if typeBorde == 1:
				right = heightmap[row][col+1]
				up = heightmap[row-1][col]
				down = heightmap[row+1][col]
				return [right, up, down]
			#derecha
			elif typeBorde == 2:
				left = heightmap[row][col-1]
				up = heightmap[row-1][col]
				down = heightmap[row+1][col]
				return [left, up, down]
			#arriba
			elif typeBorde == 3:
				left = heightmap[row][col-1]
				right = heightmap[row][col+1]
				down = heightmap[row+1][col]
				return [left, right, down]
			#abajo
			else:
				left = heightmap[row][col-1]
				right = heightmap[row][col+1]
				up = heightmap[row-1][col]
				return [left, right, up]
		#si no es esquina ni borde -> punto normal, 4 adyacentes
		else:
			left = heightmap[row][col-1]
			right = heightmap[row][col+1]
			up = heightmap[row-1][col]
			down = heightmap[row+1][col]
			return [left, right, up, down]

#devuelve si un punto es minimo respecto los adyacentes:
def lowPoint(point, adjacents):
	#si el punto pertenece a los adyacentes, no puede ser el minimo
	if point in adjacents:
		return False
	else:
		#si no pertenece, devolvemos si es menor que el minimo de los adyacentes (es el menor de todos)
		minAux = min(adjacents)
		return minAux > point

#calcula los low points del mapa
def calculateLowPoints(heightmap):
	#tamaño de filas y de columnas para explorar el mapa
	rows = len(heightmap)
	cols = len(heightmap[0])

	lowpoints = 0
	#por cada punto, vemos cogemos sus adyacentes y si es un lowpoint, incrementamos el contador
	for row in range(rows):
		for col in range(cols):
			adjacents = getAdjacents(row, col, heightmap)
			if lowPoint(heightmap[row][col], adjacents):
				lowpoints += heightmap[row][col] +1
	return lowpoints

#main de ejecucion
if __name__ == '__main__':
	heightmap = []
	#leemos el mapa
	readDigits(heightmap)
	#calculamos el numero de lowpoints
	print(calculateLowPoints(heightmap))