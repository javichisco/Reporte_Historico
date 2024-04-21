#!/usr/bin/env python
# coding: utf-8
# Autor: Francisco Rodriguez | Mty., N. L., Mx. ! 2024

# Importacion de librerias
import os
import pandas as pd
import numpy as np
import xlsxwriter


def leerArchivos(parametrosGenerales):
    
    archivos = parametrosGenerales["archivos"] 
    tab = parametrosGenerales["tab"] 
    filas = parametrosGenerales["filas"] 
    auto = parametrosGenerales["auto"] 
    caracteristica = parametrosGenerales["caracteristica"] 
    proveedor = parametrosGenerales["proveedor"] 
    numero_parte = parametrosGenerales["numero_parte"]
    min_spec = parametrosGenerales["min_spec"]
    max_spec = parametrosGenerales["max_spec"]
    decimales = parametrosGenerales["decimales"]
    
    columna = parametrosGenerales["columna"]
    colProveedor = parametrosGenerales["colProveedor"]
    colNumero = parametrosGenerales["colNumero"]
    colCaracteristica = parametrosGenerales["colCaracteristica"]
    colEspecificaciones = parametrosGenerales["colEspecificaciones"] 
    fila = parametrosGenerales["fila"]
    filaProveedor = parametrosGenerales["filaProveedor"]
    filaNumero = parametrosGenerales["filaNumero"]
    filaCaracteristica = parametrosGenerales["filaCaracteristica"]
    filaEspecificaciones = parametrosGenerales["filaEspecificaciones"]
    
    caract_auto = pd.DataFrame
    proveedor_auto = pd.DataFrame
    np_auto = pd.DataFrame
    spec_auto = pd.DataFrame
    valores = pd.DataFrame
    valores_cadena = pd.DataFrame()
    extractor=[]
    lote=[]
    c=1
    muestra=[]
    
    for i in range (len(archivos)):
        lectura = archivos[i].name
        extractor=lectura.split("\\")
        extractor=lectura.split("/")
        
        for a in range (len(extractor)):
            
            if a == (len(extractor))-1:
                extractor[a]=extractor[a].replace(".xlsx","")
                
                for b in range (filas):
                    lote.append(extractor[(len(extractor))-1])
                    muestra.append(c)
                    c=c+1
        
        valores = pd.read_excel(lectura, sheet_name = tab, header = None, usecols = columna, skiprows = (fila-1), nrows = filas)
        valores_cadena = pd.concat([valores_cadena, valores], axis = 0, ignore_index = False)

    if auto == "Y": 
        caract_auto = pd.read_excel(lectura, sheet_name = tab, header = None, usecols = colCaracteristica, skiprows = (filaCaracteristica-1), nrows = 1)
        proveedor_auto = pd.read_excel(lectura, sheet_name = tab, header = None, usecols = colProveedor, skiprows = (filaProveedor-1), nrows = 1)
        np_auto = pd.read_excel(lectura, sheet_name = tab, header = None, usecols = colNumero, skiprows = (filaNumero-1), nrows = 1)
        spec_auto = pd.read_excel(lectura, sheet_name = tab, header = None, usecols = colEspecificaciones, skiprows = (filaEspecificaciones-1), nrows = 1)
    
        caract_auto = caract_auto.rename(columns={caract_auto.columns.values[0]: "caracteristica"})
        proveedor_auto = proveedor_auto.rename(columns={proveedor_auto.columns.values[0]: "proveedor"})
        np_auto = np_auto.rename(columns={np_auto.columns.values[0]: "numero_parte"})
        spec_auto = spec_auto.rename(columns={spec_auto.columns.values[0]: "especificacion"})
    
        caracteristica = list(caract_auto["caracteristica"])
        proveedor = list(proveedor_auto["proveedor"])
        numero_parte = list(np_auto["numero_parte"])
        spec_temp = list(spec_auto["especificacion"])
    
        caracteristica = caracteristica[0]
        proveedor = proveedor[0]
        numero_parte = numero_parte[0]
        spec_temp = spec_temp[0]
        spec_temp = spec_temp.replace(" ","")
        spec_temp = spec_temp.split("-")
        min_spec = float(spec_temp[0])
        max_spec = float(spec_temp[1])
    else:
        caracteristica = caracteristica
        proveedor = proveedor
        numero_parte = numero_parte
        min_spec = min_spec
        max_spec = max_spec
        
    
    valores_cadena = valores_cadena.rename(columns={valores_cadena.columns.values[0]: caracteristica})
    valores_cadena["Grupo"]=lote
    valores_cadena["Muestra"]=muestra
    valores_cadena = valores_cadena.reindex(["Muestra", caracteristica, "Grupo"], axis=1)

    return valores_cadena, caracteristica, numero_parte, proveedor, max_spec, min_spec
    

