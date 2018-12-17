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

    g.agregarArista(c,d,1)
    g.agregarArista(c,f,1)

    g.agregarArista(d,e,4)
    g.agregarArista(d,f,1)

    g.agregarArista(e,f,2)

    padres, distancia = DIJKSTRA(g, "a")

    print("Dijkstra A:")
    print("padres: ",padres)
    print("distancia: ",distancia)

    padres, distancia = DIJKSTRA(g, "b")

    print("Dijkstra B:")
    print("padres: ",padres)
    print("distancia: ",distancia)

    padres, distancia = DIJKSTRA(g, "c")

    print("Dijkstra C:")
    print("padres: ",padres)
    print("distancia: ",distancia)

    padres, distancia = DIJKSTRA(g, "d")

    print("Dijkstra D:")
    print("padres: ",padres)
    print("distancia: ",distancia)

    padres, distancia = DIJKSTRA(g, "e")

    print("Dijkstra E:")
    print("padres: ",padres)
    print("distancia: ",distancia)

    padres, distancia = DIJKSTRA(g, "f")

    print("Dijkstra F:")
    print("padres: ",padres)
    print("distancia: ",distancia)

    padres, distancia = DIJKSTRA(g, "g")

    print("Dijkstra G:")
    print("padres: ",padres)
    print("distancia: ",distancia)

    print("centralidad grafo1: ",centralidad(g))

    g2 = Grafo(True)

    vertices = ["a","b","c","d","e","f","h"]

    a = "a"
    b = "b"
    c = "c"
    d = "d"
    e = "e"
    f = "f"
    h = "h"

    for vertice in vertices:
        g2.agregarVertice(vertice)

    g2.agregarArista(b,a,1)
    g2.agregarArista(a,c,2)
    g2.agregarArista(d,a,2)
    g2.agregarArista(a,f,1)
    g2.agregarArista(e,f,3)
    g2.agregarArista(f,h,2)

    print("centralidad grafo 2: ",centralidad(g2))

main()
