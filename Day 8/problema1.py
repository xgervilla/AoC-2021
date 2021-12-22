#leemos los digitos
def readDigits(digits):
	f = open("input.txt", "r")
	for line in f:
		#solo nos interesan los outputs
		_, outDig = line.split("|")
		for digit in outDig.split():
			digits.append(digit)

#contamos los digitos que sean 1, 4, 7 y 8 (tamaño 2,3,4 y 7)
def contDigs(digits):
	cont = 0
	digits1478 = [2, 3, 4, 7]
	for dig in digits:
		if len(dig) in digits1478:
			cont+=1
	return cont

#main de ejecucion
if __name__ == '__main__':
	digits = []
	#leemos los digitos de output
	readDigits(digits)
	#contamos los numeros
	prin(contDigs(digits))