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

    def obternerPeso(self, vertice, adyacente):
        
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


