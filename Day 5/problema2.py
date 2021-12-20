import numpy as np

#lectura del input
def readVents(vents):
    f = open('input.txt', 'r')
    maxRow, maxCol = 0, 0
  #por cada linea leemos las coordenadas de partida y destino
    for line in f:
        elem1, _, elem2 = line.split()
        xOrig, yOrig = elem1.split(',')
        xDest, yDest = elem2.split(',')
        vents.append([int(xOrig), int(yOrig), int(xDest), int(yDest)])
    maxNums = np.amax(vents, axis = 1)
    return max(maxNums) + 1


#llenamos el mapa del oceano con las diferentes hydrotermal vents
def fillVents(vents, mapOcean):
    for xOrig, yOrig, xDest, yDest in vents:
        #movimiento en vertical (cambia X)
        verMov = xOrig != xDest
        #movimiento en horizontal (cambia Y)
        horMov = yOrig != yDest
        #si es movimiento SOLO vertical
        if verMov and not horMov:
            minRow, maxRow = min(xOrig, xDest), max(xOrig,xDest)
            for row in range(minRow, maxRow+1):
                mapOcean[row][yOrig]+=1
        #si es movimiento SOLO horizontal
        elif not verMov and horMov:
            minCol, maxCol = min(yOrig, yDest), max(yOrig, yDest)
            for col in range(minCol, maxCol+1):
                mapOcean[xOrig][col]+=1
        #si es un solo punto, incrementamos el contador
        elif not verMov and not horMov:
            mapOcean[xOrig][yOrig]+=1
        #es movimiento diagonal
        else:
            #obtenemos la direccion en la que avanzamos
            dirX = 1 if xOrig < xDest else -1
            dirY = 1 if yOrig < yDest else -1
            #desde la posicion inicial (origen), incrementamos las coordenadas hasta llegar a la posicion destino
            posX, posY = xOrig, yOrig
            mapOcean[posX][posY] +=1
            while posX != xDest and posY != yDest:
                posX, posY = posX+dirX, posY+dirY
                mapOcean[posX][posY] +=1

#contamos donde se cruzan las vents en el mapa (valor mayor de 1)
def calculateVents(mapOcean):
    cont = 0
    for row in mapOcean:
        for val in row:
            if val > 1:
                cont+=1
    return cont



if __name__ == '__main__':
  #leemos las hydrotemral vents
    vents = []
    maxSize = readVents(vents)
  #creamos el mapa del oceano (todo 0s)
    mapOcean = [[] for _ in range(maxSize)]
    for i in range(maxSize):
        mapOcean[i] = [0 for _ in range(maxSize)]
  #rellenamos el mapa con las vents
    fillVents(vents, mapOcean)
  #obtenemos el numero de puntos en los que se cruzan
    print(calculateVents(mapOcean))
