from numpy import median

#leemos el mapa de alturas
def readLines(lines):
	f = open("input.txt", "r")
	for line in f:
		line = line.rstrip('\n')
		newLine = []
		for char in list(line):
			newLine.append(char)
		lines.append(newLine)

#calcula la puntuacion de una completion string
def getValue(chars):
	'''
	) -> 0 --> 0+1
	] -> 1 --> 1+1
	} -> 2 --> 2+1
	> -> 3 --> 3+1
	'''
	value = 0
	for c in chars:
		value = value*5 + c + 1
	return value

	

#buscamos en una linea el caracter que falla, -1 si no falla ninguno (solo esta incompleta)
def findIC(line):
	stack = []
	for char in line:
		#si es simbolo de apertura, lo añadimos a la pila
		if char == '(':
			stack.append(0)
		elif char == '[':
			stack.append(1)
		elif char == '{':
			stack.append(2)
		elif char == '<':
			stack.append(3)
		#si es simbolo de cierre, si NO coincide con el ultimo simbolo de la pila es ilegal -> devolvemos []
		elif char == ')':
			lastChar = stack.pop()
			if lastChar != 0:
				return []
		elif char == ']':
			lastChar = stack.pop()
			if lastChar != 1:
				return []
		elif char == '}':
			lastChar = stack.pop()
			if lastChar != 2:
				return []
		elif char == '>':
			lastChar = stack.pop()
			if lastChar != 3:
				return []
	#si no hay ningun caracter ilegal, calculamos los simbolos que faltan por poner
	chars = []
	while stack != []:
		chars.append(stack.pop())
	return chars

#buscamos en todas las lineas el caracter que falla
def filterIllegal(lines):
	#por cada linea: buscamos el caracter ilegal y aumentamos su contador
	allCompletions = []
	for line in lines:
		#buscamos la string a completar
		completionString = findIC(line)
		#si no es ilegal ([]), caclulamos el valor y lo añadimos al conjunto de 
		if completionString != []:
			allCompletions.append(getValue(completionString))
	#devolvemos los contadores
	return allCompletions


#main de ejecucion
if __name__ == '__main__':
	lines = []
	#leemos las lineas
	readLines(lines)
	#contamos cada char ilegal separando por tipos
	totalPoints = filterIllegal(lines)
	print(totalPoints)
	#ordenamos los puntos
	totalPoints = sorted(totalPoints)
	#nos quedamos con el valor del medio
	print(median(totalPoints))