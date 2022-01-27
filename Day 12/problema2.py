#lectura del grafo (cave system)
def readGraph(graph):
	f = open("input.txt", "r")
	for line in f:
		v1, v2 = line.rstrip('\n').split('-')
		#añadimos la conexion entre cuevas
		if v1 in graph.keys():
			graph[v1].append(v2)
		else:
			graph[v1] = [v2]
		#adireccional (añadimos en ambas cuevas)
		if v2 in graph.keys():
			graph[v2].append(v1)
		else:
			graph[v2] = [v1]

#scu: small cave used -> true si ya hay una cueva pequeña usada dos veces
#obtenemos un path
def getPath(graph, visited, node, actualPath, allPaths, scu):
	#final del camino
	if node == "end":
		actualPath.append(node)
		#hemos llegado al final -> lo añadimos al conjunto de caminos
		pathCopy = actualPath.copy()
		allPaths.append(pathCopy)
		actualPath.pop()
	
	#nuevo nodo
	elif not visited[node]:
		#incrementamos el numero de visitas y lo añadimos al path actual
		visited[node]+=1
		actualPath.append(node)
		possibleNodes = [n for n in graph[node] if n!= "start" and (n.isupper() or (visited[n]<2 and not scu) or (visited[n]<1 and scu))]
		for neighbour in possibleNodes:
			getPath(graph, visited, neighbour, actualPath, allPaths,scu)
		if not node.isupper():
			visited[node]-=1
		actualPath.pop()
	
	#repetimos nodo
	else:
		#cueva grande
		if node.isupper():
			visited[node]+=1
			actualPath.append(node)
			possibleNodes = [n for n in graph[node] if n!= "start" and (n.isupper() or (visited[n]<2 and not scu) or (visited[n]<1 and scu))]
			for neighbour in possibleNodes:
				getPath(graph, visited, neighbour, actualPath, allPaths, scu)
			actualPath.pop()

		#cueva pequeña -> limite de 2 visitas si scu = False, 1 otherwise
		else:
			#si ya hemos pasado por una cueva pequeña dos veces
			if scu:
				#podemos pasar por la cueva
				if visited[node] < 1:
					visited[node]+=1
					actualPath.append(node)
					possibleNodes = [n for n in graph[node] if n!= "start" and (n.isupper() or visited[n]<1)]
					for neighbour in possibleNodes:
						getPath(graph, visited, neighbour, actualPath, allPaths, scu)
					visited[node]-=1
					actualPath.pop()
				#si no podemos pasar, no hacemos nada
			#si todavia no hemos pasado por una cueva pequeña dos veces
			else:
				#podemos pasar una segunda vez
				if visited[node] == 1:
					visited[node]+=1
					actualPath.append(node)
					possibleNodes = [n for n in graph[node] if n!= "start" and (n.isupper() or visited[n]<1)]
					for neighbour in possibleNodes:
						getPath(graph, visited, neighbour, actualPath, allPaths, True)
					visited[node]-=1
					actualPath.pop()

#obtenemos todos los paths del cave system partiendo de start y sin haber visitado una cueva pequeña dos veces
def getAllPaths(graph):
	#marcamos todas las cuevas como no visitadas
	visited = {}
	for node in graph.keys():
		visited[node] = 0
	#conjunto de paths y path actual, ambos inicialmente vacios
	actualPath, allPaths = [], []
	getPath(graph, visited, "start", actualPath, allPaths, False)
	return allPaths

#print de todos los paths -> por cada path, imprime las cuevas que lo forman
def ppPaths(allPaths):
	for path in allPaths:
		for cave in path:
			print(cave + " ", end="")
		print()

#main de ejecucion
if __name__ == '__main__':
	#leemos el grapho que forma el sistema de cuevas
	graph = {}
	readGraph(graph)
	#obtenemos todos los caminos
	allPaths = getAllPaths(graph)
	print("There are "+str(len(allPaths))+" paths")
	#ppPaths(allPaths)