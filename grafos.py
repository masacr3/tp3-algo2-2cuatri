from heap import *
from cola import *

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
    return (a>b) - (a<b)


def DIJKSTRA(grafo, origen):

    padre = {}
    distancia = {}

    for vertice in grafo:
        distancia[vertice] = INFINITO

    distancia[origen] = 0
    padre[origen] = None

    heap = Heap(cmp)

    heap.encolar([origen,distancia[origen]])

    while not heap.esta_vacio():
        vertice , peso = heap.desencolar()

        for adyacente in grafo.obtenerAdyacentes(vertice):
            distanciaActual = distancia[vertice] + grafo.obtenerPeso(vertice, adyacente)

            if distanciaActual < distancia[adyacente]:
                padre[adyacente] = vertice
                distancia[adyacente] = distanciaActual
                heap.encolar([adyacente,distancia[adyacente]])

    return padre, distancia

def orden_topologico(grafo):
    grados = {}

    for vertice in grafo:
        grados[vertice] = 0

    for vertice in grafo:

        for adyacente in grafo.obtenerAdyacentes(vertice):
            grados[adyacente] += 1

    resultado = []
    cola = Cola()

    for vertice in grafo:

        if grados[vertice] == 0: cola.encolar(vertice)

    while not cola.esta_vacia():
        vertice = cola.desencolar()
        resultado.append(vertice)

        for adyacente in grafo.obtenerAdyacentes(vertice):
            grados[adyacente] -= 1

            if grados[adyacente] == 0: cola.encolar(adyacente)

    return None if len(resultado) == 0 else resultado
