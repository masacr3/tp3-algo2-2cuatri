from heap import *

class Grafo:

    def __init__(self,dirigido = False):
        self.vertices = {}
        self.cantidad = 0
        self.dirigido = dirigido

    def agregarVertice(self, vertice, dato):
        self.vertices[vertice] = (dato,{}) #aca van los adyacentes
        self.cantidad += 1

    def agregarArista(self, vertice, adyacente, peso):

        if not self.verticePertenece(vertice) or not self.verticePertenece(adyacente):
            return False

        if not self.dirigido:
            diccionario_a = self.vertices[adyacente][1]
            diccionario_a[vertice] = peso

        diccionario_v = self.vertices[vertice][1]
        diccionario_v[adyacente] = peso
        return True

    def obtenerPeso(self, vertice, adyacente):

        if vertice not in self.vertices:
            return None

        return self.vertices[vertice][1].get(adyacente, None)

    def obtenerAdyacentes(self,vertice):
        return list(self.vertices[vertice][1])

    def verticePertenece(self,vertice):
        return vertice in self.vertices

    def obtenerDatos(self,vertice):
        if not self.verticePertenece(vertice): return None
        return self.vertices[vertice][0]

    def __iter__(self):
        return iter(self.vertices)
