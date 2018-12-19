#!/usr/bin/python
from grafo import *
from funciones import *
from biblioteca import *
import csv
import argparse
import sys

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
    dic_aeropuertos = {} #Cada clave es una ciudad, con sus respectivos aeropuertos

    cargar_flycombi(grafo,nombre_arch_aeropuertos,nombre_arch_vuelos,dic_aeropuertos)

    try:
        linea_comando = input()
    except EOFError:
    	print("No hay comandos de entrada")

    while(linea_comando):

        comando = linea_comando.rstrip().split(" ")[0]

        ejecutar_operacion(comando,linea_comando,grafo,dic_aeropuertos)

        try:
            linea_comando = input()
        except EOFError:
            break


main()
