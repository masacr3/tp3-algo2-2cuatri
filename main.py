from grafos import *

def main ():
    g = Grafo()

    vertices = ["a","b","c","d","e","f"]
    
    a = "a"
    b = "b"
    c = "c"
    d = "d"
    e = "e"
    f = "f"

    for vertice in vertices:
        g.agregarVertice(vertice)
    
    g.agregarArista(a,b)
    g.agregarArista(a,d)
    g.agregarArista(a,e)
    g.agregarArista(a,f)

    g.agregarArista(b,c)

    g.agregarArista(c,d)
    g.agregarArista(c,f)

    g.agregarArista(d,e)
    g.agregarArista(d,f)

    g.agregarArista(e,f)

    
    print("vertices")
    for v in g:
        print(v)

    print("\nAdyacentes")
    
    for v in g:
        print(v)
        for w in g.obtenerAdyacentes(v):
            print("\t",w)

    padre , orden = DFS(g,"a")

    print("padres",padre)
    print("orden",orden)


main()


