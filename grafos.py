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

    def verticePertenece(self,vertice):
        return vertice in self.vertices

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

    if not grafo.verticePertenece(origen): return None,None

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


def betweenness_centrality(grafo,n):
    res = []
    apariciones = {}
    l_padres = []
    for v in grafo:
        apariciones[v]= 0
        padre,distancia = DIJKSTRA(grafo,v)
        l_padres.append(padre)

    for padres in l_padres:
        for w in padres:
            if(padres[w]): apariciones[padres[w]]+=1

    print(apariciones)
    num_apariciones = list(apariciones.values())
    vertices = list(apariciones.keys())
    i = 0
    while i<n and vertices:
        pos = num_apariciones.index(max(num_apariciones))
        clave = vertices[pos]
        res.append(clave)
        num_apariciones.pop(pos)
        vertices.pop(pos)
        i+=1

    return res
