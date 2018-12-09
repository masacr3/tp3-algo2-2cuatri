from heap import *

class Grafo:

    def __init__(self,dirigido = False):
        self.vertices = {}
        self.cantidad = 0
        self.dirigido = dirigido

    def agregarVertice(self, vertice):
        self.vertices[vertice] = {} #aca van los adyacentes
        self.cantidad += 1

    def agregarArista(self, vertice, adyacente, peso = 1):

        if vertice not in self.vertices:
            return False

        if not self.dirigido:
            self.vertices[adyacente][vertice] = peso

        self.vertices[vertice][adyacente] = peso
        return True

    def obtenerPeso(self, vertice, adyacente):

        if vertice not in self.vertices:
            return -1

        return self.vertices[vertice].get(adyacente, -1)

    def obtenerAdyacentes(self,vertice):
        return list(self.vertices[vertice])

    def __iter__(self):
        return iter(self.vertices)



def dfs(grafo, v, visitados, padres, orden):

    visitados[v] = v

    for w in grafo.obtenerAdyacentes(v):

        if w not in visitados:

            padres[w] = v
            orden[w] = orden[v] + 1
            dfs(grafo, w, visitados, padres, orden)

def DFS(grafo, origen):
    visitados = {}
    padres = {}
    orden = {}

    padres[origen] = None
    orden[origen] = 0

    dfs(grafo, origen, visitados, padres, orden)

    return padres, orden


INFINITO = 9999999 #simulamos un numero gigante

def cmp(a,b):
    dato1 = a[1]
    dato2 = b[1]

    if dato1 < dato2:
        return -1

    elif dato1 > dato2:
        return 1

    else:
        return 0


def DIJKSTRA(grafo, origen):

    padre = {}
    distancia = {}

    for vertice in grafo:
        distancia[vertice] = INFINITO

    distancia[origen] = 0
    padre[origen] = None

    array = []

    heap_encolar(array,[origen,distancia[origen]],cmp)

    while not len(array) == 0:
        vertice , peso = heap_desencolar(array, cmp)

        for adyacente in grafo.obtenerAdyacentes(vertice):
            distanciaActual = distancia[vertice] + grafo.obtenerPeso(vertice, adyacente)

            if distanciaActual < distancia[adyacente]:
                padre[adyacente] = vertice
                distancia[adyacente] = distanciaActual
                heap_encolar( array, [adyacente, distancia[adyacente]] , cmp )

    return padre, distancia