def definir_escala(valores_cadena, parametrosGenerales):
    
    max_spec = parametrosGenerales["max_spec"]
    min_spec = parametrosGenerales["min_spec"]
    caracteristica = parametrosGenerales["caracteristica"]
    decimales = parametrosGenerales["decimales"]

    eje_x = list(valores_cadena["Muestra"])
    eje_y = list(valores_cadena[caracteristica])
    grupo = list(valores_cadena["Grupo"])
    temp = "temp"
    promedio = []
    indice = 0
    contador = 0
    lotes = []
    valores = []
    maximos = []
    minimos = []
    rangos = []
    
    for a in grupo:
        if indice == 0:
            temp = grupo[indice]
            suma = eje_y[indice]
            valores.append(eje_y[indice])
            
        elif temp != grupo[indice] and indice < (len(grupo)-1):
            temp = grupo[indice]
            contador = contador + 1
            prom = suma/contador
            promedio.append(round(prom, decimales))
            valores.append(eje_y[indice])
            maximos.append(round(max(valores), decimales))
            minimos.append(round(min(valores), decimales))
            rangos.append(round(max(valores)-min(valores), decimales))
            lotes.append(grupo[indice-1])
            suma = eje_y[indice]
            contador = 0 
            valores = [eje_y[indice]]
            
        elif contador == 3 and indice == (len(grupo)-1):
            temp = grupo[indice]
            contador = contador + 1
            prom = suma/contador
            promedio.append(prom)
            valores.append(eje_y[indice])
            maximos.append(round(max(valores), decimales))
            minimos.append(round(min(valores), decimales))
            rangos.append(round(max(valores)-min(valores), decimales))
            lotes.append(grupo[indice-1])
            suma = eje_y[indice]
            contador = 0 
            valores = [eje_y[indice]]
            
        else:
            temp = grupo[indice]
            suma = eje_y[indice] + suma
            valores.append(eje_y[indice])
            contador = contador + 1 
       
        indice = indice + 1
    
    sum_num = 0
    for t in promedio:
        sum_num = sum_num + t           
        prom_promedio = sum_num / len(promedio)
    
    min_x = min(eje_x)
    max_x = max(eje_x)
    min_y = min(eje_y)
    max_y = max(eje_y)
    range = max_spec - min_spec
    nominal = min_spec+(range/2)
    
    if min_y > nominal-((range/2)*1.1): min_y = nominal-((range/2)*1.1)
    if max_y < nominal+((range/2)*1.1): max_y = nominal+((range/2)*1.1)
    
    r1 = nominal - min_y
    r2 = max_y - nominal
    
    if r1 >= r2: 
        max_y = nominal + r1
    else:
        min_y = nominal - r2
    
    parametrosGraficas = {
            "max_x": max_x,
            "min_x": min_x,
            "max_y": max_y,
            "min_y": min_y,
            "range": range,
            "nominal": nominal,
            "promedio": promedio,
            "valores": valores,
            "maximos": maximos,
            "minimos": minimos, 
            "rangos": rangos,
            "lotes": lotes,
            "prom_promedio": prom_promedio, 
            "eje_x": eje_x, 
            "eje_y": eje_y
        }
        
    return parametrosGraficas