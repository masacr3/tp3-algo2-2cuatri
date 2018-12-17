from grafos import *
from funciones import *

def pruebas_grafo(grafo):

	vertices = ["JFK","LAN","SHE","ATL","RIV","WAC","NAR","BAT","ASH","BH6"]
	for vertice in vertices:
		if grafo.verticePertenece(vertice):
			print(vertice)
			print(grafo.obtenerDatos(vertice))
			continue
		print("No se encontro "+vertice)
	#Prueba aristas correctas.
	adyacentes = grafo.obtenerAdyacentes('JFK')
	adyacentes_esperados = ['BH6','ATL','LAN']
	adyacentes_obtenidos = []
	print(adyacentes)
	for clave in adyacentes:
		if clave in adyacentes_esperados:
			print("Peso arista "+'JFK - '+clave)
			print(grafo.obtenerPeso('JFK',clave))
			adyacentes_obtenidos.append(clave)
			continue
		print("Adyacente no esperado.")
	print("Adyacentes JFK: ", adyacentes_esperados)
	print("Adyacentes obtenidos: ", adyacentes_obtenidos)

def pruebas_dic_aeropuertos(ciudades):
	for ciudad in cuidades:
		for aeropuerto in cuidad:

			print(ciudad,aeropuerto,cuidades[ciudad][aeropuerto])

def pruebas_cmp(grafo):
	peso1 = grafo.obtenerPeso("SHE","RIV")
	peso2 = grafo.obtenerPeso("ATL","RIV")
	if f_cmp_tiempo(peso1,peso2) < 0: print("peso1 menor a peso2")
	if f_cmp_precio(peso1,peso2) < 0: print("precio1 menor a precio2")
	if f_cmp_escalas(peso1,peso2) > 0: print("escala1 mayor a escala2")
