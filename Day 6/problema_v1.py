#lectura de los peces iniciales
def readOGfishes():
	f = open('input.txt', 'r')
	line = f.readline()
	return [int(val) for val in line.split(',')]

#calculo de un nuevo dia
def computeNewDay(fishes):
	countNewFishes = 0
	for i in range(len(fishes)):
		if fishes[i] == 0:
			fishes[i] = 6
			countNewFishes+=1
		else:
			fishes[i]-=1
	for i in range(countNewFishes):
		fishes.append(8)


if __name__ == '__main__':
	#leemos los peces iniciales (dias que faltan para que pongan huevos)
	fishes = readOGfishes()
	#calculamos dia a dia como evoluciona la poblacion de peces
	for i in range(80):
		computeNewDay(fishes)
	#obtenemos el numero de peces tras los 80 dias
	print(len(fishes))
