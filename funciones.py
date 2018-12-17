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

pos_comando = 0
pos_parametros = 1

ciudad = 0
codigo_aeropuerto = 1
latitud = 2
longitud = 3

aeropuerto_i = 0
aeropuerto_j = 1
tiempo_promedio = 2
precio = 3
cant_vuelos_entre_aeropuertos = 4

def cargar_flycombi(grafo,aeropuertos,vuelos,dic_ciudades):
    with open(aeropuertos) as csv_file:
        datos_aeropuertos = csv.reader(csv_file,delimiter=',')
        for registro in datos_aeropuertos:
            grafo.agregarVertice(registro[codigo_aeropuerto],registro)
            if not registro[ciudad] in dic_ciudades:
            	dic_ciudades[registro[ciudad]] = []
            dic_ciudades[registro[ciudad]].append(registro[codigo_aeropuerto])

    with open(vuelos) as csv_file:
        datos_vuelos = csv.reader(csv_file,delimiter=',')
        for registro in datos_vuelos:
            grafo.agregarArista(registro[aeropuerto_i],registro[aeropuerto_j],registro)


def _camino_mas(origen,destino,grafo,f_cmp,dic_ciudades):
	for aeropuerto in dic_ciudades[origen]:
		padre, rapidezVuelo = DIJKSTRA(grafo,origen,f_cmp)

	caminoMasRapido = []
	while destino != None:
		caminoMasRapido.append(destino)
		destino = padre[destino]

	caminoMasRapido.reverse()
	return caminoMasRapido

def mostrarCamino(camino):
	for aeropuerto in range(len(camino)-1):
		print("{} -> ".format(camino[aeropuerto]), end = " ")
	print(camino[-1])

def f_camino_mas(parametros,grafo,dic_ciudades):
	print(len(parametros))
	if len(parametros) != 3: return False
	modo = 0
	origen = 1
	destino = 2
	print(parametros[modo])
	if parametros[modo] == "barato":
		camino = _camino_mas(parametros[origen],parametros[destino],grafo,f_cmp_precio,dic_ciudades)
		mostrarCamino(camino)
		return True
	if parametros[modo] == "rapido":
		camino = _camino_mas(parametros[origen],parametros[destino],grafo,f_cmp_tiempo,dic_ciudades)
		mostrarCamino(camino)
		return True
	return False

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
    print(camino_mas)
    print(comando)
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
