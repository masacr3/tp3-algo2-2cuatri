#!/usr/bin/python
from grafos import *
from funciones import *
from biblioteca import *
import csv
import argparse
import sys
from pruebas import *

ciudad = 0
codigo_aeropuerto = 1
latitud = 2
longitud = 3

aeropuerto_i = 0
aeropuerto_j = 1
tiempo_promedio = 2
precio = 3
cant_vuelos_entre_aeropuertos = 4

def main():

    parser = argparse.ArgumentParser(description='Programa Flycombi')
    parser.add_argument('aeropuertos',metavar='archivo_aeropuertos',help='Archivo csv con datos de aeropuertos a procesar')
    parser.add_argument('vuelos',metavar='archivo_vuelos',help='Archivo csv con datos de vuelos a procesar')
    args = parser.parse_args()

    nombre_arch_aeropuertos = args.aeropuertos
    nombre_arch_vuelos = args.vuelos

    grafo = Grafo()

    with open(nombre_arch_aeropuertos) as csv_file:
        datos_aeropuertos = csv.reader(csv_file,delimiter=',')
        for registro in datos_aeropuertos:
            grafo.agregarVertice(registro[codigo_aeropuerto],"".join(registro))

    with open(nombre_arch_vuelos) as csv_file:
        datos_vuelos = csv.reader(csv_file,delimiter=',')
        for registro in datos_vuelos:
            if grafo.agregarArista(registro[aeropuerto_i],registro[aeropuerto_j],registro): continue
            print("No agrego arista "+registro[aeropuerto_i]+"-"+registro[aeropuerto_j])

    try:
        linea_comando = input()
    except EOFError:
    	print("No hay comandos de entrada")

    while(linea_comando):
        comando_parametros = linea_comando.split(" ")
        print(comando_parametros[0])
        if not ejecutar_operacion(comando_parametros,grafo):
            print("Ups")
        else:
            print("Ok")

        try:
            linea_comando = input()
        except EOFError:
            break






main()
