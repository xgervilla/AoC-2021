#leemos el mapa de alturas
def readDigits(heightmap):
	f = open("input.txt", "r")
	for line in f:
		line = line.rstrip('\n')
		newLine = []
		for num in list(line):
			newLine.append(int(num))
		heightmap.append(newLine)

'''--- LowPoints ---'''
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

	lowpoints = []
	#por cada punto, vemos cogemos sus adyacentes y si es un lowpoint, lo añadimos a la lista de lowpoints
	for row in range(rows):
		for col in range(cols):
			adjacents = getAdjacents(row, col, heightmap)
			if lowPoint(heightmap[row][col], adjacents):
				lowpoints.append([row,col])
	return lowpoints

'''--- Basins ---'''
#calcula el basin de un lowpoint
def getBasinSize(row, col, heightmap):
	#marcamos la casilla actual como "explorada"
	explore = 1 if heightmap[row][col] != 9 else 0
	heightmap[row][col] = 9

	#si se puede explorar abajo, seguimos buscando
	if not (row+1 >= len(heightmap) or heightmap[row+1][col] == 9) :
		explore += getBasinSize(row+1, col, heightmap)

	#si se puede explorar arriba, seguimos buscando
	if not (row-1 < 0 or heightmap[row-1][col] == 9):
		explore += getBasinSize(row-1, col, heightmap)
	
	#si se puede explorar a la derecha, seguimos buscando
	if not (col+1 >= len(heightmap[0]) or heightmap[row][col+1] == 9):
		explore += getBasinSize(row, col+1, heightmap)
	
	#si se puede explorar a la izquierda, seguimos buscando
	if not (col-1 < 0 or heightmap[row][col-1] == 9):
		explore += getBasinSize(row, col-1, heightmap)
	
	#una vez acabadas las exploraciones, devolvemos el valor encontrado 
	return explore


#calcula los 3 basins mas grandes
def calculateBasins(lowpoints, heightmap):
	#tamaño inicial: no hay -> 0
	basin1, basin2, basin3 = 0, 0, 0
	minPrev = 0

	#por cada lowpoint: calculamos su basin
	for row, col in lowpoints:
		actSize = getBasinSize(row, col, heightmap)
		#si el tamaño del basin actual es mayor que el minimo, sustituimos el menor
		if actSize > minPrev:
			#el menor es basin1
			if basin1 == minPrev:
				basin1 = actSize
			#el menor es basin2
			elif basin2 == minPrev:
				basin2 = actSize
			#el menor es basin3
			else:
				basin3 = actSize
			#actualizamos el valor de tamaño minimo
			minPrev = min([basin1, basin2, basin3])
		#si el tamaño es mayor o igual, no hacemos nada
	return [basin1, basin2, basin3]


#main de ejecucion
if __name__ == '__main__':
	heightmap = []
	#leemos el mapa
	readDigits(heightmap)
	#calculamos los lowpoints	
	lowpoints = calculateLowPoints(heightmap)
	#calculamos los 3 basins de mayor tamaño segun los lowpoints
	top3Basins = calculateBasins(lowpoints, heightmap)
	print(top3Basins[0]*top3Basins[1]*top3Basins[2])