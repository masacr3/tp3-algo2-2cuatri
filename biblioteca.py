# DFS (grafo, origen)
# DIJKSTRA (grafo, origen, cmp_dijkstra)
# ORDEN_TOPOLOGICO(grafo)
# PRIM (grafo, origen, cmp_prim)

# ? CENTRALIDAD(grafo)

from grafos import *
from colas import *

"""
def dfs(grafo, v, visitados, padres, orden):

    visitados[v] = v

    for w in grafo.obtenerAdyacentes(v):

        if w not in visitados:

            padres[w] = v
            orden[w] = orden[v] + 1
            dfs(grafo, w, visitados, padres, orden)

def DFS(grafo, origen):
    visitados = {}
    padre = {}
    orden = {}

    padre[origen] = None
    orden[origen] = 0

    dfs(grafo, origen, visitados, padre, orden)

    return padres, orden
"""

def DFS(grafo, origen, visitados, l,n,etapa):

    if etapa > n : return False

    visitados[origen] = origen
    l.append(origen)

    for w in grafo.obtenerAdyacentes(origen):
        if es_solucion(grafo, w, visitados, l,n):
            return True

        if w not in visitados :
            if DFS(grafo, w, visitados, l,n,etapa + 1 ):
                return True


    del visitados[origen]
    l.pop()
    return False

def es_solucion(grafo, v, visitados, l, n):

    if v in visitados and len(visitados) == n and l[0] == v:
        l.append(v)
        return True
    return False

def BFS(grafo, origen):

    if origen not in grafo: return None, None

    visitados = {}
    padre = {}
    orden = {}

    padre[origen] = None
    orden[origen] = 0
    visitados[origen] = origen

    q = Cola()

    q.encolar(origen)

    while not q.esta_vacia():
        v = q.desencolar()

        for w in grafo.obtenerAdyacentes(v):

            if w not in visitados:
                visitados[w] = w
                padre[w] = v
                orden[w] = orden[v] + 1
                q.encolar(w)

    return padre, orden

def random_adyacente(grafo,v):
    l = grafo.obtenerAdyacentes(v)
    return random.choice(l)

def _random_walk(grafo,n,i,recorrido,v):
    if i >= n: return
    recorrido.append(v)
    siguiente = random_adyacente(grafo,v)
    _random_walk(grafo,n,i+1,recorrido,siguiente)


def Random_walk(grafo,n):
    origen = random.choice(grafo.obtenerVertices())
    recorrido = []
    _random_walk(grafo,n,0,recorrido,origen)
    return recorrido

def mostrarCamino(camino):
    for i in range(len(camino)-1):
        print("{} -> ".format(camino[i]), end = "")
    print(camino[-1])


INFINITO = 9999999 #simulamos un numero gigante

def cmp(a,b):
    return (a>b) - (a<b)


def DIJKSTRA(grafo, origen, cmp_dijkstra,index):

    if origen not in grafo:
        return None,None

    padre = {}
    distancia = {}

    for vertice in grafo:
        distancia[vertice] = INFINITO

    distancia[origen] = 0
    padre[origen] = None

    heap = Heap(cmp_dijkstra)

    heap.encolar([origen,distancia[origen]])

    while not heap.esta_vacio():
        vertice , peso = heap.desencolar()

        for adyacente in grafo.obtenerAdyacentes(vertice):
            distanciaActual = distancia[vertice] + grafo.obtenerPeso(vertice, adyacente)[index]

            if distanciaActual < distancia[adyacente]:

                padre[adyacente] = vertice
                distancia[adyacente] = distanciaActual
                heap.encolar([adyacente,distancia[adyacente]])


    return padre, distancia

def ordenar_vertices(distancias):
    l = []
    for v in distancias:
        if(distancias[v] == INFINITO): continue
        l.append((v,distancias[v]))
    l.sort(reverse = True,key=lambda x: x[1])
    return l

def obtener_centralidad(grafo,f_cmp,index):
    cent = {}
    for v in grafo: cent[v] = 0
    for v in grafo:
        #padre, distancia = DIJKSTRA(grafo,v,f_cmp,index)
        padre, distancia = BFS(grafo,v)
        cent_aux = {}
        for w in grafo: cent_aux[w]=0
        vertices_ordenados = ordenar_vertices(distancia)
        for w,dist in vertices_ordenados:
            if w == v: continue
            cent_aux[padre[w]] += 1 + cent_aux[w]
        for w in grafo:
            if w == v: continue
            cent[w] += cent_aux[w]
    return cent

def ORDEN_TOPOLOGICO(grafo):
    grados = {}

    for vertice in grafo:
        grados[vertice] = 0

    for vertice in grafo:

        for adyacente in grafo.obtenerAdyacentes(vertice):
            grados[adyacente] += 1

    resultado = []
    cola = Cola()

    for vertice in grafo:

        if grados[vertice] == 0 : cola.encolar(vertice)

    while not cola.esta_vacia():
        vertice = cola.desencolar()
        resultado.append(vertice)

        for adyacente in grafo.obtenerAdyacentes(vertice):
            grados[adyacente] -= 1

            if grados[adyacente] == 0: cola.encolar(adyacente)

    return None if len(resultado) == 0 else resultado

def PRIM(grafo,origen,cmp_prim):
    visitados = {}
    visitados[origen] = origen
    heap = heap(cmp_prim)

    for adyacente in grafo.obtenerAdyacentes(origen):
        heap.encolar( [origen, adyacente, grafo.obtenerPeso(inicio, adyacente)] )

    arbol = Grafo(False)

    for vertice in grafo: arbol.agregarVertice(vertice)

    while not heap.esta_vacio():
        vertice, adyacente, peso = heap.desencolar(heap)

        if adyacente in visitados: continue

        arbol.agregarArista(vertice, adyacente, grafo.obtenerPeso(vertice, adyacente))
        visitados[adyacente] = adyacente

        for w in grafo.obtenerAdyacentes(adyacente):
            heap.encolar( [adyacente, w, grafo.obtenerPeso(adyacente, w)] )

    return arbol
