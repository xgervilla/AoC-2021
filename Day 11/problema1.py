#leemos el mapa de alturas
def readDigits(octopusmap):
	f = open("input.txt", "r")
	for line in f:
		line = line.rstrip('\n')
		newLine = []
		for num in list(line):
			newLine.append(int(num))
		octopusmap.append(newLine)


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
def getAdjacents(row, col, octopusmap):
	#guardamos los limites del mapa
	minRow, maxRow = 0, len(octopusmap)-1
	minCol, maxCol = 0, len(octopusmap[0])-1

	#si el punto es esquina -> solo tiene 3 adyacentes (depende del tipo de esquina que sea)
	typeEsq = esEsquina(row, col, [minRow, maxRow, minCol, maxCol])
	if typeEsq > 0:
		#superior izquierda
		if typeEsq == 1:
			right = [row, col+1]
			down = [row+1, col]
			diag = [row+1, col+1]
			return [right, down, diag]
		#superior derecha
		elif typeEsq == 2:
			left = [row, col-1]
			down = [row+1, col]
			diag = [row+1, col-1]
			return [left, down, diag]
		#inferior izquierda
		elif typeEsq == 3:
			right = [row, col+1]
			up = [row-1, col]
			diag = [row-1, col+1]
			return [right, up, diag]
		#inferior derecha
		else:
			left = [row, col-1]
			up = [row-1, col]
			diag = [row-1, col-1]
			return [left, up, diag]
	#si no es esquina
	else:
		#si es borde -> solo tiene 5 adyacentes (depende del tipo de borde que sea)
		typeBorde = esBorde(row, col, [minRow, maxRow, minCol, maxCol])
		if typeBorde > 0:
			#izquierda
			if typeBorde == 1:
				right = [row, col+1]
				up = [row-1, col]
				down = [row+1, col]
				diag1, diag2 = [row-1, col+1], [row+1, col+1]
				return [right, up, down, diag1, diag2]
			#derecha
			elif typeBorde == 2:
				left = [row, col-1]
				up = [row-1, col]
				down = [row+1, col]
				diag1, diag2 = [row-1, col-1], [row+1, col-1]
				return [left, up, down, diag1, diag2]
			#arriba
			elif typeBorde == 3:
				left = [row, col-1]
				right = [row, col+1]
				down = [row+1, col]
				diag1, diag2 = [row+1, col-1], [row+1, col+1]
				return [left, right, down, diag1, diag2]
			#abajo
			else:
				left = [row, col-1]
				right = [row, col+1]
				up = [row-1, col]
				diag1, diag2 = [row-1, col-1], [row-1, col+1]
				return [left, right, up, diag1, diag2]
		#si no es esquina ni borde -> punto normal, 8 adyacentes
		else:
			left = [row, col-1]
			right = [row, col+1]
			up = [row-1, col]
			down = [row+1, col]
			diag1, diag2, diag3, diag4 = [row+1, col+1], [row+1, col-1], [row-1, col+1], [row-1, col-1]
			return [left, right, up, down, diag1, diag2, diag3, diag4]

#propagamos el flash de un pulpo
def propagateFlash(octopusmap, row, col):
	#obtenemos los adyacentes del pulpo en [row][col]
	adj = getAdjacents(row, col, octopusmap)
	#a cada uno de ellos, propagamos
	for rowP, colP in adj:
		#si no ha flasheado ya, incrementamos
		if octopusmap[rowP][colP] != -1:
				octopusmap[rowP][colP]+=1
				#si tras incrementar es mayor de 9, propagamos el flash
				if octopusmap[rowP][colP] >9:
					#lo marcamos como que ha flasheado
					octopusmap[rowP][colP] = -1
					propagateFlash(octopusmap, rowP, colP)

#devuelve el numero de flashes de un dia
def getFlashes(octopusmap):
	newFlashes = 0

	#por cada pulpo, incrementamos el contador -> si >9 -> flashea e incrementa los que rodea (DIAGONALES INCLUIDAS)
	rows = len(octopusmap)
	cols = len(octopusmap[0])

	#flashea e incrementa adyacentes -> los que han flasheado los marcamos con -1
	for row in range(rows):
		for col in range(cols):
			#si no es un pulpo que ya ha flasheado, incrementamos el contador
			if octopusmap[row][col] != -1:
				octopusmap[row][col]+=1
				#si tras incrementar es mayor de 9, propagamos el flash
				if octopusmap[row][col] >9:
					#lo marcamos como que ha flasheado
					octopusmap[row][col] = -1
					propagateFlash(octopusmap, row, col)


	#dejamos los que han flasheado a 0 y los contamos
	for row in range(rows):
		for col in range(cols):
			if octopusmap[row][col] == -1:
				newFlashes+=1
				octopusmap[row][col] = 0
	return newFlashes

#printeamos el mapa de puplos (de forma "bonita")
def prettyPrint(octopusmap):
	rows = len(octopusmap)
	cols = len(octopusmap[0])
	for row in range(rows):
		for col in range(cols):
			print(octopusmap[row][col], end=' ')
		print()
	print()


#main de ejecucion
if __name__ == '__main__':
	#leemos el mapa de pulpos
	octopusmap = []
	readDigits(octopusmap)

	flashes, numDays = 0, 100
	#obtenemos el numero de flashes despues de 100 dias
	for i in range(numDays):
		flashes += getFlashes(octopusmap)
	
	#printeamos el mapa resultante y el numero de flashes que se han producido
	prettyPrint(octopusmap)
	print(flashes)