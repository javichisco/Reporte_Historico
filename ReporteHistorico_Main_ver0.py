#!/usr/bin/env python
# coding: utf-8
# Autor: Francisco Rodriguez | Mty., N. L., Mx. ! 2024

import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from Interfaces.ui_Dispersion import Ui_ventanaPrincipal
from datetime import datetime
import ventanasDialogos as pop
import Configuraciones.Configuraciones as config
import funcionesDispersion as fD
import crearGraficas as graficar
import reporteExcel as reporte
import statistics as stat
import numpy as np
import pandas as pd


class MainWindow(QMainWindow, Ui_ventanaPrincipal):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        #Setear parametros de arranque
        self.inputFecha.setDate(datetime.now().date())
        self.cargarConfiguraciones()
        self.cargarUltimosValores()
        self.lblEstatus.setText(" Por favor carga los parametros...")
        
        #Declaracion de Variables
        global archivos
        global folder_salida
        archivos = ""
        folder_salida = ""
        
        #Controles para Checkbox
        self.checkReporte.checkStateChanged.connect(self.parametrosReporte)
        self.checkAutomatico.checkStateChanged.connect(self.parametrosAutomaticos)
        self.checkCampana.checkStateChanged.connect(self.estatusCampana)
        
        #Seleccion de archivos
        self.btnArchivos.clicked.connect(self.seleccionarArchivos)
        
        #Seleccion de carpeta
        self.btnCarpeta.clicked.connect(self.seleccionarCarpeta)
        
        #Seleccion de logo
        self.logo = self.btnLogo.clicked.connect(self.seleccionarlogo)
        
        #Cargar configuraciones
        self.btnResetearConfiguracion.clicked.connect(self.cargarConfiguraciones)
        
        #Guardar configuraciones
        self.btnGuardarConfiguracion.clicked.connect(self.guardarConfiguraciones)
        
        #Guardar Ultimos Valores
        self.btnGuardar.clicked.connect(self.guardarUltimosValores)
        
        #Ejecutar Programa
        self.btnEjecutar.clicked.connect(self.ejecutarPrograma)
        
        #Borrar resultados del reporte
        self.btnBorrar.clicked.connect(self.borrarResultados)
        
        #Cambiar de Pestaña principal
        self.tabWidget.tabBarClicked.connect(self.cambioTab)
        
        #Aplicar Configuracion
        self.btnAplicarConfiguracion.clicked.connect(self.aplicarConfiguracion)
    
    def estatusCampana (self):
        self.inputCategorias.setEnabled(1) if self.checkCampana.isChecked() else self.inputCategorias.setEnabled(0)
    
    def aplicarConfiguracion(self):
        self.tabWidget.setCurrentIndex(0)
    
    def cambioTab(self, indiceTab):
        if indiceTab == 0:
            self.cargarConfiguraciones()
            pop.informar(2, "Configuracion actual", "Usted ha decidido NO aplicar los cambios; si realizas cambios en la configuracion y deaseas usarlos, deberas dar click en el botono APLICAR.")
        
    def borrarResultados(self):
        global archivos, folder_salida
        archivos = ""
        folder_salida =""
        
        self.cargarUltimosValores()
        self.tableResultados.setRowCount(0)
        self.tablePromedios.setRowCount(0)
        self.tableDatos.setRowCount(0)
        self.tableResultados.setColumnCount(0)
        self.tablePromedios.setColumnCount(0)
        self.tableDatos.setColumnCount(0)
        self.inputArchivos.setText("")
        self.inputCarpeta.setText("")
        
        self.lblEstatus.setText(" Por favor carga los parametros...")
        pop.informar(2, "Borrar Resultados", "Los Resultados anteriores han sido borrados con exito y los Parametros se han restablecido correctamente.")
        
    def ejecutarPrograma(self):
        self.lblEstatus.setText("La aplicacion No responde...")
        
        global archivos, folder_salida
        
        folder_salida = "" if not self.checkReporte.isChecked() else str(folder_salida)
        
        auto = "Y" if self.checkAutomatico.isChecked() else "N"
        auto2 = "Y" if self.checkReporte.isChecked() else "N"
        campana_ = "Y" if self.checkCampana.isChecked() else "N"
        sigma3 = "Y" if self.check3Sigma.isChecked() else "N"
        rawdata = "Y" if self.checkDatos.isChecked() else "N"
        
        columna = str(self.inputDatosColumna.text())
        colProveedor = str(self.inputProveedorColumna.text())
        colNumero = str(self.inputNumeroColumna.text())
        colCaracteristica = str(self.inputCaracteristicaColumna.text())
        colEspecificaciones = str(self.inputEspecColumna.text())
        
        fila = int(self.inputDatosFila.value())
        filaProveedor = int(self.inputProveedorFila.value())
        filaNumero = int(self.inputNumeroFila.value())
        filaCaracteristica = int(self.inputCaracteristicaFila.value())
        filaEspecificaciones = int(self.inputEspecFila.value())
        
        filas = int(self.inputMuestras.value())
        tab = str(self.inputPestana.text())
        caracteristica = str(self.inputCaracteristica.text())
        decimales = int(self.inputDecimales.value())
        categorias = int(self.inputCategorias.value())
        fecha = str(self.inputFecha.text())
        proveedor = str(self.inputProveedor.text())
        unidades = str(self.inputUnidades.text())
        responsable = str(self.inputResponsable.text())
        archivo_nombre = str(self.inputReporteName.text())
        numero_parte = str(self.inputNumero.text())
        max_spec = float(self.inputLSE.value())
        min_spec = float(self.inputLIE.value())
        
        parametrosGenerales = {
                "archivos": archivos,
                "folder_salida": folder_salida,
                "auto": auto,
                "auto2": auto2,
                "campana_": campana_,
                "sigma3": sigma3,
                "tab": tab,
                "columna": columna,
                "filas": filas,
                "caracteristica": caracteristica, 
                "decimales": decimales,
                "categorias": categorias,
                "fecha": fecha, 
                "proveedor": proveedor, 
                "unidades": unidades, 
                "responsable": responsable, 
                "archivo_nombre": archivo_nombre, 
                "numero_parte": numero_parte, 
                "max_spec": max_spec, 
                "min_spec": min_spec,
                "colProveedor": colProveedor,
                "colNumero": colNumero,
                "colCaracteristica": colCaracteristica,
                "colEspecificaciones": colEspecificaciones,
                "fila": fila,
                "filaProveedor": filaProveedor,
                "filaNumero": filaNumero,
                "filaCaracteristica": filaCaracteristica,
                "filaEspecificaciones": filaEspecificaciones,
                "rawdata": rawdata
            }
        
        if not (archivos == "" or tab  == "" or columna  == "" or fecha  == ""):
            
            valores_cadena, parametrosGenerales["caracteristica"], parametrosGenerales["numero_parte"], parametrosGenerales["proveedor"], parametrosGenerales["max_spec"], parametrosGenerales["min_spec"] = fD.leerArchivos(parametrosGenerales)

            parametrosGraficas = fD.definir_escala(valores_cadena, parametrosGenerales)
            
            self.inputProveedor.setText(str(parametrosGenerales["proveedor"]))
            self.inputCaracteristica.setText(str(parametrosGenerales["caracteristica"]))
            self.inputNumero.setText(str(parametrosGenerales["numero_parte"]))
            self.inputLSE.setValue(float(parametrosGenerales["max_spec"]))
            self.inputLIE.setValue(float(parametrosGenerales["min_spec"]))
            
            if not (parametrosGenerales["max_spec"] == "" or parametrosGenerales["min_spec"]  == "" or parametrosGenerales["numero_parte"]  == "" or parametrosGenerales["fecha"]  == ""):
                
                graficar.graficaPromedios(parametrosGraficas, parametrosGenerales)
                
                if not (categorias == "" or  campana_ == "N"): 
                    sigma, fecha2 = graficar.graficaCampana(parametrosGraficas, parametrosGenerales)
            
                else:
                    fecha2 = fecha.replace("/", "-")
                    pop.informar(2, "Campana faltante", "La grafica de campana no se agrego al reporte, si deseas agregarla; actualiza los parametros.")
                
                lotes = parametrosGraficas["lotes"]
                maximos = parametrosGraficas["maximos"]
                minimos = parametrosGraficas["minimos"]
                promedio = parametrosGraficas["promedio"]
                nominal = parametrosGraficas["nominal"]
                prom_promedio = parametrosGraficas["prom_promedio"]
                rangos = parametrosGraficas["rangos"]
                
                decimales = parametrosGenerales["decimales"]
                caracteristica = parametrosGenerales["caracteristica"]
                
                #Tabla Resultados
                self.tableResultados.setRowCount(1)
                self.tableResultados.setColumnCount(7)
                self.tableResultados.setHorizontalHeaderLabels(["Cantidad", "Rango", "Promedio", "Mediana", "Moda", "Sigma", "Delta_Nom"])
            
                self.tableResultados.setItem(0, 0, QTableWidgetItem(str(len(lotes))))
                self.tableResultados.setItem(0, 1, QTableWidgetItem(str(round(max(maximos) - min(minimos), decimales))))
                self.tableResultados.setItem(0, 2, QTableWidgetItem(str(round(stat.mean(promedio), decimales))))
                self.tableResultados.setItem(0, 3, QTableWidgetItem(str(round(stat.median(promedio), decimales))))
                self.tableResultados.setItem(0, 4, QTableWidgetItem(str(round(stat.mode(promedio), decimales))))
                self.tableResultados.setItem(0, 5, QTableWidgetItem(str(round(np.std(promedio), decimales))))
                self.tableResultados.setItem(0, 6, QTableWidgetItem(str(round(prom_promedio - nominal, decimales))))
                    
                #Tabla promedios
                contador = int(len(lotes))
                
                self.tablePromedios.setRowCount(contador)
                self.tablePromedios.setColumnCount(5)
                self.tablePromedios.setHorizontalHeaderLabels(["Grupos", "Maximo", "Minimo", "Rango", "Promedio"])
                    
                i = 0
                while i < contador:
                    self.tablePromedios.setItem(i, 0, QTableWidgetItem(str(lotes[i])))
                    self.tablePromedios.setItem(i, 1, QTableWidgetItem(str(maximos[i])))
                    self.tablePromedios.setItem(i, 2, QTableWidgetItem(str(minimos[i])))
                    self.tablePromedios.setItem(i, 3, QTableWidgetItem(str(rangos[i])))
                    self.tablePromedios.setItem(i, 4, QTableWidgetItem(str(promedio[i])))
                    i=i+1
                        
                #Tabla Datos
                muestra = list(valores_cadena["Muestra"])
                caract = list(valores_cadena[caracteristica])
                grupo = list(valores_cadena["Grupo"])
                        
                contador = int(len(muestra))
                        
                self.tableDatos.setRowCount(contador)
                self.tableDatos.setColumnCount(2)
                        
                self.tableDatos.setHorizontalHeaderLabels(["Valores", "Grupos"])
                        
                i = 0
                while i < contador:
                    self.tableDatos.setItem(i, 0, QTableWidgetItem(str(caract[i])))
                    self.tableDatos.setItem(i, 1, QTableWidgetItem(str(grupo[i])))
                    i=i+1
                        
                    #Si se selecciono generar Excel
                    if auto2 == "Y":
                        #Preparar la lista con la informacion de la tabla
                        informacion = pd.DataFrame({"Lotes": lotes,
                                                    "Maxima": maximos,
                                                    "Minima": minimos,
                                                    "Rangos": rangos,
                                                    "Promedios": promedio})
                
                    cantidad = len(lotes)
                    rango_general = round(max(maximos) - min(minimos), decimales)
                    promedio_general = round(stat.mean(promedio), decimales)
                    mediana_general = round(stat.median(promedio), decimales)
                    moda_general = round(stat.mode(promedio), decimales)
                    sigma_general = round(np.std(promedio), decimales)
                    delta_nom = round(prom_promedio - nominal, decimales)
                
                    informacion2 = pd.DataFrame({"Cantidad": [cantidad],
                                                 "Rango": [rango_general],
                                                 "Promedio": [promedio_general],
                                                 "Mediana": [mediana_general],
                                                 "Moda": [moda_general],
                                                 "Sigma": [sigma_general],
                                                 "Delta_Nom": [delta_nom]})
                
                if auto2 == "Y":
                    if not (folder_salida == ""):                    
                        reporte.dibujarTablas(informacion, informacion2, fecha2, parametrosGenerales, valores_cadena)
                        self.lblEstatus.setText(" Aplicacion ejecutada con exito!")
                        pop.informar(2, "Reporte de excel", "¡Reporte generado con exito!, lo podras localizar en la carpeta que seleccionaste.")
                    else:
                        pop.informar(1, "Reporte de Excel", "Error al generar reporte de excel: Revisa los parametros relacionados.")
                else:
                    self.lblEstatus.setText(" Aplicacion ejecutada con exito!")
            else:
                pop.informar(1, "Generacio de Graficas", "Error al gintentar generar las Graficas: Revisa los parametros relacionados.")
                    
        else:
            pop.informar(1, "Error en parametros", "Error al ejecutar: Por favor revisa que todos los parametros fueron seleccionados y/o llenados correctamente.")

                               
    def cargarUltimosValores(self):
        columna1, columna2 = config.leerConfiguraciones('Configuraciones/ultimosvalores.csv')
        for i in range (len(columna1)):
            if columna1[i] == "responsable":
                self.inputResponsable.setText(str(columna2[i]))
            elif columna1[i] == "unidades":
                self.inputUnidades.setText(str(columna2[i]))
            elif columna1[i] == "reporte_nombre":
                self.inputReporteName.setText(str(columna2[i]))
            elif columna1[i] == "automatico":
                self.checkAutomatico.setChecked(int(columna2[i]))
            elif columna1[i] == "excel":
                self.checkReporte.setChecked(int(columna2[i]))
            elif columna1[i] == "proveedor":
                self.inputProveedor.setText(str(columna2[i]))
            elif columna1[i] == "caracteristica":
                self.inputCaracteristica.setText(str(columna2[i]))
            elif columna1[i] == "numero":
                self.inputNumero.setText(str(columna2[i]))
            elif columna1[i] == "lse":
                self.inputLSE.setValue(float(columna2[i]))
            elif columna1[i] == "lie":
                self.inputLIE.setValue(float(columna2[i]))
            elif columna1[i] == "raw_data":
                self.checkDatos.setChecked(int(columna2[i]))
            self.parametrosAutomaticos()
            self.parametrosReporte()

    def guardarUltimosValores(self):
        headers = ["variables", "valores"]
        contenido = [
            ["responsable", self.inputResponsable.text()],
            ["unidades", self.inputUnidades.text()],
            ["reporte_nombre", self.inputReporteName.text()],
            ["automatico", int(self.checkAutomatico.isChecked())],
            ["excel", int(self.checkReporte.isChecked())],
            ["proveedor", self.inputProveedor.text()],
            ["caracteristica", self.inputCaracteristica.text()],
            ["numero", self.inputNumero.text()],
            ["lse", self.inputLSE.value()],
            ["lie", self.inputLIE.value()],
            ["raw_data", int(self.checkDatos.isChecked())]
            ]
        config.guardarConfiguraciones(headers, contenido, 'Configuraciones/ultimosvalores.csv')
        pop.informar(2, "Parametros de arranque", "Los parametros de arranque fueron actualizados con exito; veras estos valores la siguiente vez que inicies la aplicacion.")

    def guardarConfiguraciones(self):
        headers = ["variables", "valores"]
        contenido = [
            ["categorias", self.inputCategorias.value()],
            ["decimales", self.inputDecimales.value()],
            ["muestras", self.inputMuestras.value()],
            ["logo", self.inputLogo.text()],
            ["pestana", self.inputPestana.text()],
            ["campana", int(self.checkCampana.isChecked())],
            ["proveedor_columna", self.inputProveedorColumna.text()],
            ["proveedor_fila", self.inputProveedorFila.value()],
            ["caracteristica_columna", self.inputCaracteristicaColumna.text()],
            ["caracteristica_fila", self.inputCaracteristicaFila.value()],
            ["numero_columna", self.inputNumeroColumna.text()],
            ["numero_fila", self.inputNumeroFila.value()],
            ["datos_columna", self.inputDatosColumna.text()],
            ["datos_fila", self.inputDatosFila.value()],
            ["3sigma", int(self.check3Sigma.isChecked())],
            ["especificaciones_columna", self.inputEspecColumna.text()],
            ["especificaciones_fila", self.inputEspecFila.value()]
            ]
        config.guardarConfiguraciones(headers, contenido, 'Configuraciones/configuracion.csv')
        pop.informar(2, "Configuraciones", "Los valores de Configuracion fueron actualizados con exito; veras estos valores la siguiente vez que inicies la aplicacion.")
    
    def cargarConfiguraciones(self):
        columna1, columna2 = config.leerConfiguraciones('Configuraciones/configuracion.csv')
        for i in range (len(columna1)):
            if columna1[i] == "categorias":
                self.inputCategorias.setValue(int(columna2[i]))
            elif columna1[i] == "decimales":
                self.inputDecimales.setValue(int(columna2[i]))
            elif columna1[i] == "muestras":
                self.inputMuestras.setValue(int(columna2[i]))
            elif columna1[i] == "pestana":
                self.inputPestana.setText(str(columna2[i]))
            elif columna1[i] == "logo":
                self.inputLogo.setText(str(columna2[i]))
            elif columna1[i] == "campana":
                self.checkCampana.setChecked(int(columna2[i]))
                self.inputCategorias.setEnabled(1) if self.checkCampana.isChecked() else self.inputCategorias.setEnabled(0)
            elif columna1[i] == "proveedor_columna":
                self.inputProveedorColumna.setText(str(columna2[i]))
            elif columna1[i] == "proveedor_fila":
                self.inputProveedorFila.setValue(int(columna2[i]))
            elif columna1[i] == "caracteristica_columna":
                self.inputCaracteristicaColumna.setText(str(columna2[i]))
            elif columna1[i] == "caracteristica_fila":
                self.inputCaracteristicaFila.setValue(int(columna2[i]))
            elif columna1[i] == "numero_columna":
                self.inputNumeroColumna.setText(str(columna2[i]))
            elif columna1[i] == "numero_fila":
                self.inputNumeroFila.setValue(int(columna2[i]))
            elif columna1[i] == "datos_columna":
                self.inputDatosColumna.setText(str(columna2[i]))
            elif columna1[i] == "datos_fila":
                self.inputDatosFila.setValue(int(columna2[i]))
            elif columna1[i] == "3sigma":
                self.check3Sigma.setChecked(int(columna2[i]))
            elif columna1[i] == "especificaciones_columna":
                self.inputEspecColumna.setText(str(columna2[i]))
            elif columna1[i] == "especificaciones_fila":
                self.inputEspecFila.setValue(int(columna2[i]))
            
    def seleccionarlogo(self):
        logo, logo_str = pop.seleccionarLogo()
        self.inputLogo.setText(logo_str)
        return logo
    
    def seleccionarCarpeta(self):
        global folder_salida
        folder_salida = pop.seleccionarCarpeta()
        self.inputCarpeta.setText(str(folder_salida))
        return folder_salida
    
    def seleccionarArchivos(self):
        global archivos
        archivos = pop.seleccionarArchivos()
        archivos_str = "Se seleccionaron " + str(len(archivos)) + " archivos .xls"
        self.inputArchivos.setText(archivos_str)
        
    def parametrosAutomaticos(self):
        if self.checkAutomatico.isChecked():
            self.inputCaracteristica.setEnabled(False)
            self.inputLIE.setEnabled(False)
            self.inputLSE.setEnabled(False)
            self.inputNumero.setEnabled(False)
            self.inputProveedor.setEnabled(False)
        else:
            self.inputCaracteristica.setEnabled(True)
            self.inputLIE.setEnabled(True)
            self.inputLSE.setEnabled(True)
            self.inputNumero.setEnabled(True)
            self.inputProveedor.setEnabled(True)
    
    def parametrosReporte(self):
        if self.checkReporte.isChecked():
            self.inputCarpeta.setEnabled(True)
            self.btnCarpeta.setEnabled(True)
            self.inputReporteName.setEnabled(True)
            self.inputLogo.setEnabled(True)
            self.btnLogo.setEnabled(True)
        else:
            self.inputCarpeta.setEnabled(False)
            self.btnCarpeta.setEnabled(False)
            self.inputReporteName.setEnabled(False)
            self.inputLogo.setEnabled(False)
            self.btnLogo.setEnabled(False)

#Cargar y generar la aplicacion        
if __name__ == '__main__':
    sys.argv += ['-platform', 'windows:darkmode=2']
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    window = MainWindow()
    window.show()
    app.exec()
    app.shutdown()
    

