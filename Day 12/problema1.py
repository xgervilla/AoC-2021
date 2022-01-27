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


#obtenemos un path
def getPath(graph, visited, node, actualPath, allPaths):
	#hemos llegado al final
	if node == "end":
		#añadimos el nodo final y copiamos el camino para añadirlo al conjunto de caminos
		actualPath.append(node)
		pathCopy = actualPath.copy()
		#lo añadimos al conjunto
		allPaths.append(pathCopy)
		#quitamos el nodo final
		actualPath.pop()
	
	#nuevo nodo
	elif not visited[node]:
		#incrementamos el numero de visitas y lo añadimos al path actual
		visited[node]+=1
		actualPath.append(node)
		#cogemos el conjunto de cuevas que podemos visitar
		possibleNodes = [n for n in graph[node] if n.isupper() or visited[n]<1]
		#visitamos las cuevas disponibles
		for neighbour in possibleNodes:
			getPath(graph, visited, neighbour, actualPath, allPaths)
		#si es cueva "sencilla", decrementamos el contador para el backtracking
		if not node.isupper():
			visited[node]-=1
		actualPath.pop()
	
	#repetimos nodo
	else:
		#cueva grande -> se puede visitar infinidad de veces
		if node.isupper():
			visited[node]+=1
			#añadimos el nodo al camino y visitamos los vecinos validos
			actualPath.append(node)
			possibleNodes = [n for n in graph[node] if n.isupper() or visited[n]<1]
			for neighbour in possibleNodes:
				getPath(graph, visited, neighbour, actualPath, allPaths)
			actualPath.pop()

		#cueva pequeña -> limite de 1 visita
		else:
			#podemos pasar por la cueva
			if visited[node] <1:
				#incrementamos el contador para marcar que la hemos visitado
				visited[node]+=1
				#añadimos el nodo al camino y visitamos los vecinos validos
				actualPath.append(node)
				possibleNodes = [n for n in graph[node] if n.isupper() or visited[n]<1]
				for neighbour in possibleNodes:
					getPath(graph, visited, neighbour, actualPath, allPaths)
				visited[node]-=1
				actualPath.pop()
			#si no podemos pasar, no hacemos nada



#obtenemos todos los paths del cave system partiendo de start
def getAllPaths(graph):
	#marcamos todas las cuevas como no visitadas
	visited = {}
	for node in graph.keys():
		visited[node] = 0
	#conjunto de paths y path actual, ambos inicialmente vacios
	actualPath, allPaths = [], []
	getPath(graph, visited, "start", actualPath, allPaths)
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