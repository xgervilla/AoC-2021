#abrimos el documento con el input en modo lectura
f = open("input.txt", 'r')
#variable para el valor de movimiento horizontal y de profundidad
horizontal, depth = 0, 0
#variable aim
aim = 0
#por cada linea, actuamos segun la instruccion
for line in f:
	#cogemos la instruccion y el valor asociado
	words = line.split()
	instruction = words[0]
	value = int(words[1])
	#si es forward, aumentamos horizontal y depth en funcion de aim
	if instruction == "forward":
		horizontal+=value
		depth+=aim*value
	#si es up, disminuimos aim
	elif instruction == "up":
		aim-=value
	#si es down, aumentamos aim
	elif instruction == "down":
		aim+=value

print(horizontal * depth)
