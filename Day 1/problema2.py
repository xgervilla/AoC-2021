#abrimos el documento con el input en modo lectura
f = open("input.txt", 'r')
#contador de incrementos
contIncrease = 0
#valores auxiliares para las tripletas de datos
val1, val2, val3 = -1, -1, -1
#por cada linea (nuevo valor):
for line in f:
	#cogemos el valor actual
	words = line.split()
	valAct = int(words[0])
	
	#"rellenamos" los tres primeros valores
	if val1== -1:
		val1 = valAct
	elif val2 == -1:
		val2 = valAct
	elif val3 == -1:
		val3 = valAct

	#una vez tenemos los tres primeros valores, vamos desplazando la suma para ver si la actual es mayor que la previa
	else:
		#suma actual: no consideramos el val1
		sumAct = val2+val3+valAct
		#suma previa: no consideramos el valor actual
		sumaPrev = val1+val2+val3
		#actualizamos los valores
		val1, val2, val3 = val2, val3, valAct
		#incrementamos el contador si es necesario
		if sumAct > sumaPrev:
			contIncrease +=1
		##optimizacion: los unicos valores que cambian entre sumaAct y sumaPrev son val1 y valAct por lo que se podria comprobar directamente si valAct>val1
print(contIncrease)
