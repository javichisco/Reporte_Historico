#!/usr/bin/env python
# coding: utf-8
# Autor: Francisco Rodriguez | Mty., N. L., Mx. ! 2024

import csv
import os

def leerConfiguraciones(archivo):
    with open(archivo) as csvArchivo:
        lectura = csv.reader(csvArchivo, delimiter=',')
        columna1=[]
        columna2=[]
        for row in lectura:
            columna1.append(row[0])
            columna2.append(row[1])
        return columna1, columna2
    
def guardarConfiguraciones(headers, contenido, archivo):
    with open(archivo, mode='w', newline='') as csvArchivo:
        writer = csv.writer(csvArchivo)
        writer.writerow(headers)
        for linea in contenido:
            writer.writerow(linea)
            