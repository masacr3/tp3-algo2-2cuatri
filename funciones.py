from grafos import *
from biblioteca import *
from f_comparacion import *
from random_walks import *
import random
import sys
import csv

camino_mas = "camino_mas"
camino_escalas = "camino_escalas"
centralidad = "centralidad"
centralidad_aprox = "centralidad_aprox"
pagerank = "pagerank"
nueva_aerolinea = "nueva_aerolinea"
recorrer_mundo = "recorrer mundo"
recorrer_mundo_aprox = "recorrer_mundo_aprox"
vacaciones = "vacaciones"
itinerario = "itinerario"
exportar_kml = "exportar_kml"
listar_operaciones = "listar_operaciones"

L_rwalk = 50
K_rwalk = 150

def cargar_flycombi(grafo,aeropuertos,vuelos,h):
    with open(aeropuertos) as lista_aeropuertos:
        for aeropuerto in lista_aeropuertos:
            ciudad,cod,latitud,longitud = aeropuerto.rstrip('\n').rstrip('\r').split(",")

            if ciudad not in h:
                h[ciudad] = {}

            h[ciudad][cod] = [float(latitud), float(longitud)]

    with open(vuelos) as lista_vuelos:
        for vuelo in lista_vuelos:
            cod_aeropuerto_i,cod_aeropuerto_j, t_promedio, precio, cant_vuelos = vuelo.rstrip('\n').split(",")
            if cod_aeropuerto_i not in grafo:
                grafo.agregarVertice(cod_aeropuerto_i)

            if cod_aeropuerto_j not in grafo:
                grafo.agregarVertice(cod_aeropuerto_j)

            grafo.agregarArista(cod_aeropuerto_i, cod_aeropuerto_j, [int(t_promedio), int(precio), int(cant_vuelos)])


def _camino_mas(origen,destino,grafo,f_cmp,peso,dic_aeropuertos):
    caminos = []
    distancia_actual = INFINITO

    padreActual = {}
    destinoActual = None

    for aeropuerto_partida in dic_aeropuertos[origen]:
        padre, distancia = DIJKSTRA(grafo , aeropuerto_partida, f_cmp, peso)
        if padre != None:
            caminos.append([padre,distancia])

    for aeropuerto_destino in dic_aeropuertos[destino]:

        for padre,distancia in caminos:

            if distancia[aeropuerto_destino] < distancia_actual:
                padreActual = padre
                destinoActual = aeropuerto_destino
                distancia_actual = distancia[aeropuerto_destino]
                
    caminoMas = []
    actual = destinoActual

    while actual != None:
        caminoMas.append(actual)
        actual = padreActual[actual]

    caminoMas.reverse()

    return caminoMas

def f_camino_mas(parametros,grafo,dic_ciudades):
    opciones = parametros[11:].split(",")
    modo = opciones[0]

    if modo not in ["barato","rapido"]: return False

    origen = opciones[1]
    destino = opciones[2]

    camino = _camino_mas(origen,destino,grafo,f_cmp_heap,0 if modo == "rapido" else 1,dic_ciudades)
    mostrarCamino(camino)

    return True


def _camino_escalas(origen,destino,grafo,f_cmp,index,dic_aeropuertos):
    caminos = []
    orden_actual = INFINITO
    padreActual = {}
    destinoActual = None
    for aeropuerto_partida in dic_aeropuertos[origen]:
        padre, orden = BFS(grafo , aeropuerto_partida)
        if padre != None:
            caminos.append([padre,orden])

    for aeropuerto_destino in dic_aeropuertos[destino]:
        for padre,orden in caminos:
            if orden[aeropuerto_destino] < orden_actual:
                padreActual = padre
                destinoActual = aeropuerto_destino
                orden_actual = orden[aeropuerto_destino]

    actual = destinoActual
    camino = []

    while actual != None:
        camino.append(actual)
        actual = padre[actual]

    camino.reverse()

    return camino

def f_camino_escalas(parametros,grafo,dic_ciudades):

    opciones = parametros[15:].split(",")

    origen = opciones[0]
    destino = opciones[1]
    camino = _camino_escalas(origen,destino,grafo,f_cmp_heap,2,dic_ciudades)
    mostrarCamino(camino)

    return True

def f_centralidad(l_comando,grafo):
    parametros = l_comando[12:].split(",")
    if(len(parametros)) != 1: return False
    n = int(parametros[0])
    cent = obtener_centralidad(grafo,f_cmp_heap,2)
    cent_ordenados = ordenar_vertices(cent)
    for i in range(n-1):
        print("{}, ".format(cent_ordenados[i][0]), end = "")
        print(cent_ordenados[i][1])
    print("{}, {}".format(cent_ordenados[n-1][0],cent_ordenados[n-1][1]))
    return True

def f_centralidad_aprox(l_comando,grafo):
    parametros = l_comando[18:].split(",")
    if(len(parametros)) != 1: return False
    n = int(parametros[0])
    cent = {}
    for v in grafo:
        cent[v]=0

    for i in range(K_rwalk):
        recorrido = Random_walk(grafo,L_rwalk)
        for v in recorrido:
            cent[v] += 1

    cent_ordenados = ordenar_vertices(cent)
    for i in range(n-1):
        print("{}, ".format(cent_ordenados[i][0]),end = "")
    print("{}".format(cent_ordenados[n-1][0]))

    return True


