#leemos los digitos
def readDigits(inDigits, outDigits):
	f = open("input.txt", "r")
	for line in f:
		#separamos en entrada y salida
		inDig, outDig = line.split("|")
		ins, outs = [], []
		for digit in inDig.split():
			ins.append(digit)

		inDigits.append(ins)
		
		for digit in outDig.split():
			outs.append(digit)

		outDigits.append(outs)

#encuentra el numero -> intersecta leftDig con digitsOrig y devuelve el digito que tenga tamaño num
def findNum(digitsOrig, leftDig, num):
	for digits in leftDig:
		dig = set(list(digits))
		if len(dig.intersection(digitsOrig)) == num:
			leftDig.remove(digits)
			return digits
	return None


#decodificamos los digitos
def decodeDigits(digits):
	'''	
	  7-segment		codificacion de los digitos
					1: 2,5 -> |1| = 2 --> directo
		 aaaa   	7: 0,2,5 -> |7| = 3 --> directo
		b    c 		4: 1,2,3,5 -> |4| = 4 --> directo
		b    c 		2: 0,2,3,4,6 -> |2| = 5 --> el que queda de tamaño 5
		 dddd 		3: 0,2,3,5,6 -> |3| = 5 --> interseccion con el 1, tamaño 2
		e    f 		5: 0,1,3,5,6 -> |5| = 5 --> interseccion con el 9, tamaño 5
		e    f		0: 0,1,2,4,5,6 -> |0| = 6 --> el que queda de tamaño 6
		 gggg		6: 0,1,3,4,5,6 -> |6| = 6 --> interseccion con el 5, tamaño 5
		 			9: 0,1,2,3,5,6 -> |9| = 6 --> interseccion con el 4, tamaño 4
					8: 0,1,2,3,4,5,6 -> |8| = 7 --> directo
	'''

	#ordenamos los digitos segun su longitud
	digits = sorted(digits, key=len)

	#codificadcion de cada numero
	numbers = [[] for i in range(10)]

	#1,4,7,8 directos
	#numero 1 -> palabra con longitud 2 (mas corta)
	numbers[1] = ''.join(sorted(list(digits[0])))
	digits1 = set(list(numbers[1]))

	#numero 4 -> palabra con longitud 4 (tecera mas corta)
	numbers[4] = ''.join(sorted(list(digits[2])))
	digits4 = set(list(numbers[4]))

	#numero 7 -> palabra con longitud 3 (la segunda mas corta)
	numbers[7] = ''.join(sorted(list(digits[1])))

	#numero 8 -> palabra con lomgitud 7 (mas larga)
	numbers[8] = ''.join(sorted(list(digits[9])))

	#el resto se obtienen al intersectar
	#separamos por tamaño
	size5 = [dig for dig in digits if len(dig) == 5]
	size6 = [dig for dig in digits if len(dig) == 6]

	#numero 3 -> interseccion de los de tamaño 5 con el 1 que tenga tamaño 2
	num3 = findNum(digits1, size5, 2)
	numbers[3] = ''.join(sorted(list(num3)))

	#numero 9 -> interseccion de los de tamaño 6 con el 4 que tenga tamaño 4
	num9 = findNum(digits4, size6, 4)
	numbers[9] = ''.join(sorted(list(num9)))
	digits9 = set(list(numbers[9]))

	#numero 5 -> interseccion de los de tamaño 5 con el 9 que tenga tamaño 5
	num5 = findNum(digits9, size5, 5)
	numbers[5] = ''.join(sorted(list(num5)))
	digits5 = set(list(numbers[5]))

	#numero 6 -> interseccion de los de tamaño 6 con el 5 que tenga tamaño 5
	num6 = findNum(digits5, size6, 5)
	numbers[6] = ''.join(sorted(list(num6)))

	#numero 0 -> el que queda de tamaño 6
	numbers[0] = ''.join(sorted(list(size6[0])))
	#numero 2 -> el que queda de tamaño 5
	numbers[2] = ''.join(sorted(list(size5[0])))

	return numbers

#calcula el output de cada entrada
def calculateOutput(decodeDigits, outDigits):
	#valor decimal
	val = 0
	#ordenamos los digitos alfabeticamente para comparar
	dig1 = ''.join(sorted(list(outDigits[0])))
	dig2 = ''.join(sorted(list(outDigits[1])))
	dig3 = ''.join(sorted(list(outDigits[2])))
	dig4 = ''.join(sorted(list(outDigits[3])))

	#comprobamos los 10 digitos posibles
	for i in range(10):
		if decodeDigits[i] == dig1:
			val += 1000*i
		if decodeDigits[i] == dig2:
			val += 100*i
		if decodeDigits[i] == dig3:
			val += 10*i
		if decodeDigits[i] == dig4:
			val += i
	#devolvemos el valor calculado
	return val



if __name__ == '__main__':
	inDigits, outDigits = [], []
	#leemos los digitos
	readDigits(inDigits, outDigits)
	sumOutputs = 0
	#por cada par entrada-salida, encontramos la codificacion y segun el input y acumulamos el output
	for inp, out in zip(inDigits, outDigits):
		decodedDigits = decodeDigits(inp)
		sumOutputs += calculateOutput(decodedDigits, out)
	print(sumOutputs)