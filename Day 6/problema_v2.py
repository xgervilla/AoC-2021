#lectura de los peces
def readOGfishes():
	f = open('input.txt', 'r')
	line = f.readline()
	return [int(val) for val in line.split(',')]

#calculo de un nuevo dia
def computeNewDay(fishes):
	#al decrementar un dia, los de 8 pasan a 7, los de 7 a 6.. -> los de 0, pasan a 6 Y 8
	auxFishes = fishes.copy()
	#en vez de ir pez a pez, movemos por bloque -> el dia 'i' pasa a tener los peces del dia siguiente --> se puede aplicar del 0 al 7
	for i in range(8):
		fishes[i] = fishes[i+1]
	#adicionalmente, los del dia 0 pasan a los del dia 6 (vuelven a contar para tener pececitos) Y a los del dia 8 (nuevos pececitos)
	fishes[6] += auxFishes[0]
	fishes[8] = auxFishes[0]

#contador de cuantos peces hay de cada "tipo" (dias que quedan hasta que ponga huevos)
def countFishes(fishes):
	#contador de 0 a 8
	counter = [0 for i in range(9)]
	#inicialmente no hay crias -> solo inicializamos de 0 a 6
	for i in range(7):
		counter[i] = len([f for f in fishes if f == i])
	return counter


if __name__ == '__main__':
	#leemos los peces
	fishes = readOGfishes()
	fishesCount = countFishes(fishes)
	#para el problema 1 cambiar de 256 a 80
	for i in range(256):
		computeNewDay(fishesCount)
		#obtenemos el numero de peces tras los 80 dias
	print(sum(fishesCount))
