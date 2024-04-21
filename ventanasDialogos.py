#!/usr/bin/env python
# coding: utf-8
# Autor: Francisco Rodriguez | Mty., N. L., Mx. ! 2024

import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox as mb

#Ventana de mensaje
def informar(tipo, titulo, mensaje):
    if tipo == 1:
        mb.showerror(titulo, mensaje)
    elif tipo == 2:
        mb.showinfo(titulo, mensaje)
        
#Ventana de seleccion de archivos
def seleccionarArchivos():
    root = tk.Tk()
    root.withdraw()
    #print("Favor de seleccionar los archivos con los que se trabajaran, desde la ventana emergente...")
    #print("")
    archivos = filedialog.askopenfiles(title='Selecciona los archivos para el reporte', initialdir='/', filetypes=[("Excel files", ".xlsx .xls")])
    return archivos

#Ventana de seleccion de archivos
def seleccionarLogo():
    root = tk.Tk()
    root.withdraw()
    #print("Favor de seleccionar los archivos con los que se trabajaran, desde la ventana emergente...")
    #print("")
    logo = filedialog.askopenfile(title='Selecciona el logo', initialdir='/', filetypes=[("imagenes", ".png")])
    return logo, logo.name

# Ventana emergente para seleccionar donde se guardara el reporte
def seleccionarCarpeta():
    root = tk.Tk()
    root.withdraw()
    
    #print("Por favor selecciona desde la ventana emergente la carpeta donde se guardara el reporte...")
    folder_salida = filedialog.askdirectory(title="Selecciona la carpeta donde se GUARDARA EL REPORTE")
    #print("_____________________________________________________________")
    #print("")
    #print("El reporte se guardara en: ")
    #print(folder_salida)
    #print("")
    return folder_salida