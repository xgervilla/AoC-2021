#abrimos el documento con el input en modo lectura
f = open("input.txt", 'r')
#variable para el valor de movimiento horizontal y de profundidad
horizontal, depth = 0, 0
#por cada linea, actuamos segun la instruccion
for line in f:
	#cogemos la instruccion y el valor asociado
	words = line.split()
	instruction = words[0]
	value = int(words[1])
	#si es forward, aumentamos horizontal
	if instruction == "forward":
		horizontal+=value
	#si es up, disminuimos depth
	elif instruction == "up":
		depth-=value
	#si es down, aumentamos depth
	elif instruction == "down":
		depth+=value

print(horizontal * depth)