def _pagerank(grafo,d,me):
    pageRanks = {}
    pageRanks_aux = {}
    n = grafo.obtenerCantidad()
    rp = (1-d)/n
    for v in grafo:
        pageRanks_aux[v] = 1/n
    convergencia = True
    while convergencia:
        pageRanks = pageRanks.fromkeys(pageRanks_aux,0)
        for v in grafo:
            for w in grafo.obtenerAdyacentes(v):
                salida = len(grafo.obtenerAdyacentes(w))
                if salida == 0: continue
                else:
                    MPi = pageRanks_aux[w]/salida
                    pageRanks[v] += MPi
        convergencia = False
        for v in grafo:
            pageRanks[v] = rp + d*pageRanks[v]
            v_converg = abs(pageRanks[v]-pageRanks_aux[v])
            if v_converg > me:
                convergencia = True
            pageRanks_aux[v] = pageRanks[v]

    return pageRanks

def f_pagerank(l_comando,grafo):
    parametros = l_comando[9:].split(",")
    if(len(parametros)) != 1: return False
    n = int(parametros[0])

    p_rank = _pagerank(grafo,0.85,0.05)

    suma = 0
    for rank in p_rank:
        suma += p_rank[rank]

    ranking = ordenar_vertices(p_rank)

    for i in range(n-1):
        print("{}, ".format(ranking[i][0]), end = "")
    print("{}".format(ranking[n-1][0]))

    return True

def f_nueva_aerolinea(l_comando,grafo):
	return True
def f_recorrer_mundo(l_comando,grafo):
	return true
def f_recorrer_mundo_aprox(l_comando,grafo):
	return true

def _viaje_lugares(origen,n,grafo,dic_aeropuertos):
    largo = int(n)
    l = []
    for aeropuerto_origen in dic_aeropuertos[origen]:
        visitados = {}
        l = []
        if DFS(grafo,aeropuerto_origen,visitados,l,largo,1):
            return l
    return l

def f_vacaciones(parametros,grafo,dic_aeropuertos):
    opcion = parametros[11:].split(",")
    origen = opcion[0]
    n = opcion[1]
    camino = _viaje_lugares(origen,n,grafo,dic_aeropuertos)
    mostrarCamino(camino)
    return True

def cargarGrafo(grafo,archivo):

    with open (archivo) as recorrido:
        ciudades = recorrido.readline().rstrip().split(",")

        for ciudad in ciudades:
            grafo.agregarVertice(ciudad)

        for condicion in recorrido:
            ciudad_i, ciudad_j = condicion.rstrip().split(",")
            grafo.agregarArista(ciudad_i,ciudad_j)


def f_itinerario(l_comando,grafo,dic_aeropuertos):
    grafoCiudades = Grafo(True)
    cargarGrafo(grafoCiudades,"itinerario_ejemplo.csv")
    itinerario = ORDEN_TOPOLOGICO(grafoCiudades)
    print(" ,".join(itinerario))
    TIEMPO = 0 #tiempo
    for ciudad in range(len(itinerario)-1):
        origen = itinerario[ciudad]
        destino = itinerario[ciudad + 1]
        l = _camino_mas(origen,destino,grafo,f_cmp_heap,TIEMPO,dic_aeropuertos)
        mostrarCamino(l)
    return True

def f_exportar_kml(l_comando,grafo):
	return true


def f_listar_operaciones():
    print (camino_mas)
    print (camino_escalas)
    print (centralidad)
    print (centralidad_aprox)
    print (pagerank)
    print (nueva_aerolinea)
    print (recorrer_mundo)
    print (recorrer_mundo_aprox)
    print (vacaciones)
    print (itinerario)
    print (exportar_kml)
    return True


def ejecutar_operacion(comando,parametros,grafo,dic_aeropuertos):
    if not comando: return False
    if comando == listar_operaciones: return f_listar_operaciones() #ya esta
    if comando == camino_mas: return f_camino_mas(parametros,grafo,dic_aeropuertos) #ya esta
    if comando == camino_escalas: return f_camino_escalas(parametros,grafo,dic_aeropuertos) #ya esta
    if comando == centralidad: return f_centralidad(parametros,grafo) 
    if comando == centralidad_aprox: return f_centralidad_aprox(parametros,grafo) #ya esta
    if comando == pagerank: return f_pagerank(parametros,grafo) #ya esta
    if comando == nueva_aerolinea: return f_nueva_aerolinea(parametros,grafo)
    if comando == recorrer_mundo: return f_recorrer_mundo(parametros,grafo)
    if comando == recorrer_mundo_aprox: return f_recorrer_mundo_aprox(parametros,grafo)
    if comando == vacaciones: return f_vacaciones(parametros,grafo,dic_aeropuertos) #ya esta
    if comando == itinerario: return f_itinerario(parametros,grafo,dic_aeropuertos) #ya esta
    if comando == exportar_kml: return f_exportar_kml(parametros,grafo) #ya esta ponele

    return False
