from grafos import *
from biblioteca import *
from f_comparacion import *
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
	if len(l_comando) != 2: return False

	return True

def f_pagerank(l_comando,grafo):
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
    if comando == pagerank: return f_pagerank(parametros,grafo)
    if comando == nueva_aerolinea: return f_nueva_aerolinea(parametros,grafo)
    if comando == recorrer_mundo: return f_recorrer_mundo(parametros,grafo)
    if comando == recorrer_mundo_aprox: return f_recorrer_mundo_aprox(parametros,grafo)
    if comando == vacaciones: return f_vacaciones(parametros,grafo,dic_aeropuertos) #ya esta
    if comando == itinerario: return f_itinerario(parametros,grafo,dic_aeropuertos) #ya esta
    if comando == exportar_kml: return f_exportar_kml(parametros,grafo) #ya esta ponele

    return False
