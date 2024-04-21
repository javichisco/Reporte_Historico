#!/usr/bin/env python
# coding: utf-8
# Autor: Francisco Rodriguez QC-KSM-2024

# Importacion de librerias
import os
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as mticker
import statistics as stat


def graficaPromedios(parametrosGraficas, parametrosGenerales):
    
    nominal = parametrosGraficas["nominal"]
    max_x = parametrosGraficas["max_x"]
    min_x = parametrosGraficas["min_x"]
    max_y = parametrosGraficas["max_y"]
    min_y = parametrosGraficas["min_y"]
    promedio = parametrosGraficas["promedio"]
    eje_x = parametrosGraficas["eje_x"]
    eje_y = parametrosGraficas["eje_y"]
    prom_promedio = parametrosGraficas["prom_promedio"]
    lotes = parametrosGraficas["lotes"]
    
    auto2 = str(parametrosGenerales["auto2"])
    folder_salida = str(parametrosGenerales["folder_salida"])
    numero_parte = str(parametrosGenerales["numero_parte"])
    caracteristica = str(parametrosGenerales["caracteristica"])
    fecha = str(parametrosGenerales["fecha"])
    filas = int(parametrosGenerales["filas"])
    sigma3 = str(parametrosGenerales["sigma3"])
    max_spec = float(parametrosGenerales["max_spec"])
    min_spec = float(parametrosGenerales["min_spec"])
    sigma3 = str(parametrosGenerales["sigma3"])
    
    #Crea carpeta de graficas
    if auto2 == "Y":
        try:
            os.mkdir(folder_salida + "/Graficas")
        except OSError as error:
            pass
    
    fig, ax = plt.subplots(layout = 'constrained')
    ax.set_title("GRAFICA DE PROMEDIOS | " + numero_parte + " | " + caracteristica)
    ax.set_ylabel("Valor Dimensional")
    ax.set_xlabel("Valores Individuales")
    ax.spines["bottom"].set_position(("axes", -0.0))
    ax.spines["bottom"].set_visible(True)
    ax.xaxis.set_label_position('bottom')
    ax.xaxis.set_ticks_position('bottom')
    
    nom_ = [nominal, nominal]
    x_ = [min_x, max_x]
    prom_ = [prom_promedio, prom_promedio]
    
    y_superior = [max_spec, max_spec]
    y_inferior = [min_spec, min_spec]
    
    sigma = np.std(promedio)
    sigma3arriba = prom_promedio + (prom_promedio*(sigma*3))
    sigma3abajo = prom_promedio - (prom_promedio*(sigma*3))
    sigma3_superior = [sigma3arriba, sigma3arriba]
    sigma3_inferior = [sigma3abajo, sigma3abajo]
    
    ax.plot(x_, y_superior, color = 'red')
    ax.plot(x_, y_inferior, color = 'red')
    if sigma3 == "Y":
        ax.plot(x_, sigma3_superior, color = 'black', linestyle=':')
        ax.plot(x_, sigma3_inferior, color = 'black', linestyle=':')
    ax.plot(x_, nom_, color = 'black')
    ax.plot(x_, prom_, color = 'blue', linestyle='--', alpha=.8)
    ax.set_xlim((min_x-1,max_x+1))
    ax.set_ylim((min_y,max_y))
    ax.grid(axis = "both", visible = "True")
    
    ax.plot(eje_x, eje_y, marker= "o", color = 'gray', alpha=0.5, linestyle='None')
    
    ax.xaxis.set_major_locator(mticker.MultipleLocator(base=filas, offset=0.0))
    ax.xaxis.set_minor_locator(mticker.MultipleLocator(base=1, offset=0.0))
    
    secax = ax.twiny()
    secax.set_xlabel("Sub-Grupos")
    secax.spines["bottom"].set_position(("axes", -0.2))
    secax.spines["bottom"].set_visible(True)
    secax.xaxis.set_label_position('bottom')
    secax.xaxis.set_ticks_position('bottom')
    secax.tick_params(axis='x', labelrotation=45)
    secax.plot(lotes, promedio, marker= "o", color = 'blue', alpha=1, linestyle = "-")
    
    #Creacion de la grafica
    fecha2 = fecha.replace("/", "-")
    if auto2 == "Y":
        plt.savefig(folder_salida + "/Graficas/" + numero_parte + "_" + fecha2 + "_Dispersion.png")
    plt.show()
    
    
def graficaCampana(parametrosGraficas, parametrosGenerales):
    
    nominal = parametrosGraficas["nominal"]
    prom_promedio = parametrosGraficas["prom_promedio"]
    promedio = parametrosGraficas["promedio"] 
    eje_y = parametrosGraficas["eje_y"]
    
    num_bins = int(parametrosGenerales["categorias"])
    max_spec = float(parametrosGenerales["max_spec"])
    min_spec = float(parametrosGenerales["min_spec"])
    auto2 = str(parametrosGenerales["auto2"])
    folder_salida = str(parametrosGenerales["folder_salida"])
    numero_parte = str(parametrosGenerales["numero_parte"])
    fecha = str(parametrosGenerales["fecha"])
    caracteristica = str(parametrosGenerales["caracteristica"])
    sigma3 = str(parametrosGenerales["sigma3"])
    
    mu = prom_promedio
    y_superior = [max_spec, max_spec]
    y_inferior = [min_spec, min_spec]
    sigma = np.std(promedio)
    nom_ = [nominal, nominal]
    
    sigma3arriba = prom_promedio + (prom_promedio*(sigma*3))
    sigma3abajo = prom_promedio - (prom_promedio*(sigma*3))
    sigma3_superior = [sigma3arriba, sigma3arriba]
    sigma3_inferior = [sigma3abajo, sigma3abajo]
    
    fig, ax = plt.subplots()
    
    # Datos del histograma
    n, bins, patches = ax.hist(eje_y, num_bins, density=True)
    
    n_max = [0, int(max(n) * 1.05)]
    
    # Linea para la campana
    fy = ((1 / (np.sqrt(2 * np.pi) * sigma)) *
         np.exp(-0.5 * (1 / sigma * (bins - mu))**2))
    
    ax.plot(bins, fy, '-')
    ax.plot(y_superior, n_max, color = 'red', linestyle="-")
    ax.plot(y_inferior, n_max, color = 'red', linestyle="-")
    if sigma3 == "Y":
        ax.plot(sigma3_superior, n_max, color = 'black', linestyle=':')
        ax.plot(sigma3_inferior, n_max, color = 'black', linestyle=':')
    ax.plot(nom_, n_max, color = 'black', linestyle="-")
    ax.set_xlabel('Valor Dimensional')
    ax.set_ylabel('Densidad de Probabilidad')
    ax.set_title("DISTRIBUCION NORMAL | " + numero_parte + " | " + caracteristica)
    
    # Ajuste de resolucion en eje Y
    fig.tight_layout()
    
    #Creacion de la grafica
    fecha2 = fecha.replace("/", "-")
    if auto2 == "Y":
        plt.savefig(folder_salida + "/Graficas/" + numero_parte + "_" + fecha2 + "_Distribucion.png")
    plt.show()
    
    return sigma, fecha2