#!/usr/bin/env python
# coding: utf-8
# Autor: Francisco Rodriguez | Mty., N. L., Mx. ! 2024

# Importacion de librerias
import os
import pandas as pd
import numpy as np
import xlsxwriter

   
def dibujarTablas(informacion, informacion2, fecha2, parametrosGenerales, valores_cadena):
    
    proveedor = str(parametrosGenerales["proveedor"])
    numero_parte = str(parametrosGenerales["numero_parte"])
    max_spec = float(parametrosGenerales["max_spec"])
    min_spec = float(parametrosGenerales["min_spec"])
    unidades = str(parametrosGenerales["proveedor"])
    responsable = str(parametrosGenerales["unidades"])
    caracteristica = str(parametrosGenerales["caracteristica"])
    folder_salida = str(parametrosGenerales["folder_salida"])
    archivo_nombre = str(parametrosGenerales["archivo_nombre"])
    campana_ = str(parametrosGenerales["campana_"])
    rawdata = str(parametrosGenerales["rawdata"])
    
    
    archivo = folder_salida + "/" + archivo_nombre + ".xlsx"
    workbook = xlsxwriter.Workbook(archivo)
    worksheet = workbook.add_worksheet("Reporte")
    
    #Titulo del reporte
    titulo = workbook.add_format(
        {
            "border": 0,
            "align": "center",
            "valign": "vnottom",
            "fg_color": "white",
            "font_name" : "Calibri",
            "font_size" : 24,
            "bold" : 1
        }
    )
    
    #Formato texto del reporte
    texto = workbook.add_format(
        {
            "border": 0,
            "align": "right",
            "valign": "vcenter",
            "font_name" : "Calibri",
            "font_size" : 10,
        }
    )
        
    #Formato texto del reporte
    texto2 = workbook.add_format(
        {
            "bottom": 1,
            "align": "left",
            "valign": "vcenter",
            "font_name" : "Calibri",
            "font_size" : 10,
        }
    )
        
    #Formato texto de lo titulos de las tablas
    tabla = workbook.add_format(
        {
            "border": 1,
            "align": "center",
            "valign": "vcenter",
            "font_name" : "Calibri",
            "font_size" : 10,
            "bold" : 1,
            "bg_color" : "black",
            "font_color" : "white",
        }
    )
        
    #Formato texto de lo subtitulos de las tablas
    tabla2 = workbook.add_format(
        {
            "border": 1,
            "align": "center",
            "valign": "vcenter",
            "font_name" : "Calibri",
            "font_size" : 10,
            "bold" : 1,
            "bg_color" : "gray",
            "font_color" : "white",
        }
    )
        
    #Formato texto del contenido de las tablas
    tabla3 = workbook.add_format(
        {
            "border": 1,
            "align": "center",
            "valign": "vcenter",
            "font_name" : "Calibri",
            "font_size" : 10,
        }
    )
    
    # Cargar de informacion y cierre del archivo
    #-----------------------
    #LOGO
    #-----------------------
    worksheet.insert_image("A1", "logo.png", {"x_scale": 0.32, "y_scale": 0.3})
    
    #TITULO
    #-----------------------
    worksheet.merge_range("A2:O5", "REPORTE DE COMPORTAMIENTO HISTORICO", titulo)
    #-----------------------
        
    #-----------------------
    #ENCABEZADOS
    #-----------------------
    worksheet.write("C7", "Proveedor: ", texto)
    worksheet.merge_range("D7:G7", proveedor, texto2)
    worksheet.write("K7", "Fecha: ", texto)
    worksheet.merge_range("L7:N7", fecha2, texto2)
    worksheet.write("C8", "Numero de parte: ", texto)
    worksheet.merge_range("D8:G8", numero_parte, texto2)
    worksheet.write("I8", "Responsable: ", texto)
    worksheet.merge_range("J8:N8", responsable, texto2)
    worksheet.write("C9", "Caracteristica: ", texto)
    worksheet.merge_range("D9:G9", caracteristica, texto2)
    worksheet.write("I9", "Unidades: ", texto)
    worksheet.write("J9", unidades, texto2)
    worksheet.write("K9", "LSE: ", texto)
    worksheet.write("L9", max_spec, texto2)
    worksheet.write("M9", "LIE: ", texto)
    worksheet.write("N9", min_spec, texto2)
        
    #-----------------------
    #TABLA
    #-----------------------
        
    #Setear parametros
    folder_graficas = folder_salida + "/Graficas"
        
    #Insertar graficas
    worksheet.insert_image("B11", folder_graficas + "/" + numero_parte + "_" + fecha2 + "_Dispersion.png", {"x_scale": 1.35, "y_scale": 1.35})
    
    if campana_ == "Y":
        worksheet.insert_image("H45", folder_graficas + "/" + numero_parte + "_" + fecha2 + "_Distribucion.png", {"x_scale": 0.75, "y_scale": 0.7})
            
    #Encabezados de las tablas
    worksheet.merge_range("B41:F41", "Datos de Sub-Grupos", tabla)
    worksheet.merge_range("H41:N41", "Resumen General", tabla)
        
    #Titilos de la tabla de subgrupos
    worksheet.write("B42", "Lotes", tabla2)
    worksheet.write("C42", "Maxima", tabla2)
    worksheet.write("D42", "Minima", tabla2)
    worksheet.write("E42", "Rango ", tabla2)
    worksheet.write("F42", "Media", tabla2)
        
    #Titilos de laa tabla de subgrupos
    worksheet.write("H42", "Cantidad", tabla2)
    worksheet.write("I42", "Rango", tabla2)
    worksheet.write("J42", "Media", tabla2)
    worksheet.write("K42", "Mediana ", tabla2)
    worksheet.write("L42", "Moda", tabla2)
    worksheet.write("M42", "Sigma", tabla2)
    worksheet.write("N42", "Delta-Nom", tabla2)
        
    #Valores de tabla1
    ini = 42
    pos_col = 1
    for row_num, row_data in enumerate(informacion.values.tolist()):
        for col_num, col_data in enumerate(row_data):
            worksheet.write(ini, pos_col + col_num, col_data, tabla3)
        ini = ini + 1
        
    #Valores de tabla2
    ini = 42
    pos_col = 7
    for row_num, row_data in enumerate(informacion2.values.tolist()):
        for col_num, col_data in enumerate(row_data):
            worksheet.write(ini, pos_col + col_num, col_data, tabla3)
        ini = ini + 1
    
    #Pestaña de rawdata
    if rawdata == "Y":
        worksheet2 = workbook.add_worksheet("Raw_Data")
        
        #Titilos rawdata
        worksheet2.write("A1", "Muestra", tabla2)
        worksheet2.write("B1", "Valores", tabla2)
        worksheet2.write("C1", "Grupo", tabla2)

        #Valores de rawdata
        ini = 1
        pos_col = 0
        for row_num, row_data in enumerate(valores_cadena.values.tolist()):
            for col_num, col_data in enumerate(row_data):
                worksheet2.write(ini, pos_col + col_num, col_data, tabla3)
            ini = ini + 1
    
    #Guardar y cerrar el excel
    workbook.close()