from grafos import *

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
	



