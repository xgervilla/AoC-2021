#abrimos el documento con el input en modo lectura
f = open("input.txt", 'r')
#vector para guardar el bit mas comun
mcbit = [0 for _ in range(12)]
#contador de lineas
contLines = 0
#por cada linea, actuamos segun la instruccion
for line in f:
	contLines+=1
	#cogemos los bits
	words = line.split()
	allBits = words[0]
	#por cada posicion (de los 12 bits)
	for pos in range(12):
		#acumulamos en el vector -> solo incrementa el valor los 1s
		mcbit[pos] += int(allBits[pos])

#al salir podemos identificar el bit mas comun
gammaRate, epsilonRate = 0, 0
for pos in range(12):
	#si el contador es mayor que la mitad del numero de lineas, mas 1s que 0s -> incrementamos gammaRate
	if mcbit[pos] > contLines/2:
		gammaRate+=2**(11-pos)
	#si hay mas 0s que 1s -> incrementamos epsilonRate
	else:
		epsilonRate+=2**(11-pos)

print(epsilonRate * gammaRate)
