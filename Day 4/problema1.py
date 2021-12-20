def readNumbers(boards, numbers):
	f = open("input 4.txt", 'r')
	#booleano para indicar que es la primera linea (la que contiene los numeros)
	num = False
	boardLine = 0
	contBoards = 0
	for line in f:
		line = line.rstrip("\n")
		#si es la primera linea:
		if not num:
			num = True
			#por cada numero de la lista de valores, lo añadimos al conjunto de numeros
			for n in line.split(","):
				numbers.append(int(n))
		#si no es la primera linea Y no es una linea "de paso"
		elif line != "":
			#si es una nueva board, la creamos
			if boardLine == 0:
				#incrementamos el numero de boards
				contBoards+=1
				#cada board tiene 2 objetos, una lista de numeros y el tablero
				boards[contBoards] = [[],[]]
				#la lista de numero si inicializa vacia
				boards[contBoards][0] = []
				#el tablero se inicializa como un vector de 5 casillas
				boards[contBoards][1] = [[],[],[],[],[]]
				#asignamos los 5 numeros de la fila
				for n in line.split():
					#añadimos el numero
					boards[contBoards][0].append(int(n))
					boards[contBoards][1][0].append(int(n))
				#incrementamos el numero de fila para la siguiente iteración
				boardLine+=1
			
			#si es una board ya existente
			else:
				#los vectores ya están inicializados, sólo debemos asignar los numeros de la fila en la que estamos
				for n in line.split():
					boards[contBoards][0].append(int(n))
					boards[contBoards][1][boardLine].append(int(n))
				#incrementamos el numero de fila, si llegamos a 5, reiniciamos	
				boardLine+=1
				boardLine%=5


def checkRow(key, row):
	#por cada columna
	for col in range(5):
		#si en la posicion NO hay un -1 (centinela), hay un valor -> no hay bingo
		if boards[key][1][row][col] != -1:
			return False
	#si todo es -1, devolvemos true
	return True


def checkCol(key, col):
	#por cada columna
	for row in range(5):
		#si en la posicion NO hay un -1 (centinela), hay un valor -> no hay bingo
		if boards[key][1][row][col] != -1:
			return False
	#si todo es -1, devolvemos true
	return True


def getVal(key):
	boardAux = boards[key][1]
	suma = 0
	for row in range(5):
		for col in range(5):
			if boardAux[row][col] != -1:
				suma+=boardAux[row][col]
	return suma



def checkNum(boards, num):
	#por cada board
	for key in boards.keys():
		#variable auxiliar para marcar que lo hemos encontrado en la board
		foundInBoard = False
		if num in boards[key][0]:
			#lo buscamos en cada fila y columna
			for row in range(5):
				if foundInBoard:
						break
				for col in range(5):
					if foundInBoard:
						break
					#si encontramos el numero
					if boards[key][1][row][col] == num:
						#marcamos que lo hemos encontrado
						foundInBoard = True
						#marcamos la posicion con un centinela
						boards[key][1][row][col] = -1
						#si hay bingo en la fila o la columna, devolvemos el tablero ganador
						if checkRow(key, row) or checkRow(key, col):
							return key, num*getVal(key)
					#si no lo encontramos seguimos buscando

		#si el tablero no tiene el numero, no hacemos nada

	#si no hemos encontrado ganador, devolvemos key = -1
	return -1, 0


if __name__ == '__main__':
	boards = {}
	numbers = []
	readNumbers(boards, numbers)


	for num in numbers:
		identifier, value = checkNum(boards, num)
		if identifier != -1:
			print("Winner found:\nKey: "+str(identifier)+"\nValue: "+str(value))
			break
