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

def mostrarCamino(camino):
	for aeropuerto in range(len(camino)-1):
		print("{} -> ".format(camino[aeropuerto]), end = "")
	print(camino[-1])

def f_camino_mas(parametros,grafo,dic_ciudades):

    if len(parametros) != 3: return False

    modo = parametros[0]

    if modo not in ["barato","rapido"]: return False

    origen = parametros[1]
    destino = parametros[2]

    camino = _camino_mas(origen,destino,grafo,f_cmp_heap,0 if modo == "rapido" else 1,dic_ciudades)
    mostrarCamino(camino)

    return True

def f_camino_escalas(l_comando,grafo):
	if len(l_comando) != 2: return False
	parametros = l_comando[pos_parametros].split(',')
	if len(parametros) != 2: return False
	origen = 0
	destino = 1

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
def f_vacaciones(l_comando,grafo):
	return true
def f_itinerario(l_comando,grafo):
	return true
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


def ejecutar_operacion(comando,parametros,grafo,dic_ciudades):
    if not comando: return False
    if comando == listar_operaciones: return f_listar_operaciones()
    if comando == camino_mas: return f_camino_mas(parametros,grafo,dic_ciudades)
    if comando == camino_escalas: return f_camino_escalas(parametros,grafo)
    if comando == centralidad: return f_centralidad(parametros,grafo)
    if comando == pagerank: return f_pagerank(parametros,grafo)
    if comando == nueva_aerolinea: return f_nueva_aerolinea(parametros,grafo)
    if comando == recorrer_mundo: return f_recorrer_mundo(parametros,grafo)
    if comando == recorrer_mundo_aprox: return f_recorrer_mundo_aprox(parametros,grafo)
    if comando == vacaciones: return f_vacaciones(parametros,grafo)
    if comando == itinerario: return f_itinerario(parametros,grafo)
    if comando == exportar_kml: return f_exportar_kml(parametros,grafo)

    return False
