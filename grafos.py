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

        if not self.verticePertenece(vertice) or not self.verticePertenece(adyacente):
            return False

        if not self.dirigido:
            self.vertices[adyacente][vertice] = peso

        self.vertices[vertice][adyacente] = peso
        return True

    def obtenerPeso(self, vertice, adyacente):

        if vertice not in self.vertices:
            return -1

        return self.vertices[vertice][adyacente]

    def obtenerAdyacentes(self,vertice):
        return list(self.vertices[vertice])

    def verticePertenece(self,vertice):
        return vertice in self.vertices

    def __iter__(self):
        return iter(self.vertices)
