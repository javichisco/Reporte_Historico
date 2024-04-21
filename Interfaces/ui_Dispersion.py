#!/usr/bin/env python
# coding: utf-8
# Autor: Francisco Rodriguez | Mty., N. L., Mx. ! 2024

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_ventanaPrincipal(object):
    def setupUi(self, ventanaPrincipal):
        if not ventanaPrincipal.objectName():
            ventanaPrincipal.setObjectName(u"ventanaPrincipal")
        self.setFixedSize(QSize(790, 630))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ventanaPrincipal.sizePolicy().hasHeightForWidth())
        ventanaPrincipal.setSizePolicy(sizePolicy)
        self.centralWidget = QWidget(ventanaPrincipal)
        self.centralWidget.setObjectName(u"centralWidget")
        sizePolicy.setHeightForWidth(self.centralWidget.sizePolicy().hasHeightForWidth())
        self.centralWidget.setSizePolicy(sizePolicy)
        self.tabWidget = QTabWidget(self.centralWidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(20, 10, 751, 590))
        palette = QPalette()
        brush = QBrush(QColor(240, 240, 240, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        brush1 = QBrush(QColor(255, 255, 255, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush1)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        brush2 = QBrush(QColor(255, 255, 255, 128))
        brush2.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush2)
#endif
        self.tabWidget.setPalette(palette)
        self.tabWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet(u"background-color: rgb(240, 240, 240);")
        self.tabPrincipal = QWidget()
        self.tabPrincipal.setObjectName(u"tabPrincipal")
        self.titulo = QLabel(self.tabPrincipal)
        self.titulo.setObjectName(u"titulo")
        self.titulo.setGeometry(QRect(20, 10, 721, 31))
        font = QFont()
        font.setPointSize(14)
        font.setBold(False)
        self.titulo.setFont(font)
        self.titulo.setScaledContents(False)
        self.titulo.setAlignment(Qt.AlignCenter)
        self.titulo.setWordWrap(False)
        self.gridLayoutWidget = QWidget(self.tabPrincipal)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(20, 60, 701, 261))
        self.gridEntrada = QGridLayout(self.gridLayoutWidget)
        self.gridEntrada.setObjectName(u"gridEntrada")
        self.gridEntrada.setHorizontalSpacing(4)
        self.gridEntrada.setVerticalSpacing(8)
        self.gridEntrada.setContentsMargins(0, 0, 0, 0)
        self.lblAutomatico = QLabel(self.gridLayoutWidget)
        self.lblAutomatico.setObjectName(u"lblAutomatico")
        self.lblAutomatico.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridEntrada.addWidget(self.lblAutomatico, 3, 0, 1, 1)

        self.lblNumero = QLabel(self.gridLayoutWidget)
        self.lblNumero.setObjectName(u"lblNumero")
        self.lblNumero.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridEntrada.addWidget(self.lblNumero, 5, 3, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btnArchivos = QToolButton(self.gridLayoutWidget)
        self.btnArchivos.setObjectName(u"btnArchivos")
        self.btnArchivos.setPopupMode(QToolButton.DelayedPopup)
        self.btnArchivos.setToolButtonStyle(Qt.ToolButtonIconOnly)

        self.horizontalLayout.addWidget(self.btnArchivos)

        self.inputArchivos = QLineEdit(self.gridLayoutWidget)
        self.inputArchivos.setObjectName(u"inputArchivos")
        self.inputArchivos.setEnabled(False)

        self.horizontalLayout.addWidget(self.inputArchivos)


        self.gridEntrada.addLayout(self.horizontalLayout, 1, 2, 1, 1)

        self.lblCarpeta = QLabel(self.gridLayoutWidget)
        self.lblCarpeta.setObjectName(u"lblCarpeta")
        self.lblCarpeta.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridEntrada.addWidget(self.lblCarpeta, 3, 3, 1, 1)

        self.lblReporteName = QLabel(self.gridLayoutWidget)
        self.lblReporteName.setObjectName(u"lblReporteName")
        self.lblReporteName.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridEntrada.addWidget(self.lblReporteName, 2, 3, 1, 1)

        self.inputLSE = QDoubleSpinBox(self.gridLayoutWidget)
        self.inputLSE.setObjectName(u"inputLSE")
        self.inputLSE.setEnabled(False)

        self.gridEntrada.addWidget(self.inputLSE, 6, 2, 1, 1)

        self.lblLIE = QLabel(self.gridLayoutWidget)
        self.lblLIE.setObjectName(u"lblLIE")
        self.lblLIE.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridEntrada.addWidget(self.lblLIE, 6, 3, 1, 1)

        self.inputFecha = QDateEdit(self.gridLayoutWidget)
        self.inputFecha.setObjectName(u"inputFecha")
        sizePolicy.setHeightForWidth(self.inputFecha.sizePolicy().hasHeightForWidth())
        self.inputFecha.setSizePolicy(sizePolicy)

        self.gridEntrada.addWidget(self.inputFecha, 0, 4, 1, 1)

        self.btnBorrar = QPushButton(self.gridLayoutWidget)
        self.btnBorrar.setObjectName(u"btnBorrar")
        self.btnBorrar.setStyleSheet(u"background-color: rgb(255, 0, 0);\n"
"color: rgb(255, 255, 255);")

        self.gridEntrada.addWidget(self.btnBorrar, 7, 3, 1, 1)

        self.lblReporte = QLabel(self.gridLayoutWidget)
        self.lblReporte.setObjectName(u"lblReporte")
        self.lblReporte.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridEntrada.addWidget(self.lblReporte, 1, 3, 1, 1)

        self.inputCaracteristica = QLineEdit(self.gridLayoutWidget)
        self.inputCaracteristica.setObjectName(u"inputCaracteristica")
        self.inputCaracteristica.setEnabled(False)

        self.gridEntrada.addWidget(self.inputCaracteristica, 5, 2, 1, 1)

        self.inputProveedor = QLineEdit(self.gridLayoutWidget)
        self.inputProveedor.setObjectName(u"inputProveedor")
        self.inputProveedor.setEnabled(False)

        self.gridEntrada.addWidget(self.inputProveedor, 4, 2, 1, 1)

        self.checkDatos = QCheckBox(self.gridLayoutWidget)
        self.checkDatos.setObjectName(u"checkDatos")
        self.checkDatos.setChecked(True)

        self.gridEntrada.addWidget(self.checkDatos, 4, 4, 1, 1)

        self.lblResponsable = QLabel(self.gridLayoutWidget)
        self.lblResponsable.setObjectName(u"lblResponsable")
        self.lblResponsable.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridEntrada.addWidget(self.lblResponsable, 0, 0, 1, 1)

        self.inputUnidades = QLineEdit(self.gridLayoutWidget)
        self.inputUnidades.setObjectName(u"inputUnidades")

        self.gridEntrada.addWidget(self.inputUnidades, 2, 2, 1, 1)

        self.inputResponsable = QLineEdit(self.gridLayoutWidget)
        self.inputResponsable.setObjectName(u"inputResponsable")

        self.gridEntrada.addWidget(self.inputResponsable, 0, 2, 1, 1)

        self.lblFecha = QLabel(self.gridLayoutWidget)
        self.lblFecha.setObjectName(u"lblFecha")
        self.lblFecha.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridEntrada.addWidget(self.lblFecha, 0, 3, 1, 1)

        self.lblLSE = QLabel(self.gridLayoutWidget)
        self.lblLSE.setObjectName(u"lblLSE")
        self.lblLSE.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridEntrada.addWidget(self.lblLSE, 6, 0, 1, 1)

        self.checkReporte = QCheckBox(self.gridLayoutWidget)
        self.checkReporte.setObjectName(u"checkReporte")
        self.checkReporte.setChecked(False)

        self.gridEntrada.addWidget(self.checkReporte, 1, 4, 1, 1)

        self.lblDatos = QLabel(self.gridLayoutWidget)
        self.lblDatos.setObjectName(u"lblDatos")
        self.lblDatos.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridEntrada.addWidget(self.lblDatos, 4, 3, 1, 1)

        self.checkAutomatico = QCheckBox(self.gridLayoutWidget)
        self.checkAutomatico.setObjectName(u"checkAutomatico")
        self.checkAutomatico.setChecked(True)

        self.gridEntrada.addWidget(self.checkAutomatico, 3, 2, 1, 1)

        self.btnEjecutar = QPushButton(self.gridLayoutWidget)
        self.btnEjecutar.setObjectName(u"btnEjecutar")
        self.btnEjecutar.setStyleSheet(u"background-color: rgb(0, 0, 255);\n"
"color: rgb(255, 255, 255);")

        self.gridEntrada.addWidget(self.btnEjecutar, 7, 4, 1, 1)

        self.inputReporteName = QLineEdit(self.gridLayoutWidget)
        self.inputReporteName.setObjectName(u"inputReporteName")
        self.inputReporteName.setEnabled(False)

        self.gridEntrada.addWidget(self.inputReporteName, 2, 4, 1, 1)

        self.lblArchivos = QLabel(self.gridLayoutWidget)
        self.lblArchivos.setObjectName(u"lblArchivos")
        self.lblArchivos.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridEntrada.addWidget(self.lblArchivos, 1, 0, 1, 1)

        self.lblUnidades = QLabel(self.gridLayoutWidget)
        self.lblUnidades.setObjectName(u"lblUnidades")
        self.lblUnidades.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridEntrada.addWidget(self.lblUnidades, 2, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btnCarpeta = QToolButton(self.gridLayoutWidget)
        self.btnCarpeta.setObjectName(u"btnCarpeta")
        self.btnCarpeta.setEnabled(False)

        self.horizontalLayout_2.addWidget(self.btnCarpeta)

        self.inputCarpeta = QLineEdit(self.gridLayoutWidget)
        self.inputCarpeta.setObjectName(u"inputCarpeta")
        self.inputCarpeta.setEnabled(False)

        self.horizontalLayout_2.addWidget(self.inputCarpeta)


        self.gridEntrada.addLayout(self.horizontalLayout_2, 3, 4, 1, 1)

        self.lblCaracteristica = QLabel(self.gridLayoutWidget)
        self.lblCaracteristica.setObjectName(u"lblCaracteristica")
        self.lblCaracteristica.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridEntrada.addWidget(self.lblCaracteristica, 5, 0, 1, 1)

        self.lblProveedor = QLabel(self.gridLayoutWidget)
        self.lblProveedor.setObjectName(u"lblProveedor")
        self.lblProveedor.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridEntrada.addWidget(self.lblProveedor, 4, 0, 1, 1)

        self.inputNumero = QLineEdit(self.gridLayoutWidget)
        self.inputNumero.setObjectName(u"inputNumero")
        self.inputNumero.setEnabled(False)

        self.gridEntrada.addWidget(self.inputNumero, 5, 4, 1, 1)

        self.inputLIE = QDoubleSpinBox(self.gridLayoutWidget)
        self.inputLIE.setObjectName(u"inputLIE")
        self.inputLIE.setEnabled(False)

        self.gridEntrada.addWidget(self.inputLIE, 6, 4, 1, 1)

        self.lblEstatus = QLabel(self.gridLayoutWidget)
        self.lblEstatus.setObjectName(u"lblEstatus")

        self.gridEntrada.addWidget(self.lblEstatus, 7, 2, 1, 1)

        self.btnGuardar = QPushButton(self.gridLayoutWidget)
        self.btnGuardar.setObjectName(u"btnGuardar")
        self.btnGuardar.setStyleSheet(u"background-color: rgb(0, 0, 255);\n"
"color: rgb(255, 255, 255);")

        self.gridEntrada.addWidget(self.btnGuardar, 7, 0, 1, 1)

        self.lblResponsable.raise_()
        self.inputResponsable.raise_()
        self.checkReporte.raise_()
        self.lblReporte.raise_()
        self.inputFecha.raise_()
        self.lblFecha.raise_()
        self.lblArchivos.raise_()
        self.lblReporteName.raise_()
        self.inputReporteName.raise_()
        self.lblCarpeta.raise_()
        self.lblUnidades.raise_()
        self.inputUnidades.raise_()
        self.lblAutomatico.raise_()
        self.checkAutomatico.raise_()
        self.lblProveedor.raise_()
        self.lblCaracteristica.raise_()
        self.lblLIE.raise_()
        self.inputProveedor.raise_()
        self.inputCaracteristica.raise_()
        self.lblLSE.raise_()
        self.inputNumero.raise_()
        self.lblNumero.raise_()
        self.lblDatos.raise_()
        self.checkDatos.raise_()
        self.inputLSE.raise_()
        self.inputLIE.raise_()
        self.btnEjecutar.raise_()
        self.btnBorrar.raise_()
        self.lblEstatus.raise_()
        self.btnGuardar.raise_()
        self.line = QFrame(self.tabPrincipal)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(20, 40, 701, 20))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.tabWidget2 = QTabWidget(self.tabPrincipal)
        self.tabWidget2.setObjectName(u"tabWidget2")
        self.tabWidget2.setGeometry(QRect(20, 320, 711, 221))
        self.tabResultados = QWidget()
        self.tabResultados.setObjectName(u"tabResultados")
        self.tableResultados = QTableWidget(self.tabResultados)
        self.tableResultados.setObjectName(u"tableResultados")
        self.tableResultados.setGeometry(QRect(10, 10, 681, 171))
        self.tabWidget2.addTab(self.tabResultados, "")
        self.tabPromedios = QWidget()
        self.tabPromedios.setObjectName(u"tabPromedios")
        self.tablePromedios = QTableWidget(self.tabPromedios)
        self.tablePromedios.setObjectName(u"tablePromedios")
        self.tablePromedios.setGeometry(QRect(10, 10, 681, 171))
        self.tabWidget2.addTab(self.tabPromedios, "")
        self.tabDatos = QWidget()
        self.tabDatos.setObjectName(u"tabDatos")
        self.tableDatos = QTableWidget(self.tabDatos)
        self.tableDatos.setObjectName(u"tableDatos")
        self.tableDatos.setGeometry(QRect(10, 10, 681, 171))
        self.tabWidget2.addTab(self.tabDatos, "")
        self.tabWidget.addTab(self.tabPrincipal, "")
        self.tabConfiguracion = QWidget()
        self.tabConfiguracion.setObjectName(u"tabConfiguracion")
        self.titulo_2 = QLabel(self.tabConfiguracion)
        self.titulo_2.setObjectName(u"titulo_2")
        self.titulo_2.setGeometry(QRect(20, 10, 721, 31))
        self.titulo_2.setFont(font)
        self.titulo_2.setScaledContents(False)
        self.titulo_2.setAlignment(Qt.AlignCenter)
        self.titulo_2.setWordWrap(False)
        self.horizontalLayoutWidget_3 = QWidget(self.tabConfiguracion)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(30, 60, 691, 31))
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.lblCategorias = QLabel(self.horizontalLayoutWidget_3)
        self.lblCategorias.setObjectName(u"lblCategorias")
        self.lblCategorias.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.lblCategorias)

        self.inputCategorias = QSpinBox(self.horizontalLayoutWidget_3)
        self.inputCategorias.setObjectName(u"inputCategorias")

        self.horizontalLayout_3.addWidget(self.inputCategorias)

        self.lblDecimales = QLabel(self.horizontalLayoutWidget_3)
        self.lblDecimales.setObjectName(u"lblDecimales")
        self.lblDecimales.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.lblDecimales)

        self.inputDecimales = QSpinBox(self.horizontalLayoutWidget_3)
        self.inputDecimales.setObjectName(u"inputDecimales")

        self.horizontalLayout_3.addWidget(self.inputDecimales)

        self.lblMuestras = QLabel(self.horizontalLayoutWidget_3)
        self.lblMuestras.setObjectName(u"lblMuestras")

        self.horizontalLayout_3.addWidget(self.lblMuestras)

        self.inputMuestras = QSpinBox(self.horizontalLayoutWidget_3)
        self.inputMuestras.setObjectName(u"inputMuestras")

        self.horizontalLayout_3.addWidget(self.inputMuestras)

        self.line_2 = QFrame(self.tabConfiguracion)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(30, 40, 691, 16))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.line_3 = QFrame(self.tabConfiguracion)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(30, 150, 691, 16))
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.horizontalLayoutWidget_4 = QWidget(self.tabConfiguracion)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(300, 490, 421, 31))
        self.horizontalLayout_4 = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.btnResetearConfiguracion = QPushButton(self.horizontalLayoutWidget_4)
        self.btnResetearConfiguracion.setObjectName(u"btnResetearConfiguracion")
        self.btnResetearConfiguracion.setStyleSheet(u"background-color: rgb(255, 0, 0);\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_4.addWidget(self.btnResetearConfiguracion)

        self.btnGuardarConfiguracion = QPushButton(self.horizontalLayoutWidget_4)
        self.btnGuardarConfiguracion.setObjectName(u"btnGuardarConfiguracion")
        self.btnGuardarConfiguracion.setStyleSheet(u"background-color: rgb(85, 0, 255);\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_4.addWidget(self.btnGuardarConfiguracion)

        self.btnAplicarConfiguracion = QPushButton(self.horizontalLayoutWidget_4)
        self.btnAplicarConfiguracion.setObjectName(u"btnAplicarConfiguracion")
        self.btnAplicarConfiguracion.setStyleSheet(u"background-color: rgb(85, 0, 255);\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_4.addWidget(self.btnAplicarConfiguracion)

        self.horizontalLayoutWidget_5 = QWidget(self.tabConfiguracion)
        self.horizontalLayoutWidget_5.setObjectName(u"horizontalLayoutWidget_5")
        self.horizontalLayoutWidget_5.setGeometry(QRect(30, 100, 691, 41))
        self.horizontalLayout_5 = QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.lblLogo = QLabel(self.horizontalLayoutWidget_5)
        self.lblLogo.setObjectName(u"lblLogo")
        
        self.horizontalLayout_5.addWidget(self.lblLogo)

        self.btnLogo = QToolButton(self.horizontalLayoutWidget_5)
        self.btnLogo.setObjectName(u"btnLogo")

        self.horizontalLayout_5.addWidget(self.btnLogo)

        self.inputLogo = QLineEdit(self.horizontalLayoutWidget_5)
        self.inputLogo.setObjectName(u"inputLogo")

        self.horizontalLayout_5.addWidget(self.inputLogo)
        
        self.lblPestana = QLabel(self.horizontalLayoutWidget_5)
        self.lblPestana.setObjectName(u"lblPestana")
        self.lblPestana.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        
        self.horizontalLayout_5.addWidget(self.lblPestana)
        
        self.inputPestana = QLineEdit(self.horizontalLayoutWidget_5)
        self.inputPestana.setObjectName(u"inputPestana")

        self.horizontalLayout_5.addWidget(self.inputPestana)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.checkCampana = QCheckBox(self.horizontalLayoutWidget_5)
        self.checkCampana.setObjectName(u"checkCampana")
        self.checkCampana.setChecked(True)

        self.verticalLayout.addWidget(self.checkCampana)

        self.check3Sigma = QCheckBox(self.horizontalLayoutWidget_5)
        self.check3Sigma.setObjectName(u"check3Sigma")
        self.check3Sigma.setChecked(True)

        self.verticalLayout.addWidget(self.check3Sigma)
        
        
        self.horizontalLayout_5.addLayout(self.verticalLayout)

        self.gridLayoutWidget_2 = QWidget(self.tabConfiguracion)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(60, 170, 621, 171))
        self.gridCeldas = QGridLayout(self.gridLayoutWidget_2)
        self.gridCeldas.setObjectName(u"gridCeldas")
        self.gridCeldas.setContentsMargins(0, 0, 0, 0)
        self.inputNumeroFila = QSpinBox(self.gridLayoutWidget_2)
        self.inputNumeroFila.setObjectName(u"inputNumeroFila")

        self.gridCeldas.addWidget(self.inputNumeroFila, 1, 8, 1, 1)

        self.inputDatosFila = QSpinBox(self.gridLayoutWidget_2)
        self.inputDatosFila.setObjectName(u"inputDatosFila")

        self.gridCeldas.addWidget(self.inputDatosFila, 3, 8, 1, 1)

        self.inputCaracteristicaColumna = QLineEdit(self.gridLayoutWidget_2)
        self.inputCaracteristicaColumna.setObjectName(u"inputCaracteristicaColumna")
        sizePolicy.setHeightForWidth(self.inputCaracteristicaColumna.sizePolicy().hasHeightForWidth())
        self.inputCaracteristicaColumna.setSizePolicy(sizePolicy)
        self.inputCaracteristicaColumna.setMaxLength(1)

        self.gridCeldas.addWidget(self.inputCaracteristicaColumna, 3, 1, 1, 1)

        self.lblFilaCaracteristica = QLabel(self.gridLayoutWidget_2)
        self.lblFilaCaracteristica.setObjectName(u"lblFilaCaracteristica")
        self.lblFilaCaracteristica.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridCeldas.addWidget(self.lblFilaCaracteristica, 3, 2, 1, 1)

        self.lblColumnaCaracteristica = QLabel(self.gridLayoutWidget_2)
        self.lblColumnaCaracteristica.setObjectName(u"lblColumnaCaracteristica")
        self.lblColumnaCaracteristica.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridCeldas.addWidget(self.lblColumnaCaracteristica, 3, 0, 1, 1)

        self.lblColumnaProveedor = QLabel(self.gridLayoutWidget_2)
        self.lblColumnaProveedor.setObjectName(u"lblColumnaProveedor")
        self.lblColumnaProveedor.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridCeldas.addWidget(self.lblColumnaProveedor, 1, 0, 1, 1)

        self.lblFilaProveedor = QLabel(self.gridLayoutWidget_2)
        self.lblFilaProveedor.setObjectName(u"lblFilaProveedor")
        self.lblFilaProveedor.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridCeldas.addWidget(self.lblFilaProveedor, 1, 2, 1, 1)

        self.inputCaracteristicaFila = QSpinBox(self.gridLayoutWidget_2)
        self.inputCaracteristicaFila.setObjectName(u"inputCaracteristicaFila")

        self.gridCeldas.addWidget(self.inputCaracteristicaFila, 3, 3, 1, 1)

        self.horizontalSpacer = QSpacerItem(50, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridCeldas.addItem(self.horizontalSpacer, 1, 4, 1, 1)

        self.inputProveedorFila = QSpinBox(self.gridLayoutWidget_2)
        self.inputProveedorFila.setObjectName(u"inputProveedorFila")

        self.gridCeldas.addWidget(self.inputProveedorFila, 1, 3, 1, 1)

        self.inputProveedorColumna = QLineEdit(self.gridLayoutWidget_2)
        self.inputProveedorColumna.setObjectName(u"inputProveedorColumna")
        sizePolicy.setHeightForWidth(self.inputProveedorColumna.sizePolicy().hasHeightForWidth())
        self.inputProveedorColumna.setSizePolicy(sizePolicy)
        self.inputProveedorColumna.setMaxLength(1)

        self.gridCeldas.addWidget(self.inputProveedorColumna, 1, 1, 1, 1)

        self.lblCaracteristica_2 = QLabel(self.gridLayoutWidget_2)
        self.lblCaracteristica_2.setObjectName(u"lblCaracteristica_2")
        self.lblCaracteristica_2.setAlignment(Qt.AlignCenter)

        self.gridCeldas.addWidget(self.lblCaracteristica_2, 2, 1, 1, 1)

        self.lbl3Sigma = QLabel(self.gridLayoutWidget_2)
        self.lbl3Sigma.setObjectName(u"lbl3Sigma")
        self.lbl3Sigma.setAlignment(Qt.AlignCenter)

        self.gridCeldas.addWidget(self.lbl3Sigma, 4, 1, 1, 1)

        self.lblFilaDatos = QLabel(self.gridLayoutWidget_2)
        self.lblFilaDatos.setObjectName(u"lblFilaDatos")
        self.lblFilaDatos.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridCeldas.addWidget(self.lblFilaDatos, 3, 7, 1, 1)

        self.lblProveedor_2 = QLabel(self.gridLayoutWidget_2)
        self.lblProveedor_2.setObjectName(u"lblProveedor_2")
        self.lblProveedor_2.setAlignment(Qt.AlignCenter)

        self.gridCeldas.addWidget(self.lblProveedor_2, 0, 1, 1, 1)

        self.lblColumnaNumero = QLabel(self.gridLayoutWidget_2)
        self.lblColumnaNumero.setObjectName(u"lblColumnaNumero")
        self.lblColumnaNumero.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridCeldas.addWidget(self.lblColumnaNumero, 1, 5, 1, 1)

        self.lblColumnaDatos = QLabel(self.gridLayoutWidget_2)
        self.lblColumnaDatos.setObjectName(u"lblColumnaDatos")
        self.lblColumnaDatos.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridCeldas.addWidget(self.lblColumnaDatos, 3, 5, 1, 1)

        self.inputDatosColumna = QLineEdit(self.gridLayoutWidget_2)
        self.inputDatosColumna.setObjectName(u"inputDatosColumna")
        sizePolicy.setHeightForWidth(self.inputDatosColumna.sizePolicy().hasHeightForWidth())
        self.inputDatosColumna.setSizePolicy(sizePolicy)
        self.inputDatosColumna.setMaxLength(1)

        self.gridCeldas.addWidget(self.inputDatosColumna, 3, 6, 1, 1)

        self.lblNumero_2 = QLabel(self.gridLayoutWidget_2)
        self.lblNumero_2.setObjectName(u"lblNumero_2")
        self.lblNumero_2.setAlignment(Qt.AlignCenter)

        self.gridCeldas.addWidget(self.lblNumero_2, 0, 6, 1, 1)

        self.lblDatos_2 = QLabel(self.gridLayoutWidget_2)
        self.lblDatos_2.setObjectName(u"lblDatos_2")
        self.lblDatos_2.setAlignment(Qt.AlignCenter)

        self.gridCeldas.addWidget(self.lblDatos_2, 2, 6, 1, 1)

        self.inputNumeroColumna = QLineEdit(self.gridLayoutWidget_2)
        self.inputNumeroColumna.setObjectName(u"inputNumeroColumna")
        sizePolicy.setHeightForWidth(self.inputNumeroColumna.sizePolicy().hasHeightForWidth())
        self.inputNumeroColumna.setSizePolicy(sizePolicy)
        self.inputNumeroColumna.setMaxLength(1)

        self.gridCeldas.addWidget(self.inputNumeroColumna, 1, 6, 1, 1)

        self.lblFilaNumero = QLabel(self.gridLayoutWidget_2)
        self.lblFilaNumero.setObjectName(u"lblFilaNumero")
        self.lblFilaNumero.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridCeldas.addWidget(self.lblFilaNumero, 1, 7, 1, 1)

        self.inputEspecColumna = QLineEdit(self.gridLayoutWidget_2)
        self.inputEspecColumna.setObjectName(u"inputEspecColumna")
        sizePolicy.setHeightForWidth(self.inputEspecColumna.sizePolicy().hasHeightForWidth())
        self.inputEspecColumna.setSizePolicy(sizePolicy)
        self.inputEspecColumna.setMaxLength(1)

        self.gridCeldas.addWidget(self.inputEspecColumna, 5, 1, 1, 1)

        self.lblColumnaEspecificaciones = QLabel(self.gridLayoutWidget_2)
        self.lblColumnaEspecificaciones.setObjectName(u"lblColumnaEspecificaciones")
        self.lblColumnaEspecificaciones.setLayoutDirection(Qt.LeftToRight)
        self.lblColumnaEspecificaciones.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridCeldas.addWidget(self.lblColumnaEspecificaciones, 5, 0, 1, 1)

        self.lblFilaEspecificaciones = QLabel(self.gridLayoutWidget_2)
        self.lblFilaEspecificaciones.setObjectName(u"lblFilaEspecificaciones")
        self.lblFilaEspecificaciones.setLayoutDirection(Qt.LeftToRight)
        self.lblFilaEspecificaciones.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridCeldas.addWidget(self.lblFilaEspecificaciones, 5, 2, 1, 1)

        self.inputEspecFila = QSpinBox(self.gridLayoutWidget_2)
        self.inputEspecFila.setObjectName(u"inputEspecFila")

        self.gridCeldas.addWidget(self.inputEspecFila, 5, 3, 1, 1)

        self.tabWidget.addTab(self.tabConfiguracion, "")
        ventanaPrincipal.setCentralWidget(self.centralWidget)
        self.statusbar = QStatusBar(ventanaPrincipal)
        self.statusbar.setObjectName(u"statusbar")
        ventanaPrincipal.setStatusBar(self.statusbar)

        self.retranslateUi(ventanaPrincipal)

        self.tabWidget.setCurrentIndex(0)
        self.tabWidget2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(ventanaPrincipal)
    # setupUi

    def retranslateUi(self, ventanaPrincipal):
        ventanaPrincipal.setWindowTitle(QCoreApplication.translate("ventanaPrincipal", u"Generador Automatico de Reportes | Francisco J. Rodriguez Gza. 2024", None))
#if QT_CONFIG(accessibility)
        self.tabWidget.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.titulo.setText(QCoreApplication.translate("ventanaPrincipal", u"Ingresa los valores requeridos para iniciar el programa", None))
        self.lblAutomatico.setText(QCoreApplication.translate("ventanaPrincipal", u"Automatico: ", None))
        self.lblNumero.setText(QCoreApplication.translate("ventanaPrincipal", u"Numero de Parte: ", None))
        self.btnArchivos.setText(QCoreApplication.translate("ventanaPrincipal", u"...", None))
        self.lblCarpeta.setText(QCoreApplication.translate("ventanaPrincipal", u"Carpeta de salida: ", None))
        self.lblReporteName.setText(QCoreApplication.translate("ventanaPrincipal", u"Nombre del reporte: ", None))
        self.lblLIE.setText(QCoreApplication.translate("ventanaPrincipal", u"LIE: ", None))
        self.btnBorrar.setText(QCoreApplication.translate("ventanaPrincipal", u"Borrar", None))
        self.lblReporte.setText(QCoreApplication.translate("ventanaPrincipal", u"Reporte: ", None))
        self.checkDatos.setText(QCoreApplication.translate("ventanaPrincipal", u"Incluir pesta\u00f1a con todos los datos", None))
        self.lblResponsable.setText(QCoreApplication.translate("ventanaPrincipal", u"Responsable: ", None))
        self.lblFecha.setText(QCoreApplication.translate("ventanaPrincipal", u"Fecha: ", None))
        self.lblLSE.setText(QCoreApplication.translate("ventanaPrincipal", u"LSE: ", None))
        self.checkReporte.setText(QCoreApplication.translate("ventanaPrincipal", u"Crear Excel", None))
        self.lblDatos.setText(QCoreApplication.translate("ventanaPrincipal", u"Raw data: ", None))
        self.checkAutomatico.setText(QCoreApplication.translate("ventanaPrincipal", u"Segun configuracion actual", None))
        self.btnEjecutar.setText(QCoreApplication.translate("ventanaPrincipal", u"Ejecutar", None))
        self.lblArchivos.setText(QCoreApplication.translate("ventanaPrincipal", u"Archivos de Entrada: ", None))
        self.lblUnidades.setText(QCoreApplication.translate("ventanaPrincipal", u"Unidades de medicion: ", None))
        self.btnCarpeta.setText(QCoreApplication.translate("ventanaPrincipal", u"...", None))
        self.lblCaracteristica.setText(QCoreApplication.translate("ventanaPrincipal", u"Caracteristica: ", None))
        self.lblProveedor.setText(QCoreApplication.translate("ventanaPrincipal", u"Proveedor: ", None))
        self.lblEstatus.setText("")
        self.btnGuardar.setText(QCoreApplication.translate("ventanaPrincipal", u"Guardar", None))
        self.tabWidget2.setTabText(self.tabWidget2.indexOf(self.tabResultados), QCoreApplication.translate("ventanaPrincipal", u"Resultados", None))
        self.tabWidget2.setTabText(self.tabWidget2.indexOf(self.tabPromedios), QCoreApplication.translate("ventanaPrincipal", u"Promedios", None))
        self.tabWidget2.setTabText(self.tabWidget2.indexOf(self.tabDatos), QCoreApplication.translate("ventanaPrincipal", u"Datos", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabPrincipal), QCoreApplication.translate("ventanaPrincipal", u"Principal", None))
        self.titulo_2.setText(QCoreApplication.translate("ventanaPrincipal", u"Menu de configuracion", None))
        self.lblCategorias.setText(QCoreApplication.translate("ventanaPrincipal", u"Cantidad de categorias: ", None))
        self.lblDecimales.setText(QCoreApplication.translate("ventanaPrincipal", u"Cantidad de decimales: ", None))
        self.lblMuestras.setText(QCoreApplication.translate("ventanaPrincipal", u"Muestras por archivo: ", None))
        self.btnResetearConfiguracion.setText(QCoreApplication.translate("ventanaPrincipal", u"Resetear", None))
        self.btnGuardarConfiguracion.setText(QCoreApplication.translate("ventanaPrincipal", u"Guardar", None))
        self.btnAplicarConfiguracion.setText(QCoreApplication.translate("ventanaPrincipal", u"Aplicar", None))
        self.lblLogo.setText(QCoreApplication.translate("ventanaPrincipal", u"Logo: ", None))
        self.btnLogo.setText(QCoreApplication.translate("ventanaPrincipal", u"...", None))
        self.lblPestana.setText(QCoreApplication.translate("ventanaPrincipal", u"Pesta\u00f1a: ", None))
        self.checkCampana.setText(QCoreApplication.translate("ventanaPrincipal", u"Agregar Grafica de Campana", None))
        self.check3Sigma.setText(QCoreApplication.translate("ventanaPrincipal", u"Agregar 3-Sigma", None))
        self.lblFilaCaracteristica.setText(QCoreApplication.translate("ventanaPrincipal", u"Fila: ", None))
        self.lblColumnaCaracteristica.setText(QCoreApplication.translate("ventanaPrincipal", u"Columna: ", None))
        self.lblColumnaProveedor.setText(QCoreApplication.translate("ventanaPrincipal", u"Columna: ", None))
        self.lblFilaProveedor.setText(QCoreApplication.translate("ventanaPrincipal", u"Fila: ", None))
        self.lblCaracteristica_2.setText(QCoreApplication.translate("ventanaPrincipal", u"Caracteristica", None))
        self.lbl3Sigma.setText(QCoreApplication.translate("ventanaPrincipal", u"Especificaciones", None))
        self.lblFilaDatos.setText(QCoreApplication.translate("ventanaPrincipal", u"Fila: ", None))
        self.lblProveedor_2.setText(QCoreApplication.translate("ventanaPrincipal", u"Proveedor", None))
        self.lblColumnaNumero.setText(QCoreApplication.translate("ventanaPrincipal", u"Columna: ", None))
        self.lblColumnaDatos.setText(QCoreApplication.translate("ventanaPrincipal", u"Columna: ", None))
        self.lblNumero_2.setText(QCoreApplication.translate("ventanaPrincipal", u"Numero de Parte", None))
        self.lblDatos_2.setText(QCoreApplication.translate("ventanaPrincipal", u"Datos", None))
        self.lblFilaNumero.setText(QCoreApplication.translate("ventanaPrincipal", u"Fila: ", None))
        self.lblColumnaEspecificaciones.setText(QCoreApplication.translate("ventanaPrincipal", u"Columna: ", None))
        self.lblFilaEspecificaciones.setText(QCoreApplication.translate("ventanaPrincipal", u"Fila: ", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabConfiguracion), QCoreApplication.translate("ventanaPrincipal", u"Configuracion", None))
    # retranslateUi