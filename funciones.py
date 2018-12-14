from grafos import *

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


def camino_mas_barato(origen,destino,grafo):
	padre, costoVuelo = DIJKSTRA(grafo,origen,cmp_costos)

	caminoMasBarato = []
	while destino != None:
		caminoMasBarato.append(destino)
		destino = padre[destino]

	caminoMasBarato.reverse()
	return caminoMasBarato

def camino_mas_rapido(origen,destino,grafo):
	padre, costoVuelo = DIJKSTRA(grafo,origen,cmp_rapidez)

	caminoMasBarato = []
	while destino != None:
		caminoMasBarato.append(destino)
		destino = padre[destino]

	caminoMasBarato.reverse()
	return caminoMasBarato

def f_camino_mas(l_comando,grafo):
	if len(l_comando) != 2: return False
	parametros = l_comando[pos_parametros].split(',')
	if len(parametros) != 3: return False
	modo = 0
	origen = 1
	destino = 2
	if parametros[modo] == "barato":  return camino_mas_barato(parametros[origen],parametros[destino],grafo)
	if pos_parametros[modo] == "rapido": return camino_mas_rapido(parametros[origen],pos_parametros[destino],grafo)
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


def ejecutar_operacion(l_comando,grafo):
    if not l_comando: return False
    comando = l_comando[0]
    if comando == listar_operaciones: return f_listar_operaciones()
    if comando == camino_mas: return f_camino_mas(l_comando,grafo)
    if comando == camino_escalas: return f_camino_escalas(l_comando,grafo)
    if comando == centralidad: return f_centralidad(l_comando,grafo)
    if comando == pagerank: return f_pagerank(l_comando,grafo)
    if comando == nueva_aerolinea: return f_nueva_aerolinea(l_comando,grafo)
    if comando == recorrer_mundo: return f_recorrer_mundo(l_comando,grafo)
    if comando == recorrer_mundo_aprox: return f_recorrer_mundo_aprox(l_comando,grafo)
    if comando == vacaciones: return f_vacaciones(l_comando,grafo)
    if comando == itinerario: return f_itinerario(l_comando,grafo)
    if comando == exportar_kml: return f_exportar_kml(l_comando,grafo)

    return False
