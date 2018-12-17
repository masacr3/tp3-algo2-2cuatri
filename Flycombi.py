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
    dic_ciudades = {} #Cada clave es una ciudad, con sus respectivos aeropuertos

    cargar_flycombi(grafo,nombre_arch_aeropuertos,nombre_arch_vuelos,dic_ciudades)
    pruebas_dic_ciudades(dic_ciudades)

    try:
        linea_comando = input()
    except EOFError:
    	print("No hay comandos de entrada")

    while(linea_comando):
        comando_parametros = linea_comando.split(",")
        comando = comando_parametros[0].split(" ")
        if(len(comando)==2): comando_parametros[0] = comando[1]
        print(comando[0])
        print(comando_parametros)
        if not ejecutar_operacion(comando[0],comando_parametros,grafo):
            print("Ups")
        else:
            print("Ok")

        try:
            linea_comando = input()
        except EOFError:
            break






main()
