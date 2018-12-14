#!/usr/bin/python
from grafos import *
from funciones import * 
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

    with open(nombre_arch_aeropuertos) as csv_file:
        datos_aeropuertos = csv.reader(csv_file,delimiter=',')
        for registro in datos_aeropuertos:
            grafo.agregarVertice(registro[codigo_aeropuerto],registro)

    with open(nombre_arch_vuelos) as csv_file:
        datos_vuelos = csv.reader(csv_file,delimiter=',')
        for registro in datos_vuelos:
            if grafo.verticePertenece(registro[aeropuerto_i]) and grafo.verticePertenece(registro[aeropuerto_j]):
                grafo.agregarArista(aeropuerto_i,aeropuerto_j,registro)
    try:
        linea_comando = input()
    except EOFError: 
    	print("No hay comandos de entrada")

    while(linea_comando):
    	comando_parametros = linea_comando.split(" ")
        if not ejecutar_operacion(comando_parametros,grafo): print("Ups")
        else: print("Ok")
        try:
            linea_comando = input()
        except EOFError:
        	break






main()