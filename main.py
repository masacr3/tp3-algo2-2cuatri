from grafos import *
from biblioteca import *

def main ():
    g = Grafo(True)

    vertices = ["a","b","c","d","e","f"]

    a = "a"
    b = "b"
    c = "c"
    d = "d"
    e = "e"
    f = "f"

    for vertice in vertices:
        g.agregarVertice(vertice)

    g.agregarArista(a,b,1)
    g.agregarArista(a,d,4)
    g.agregarArista(a,e,7)
    g.agregarArista(a,f,8)

    g.agregarArista(b,c,2)
    g.agregarArista(b,d,1)

    g.agregarArista(c,d,1)
    g.agregarArista(c,f,1)

    g.agregarArista(d,e,4)
    g.agregarArista(d,f,1)

    g.agregarArista(e,f,2)

    padre , orden = BFS(g,a)

    actual = c
    camino = []
    camino2 = [a,d]

    while actual != None:
        camino.append(actual)
        actual = padre[actual]

    camino.reverse()

    mostrarCamino(camino)
    mostrarCamino(camino2)


main()
