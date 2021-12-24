#leemos el mapa de alturas
def readLines(lines):
	f = open("input.txt", "r")
	for line in f:
		line = line.rstrip('\n')
		newLine = []
		for char in list(line):
			newLine.append(char)
		lines.append(newLine)

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
		#si es simbolo de cierre, si NO coincide con el ultimo simbolo de la pila es ilegal -> devolvemos su tipo
		elif char == ')':
			lastChar = stack.pop()
			if lastChar != 0:
				return 0
		elif char == ']':
			lastChar = stack.pop()
			if lastChar != 1:
				return 1
		elif char == '}':
			lastChar = stack.pop()
			if lastChar != 2:
				return 2
		elif char == '>':
			lastChar = stack.pop()
			if lastChar != 3:
				return 3
	#si lo que falla es que faltan cierres (no hemos encontrado un cierre erroneo) devolvemos un -1
	return -1

#buscamos en todas las lineas el caracter que falla
def filterIncomplete(lines):
	#	    ) ] } >
	cont = [0,0,0,0]

	#por cada linea: buscamos el caracter ilegal y aumentamos su contador
	for line in lines:
		#buscamos el caracter ilegal
		illegalChar = findIC(line)
		#si no es incompleta (-1), incrementamos el contador del char
		if illegalChar != -1:
			cont[illegalChar]+=1
	#devolvemos los contadores
	return cont


#main de ejecucion
if __name__ == '__main__':
	lines = []
	#leemos las lineas
	readLines(lines)
	#contamos cada char ilegal separando por tipos
	totalPoints = filterIncomplete(lines)
	print(totalPoints)
	#calculamos los puntos
	totalPoints[0] = totalPoints[0]*3 		# ')'
	totalPoints[1] = totalPoints[1]*57 		# ']'
	totalPoints[2] = totalPoints[2]*1197 	# '}'
	totalPoints[3] = totalPoints[3]*25137 	# '>'
	print(sum(totalPoints))
	