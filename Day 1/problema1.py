#abrimos el documento con el input en modo lectura
f = open("input.txt", 'r')
#valor previo
valPrev = -1
#contador de incrementos
cont = 0
#por cada linea (nuevo valor) vemos si se produce un incremento o no
for line in f:
  #cogemos con el valor actual
	words = line.split()
	valAct = int(words[0])
  #si el valor actual es mayor al previo (pero no es el primer valor de todos), incrementamos
	if valAct > valPrev and valPrev != -1:
		cont+=1
  #actualizamos el valor previo para la siguiente iteracion
	valPrev = valAct

print(cont)
