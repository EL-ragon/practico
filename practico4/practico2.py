import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QTextEdit, QAction, QFileDialog,
    QMessageBox, QToolBar, QInputDialog, QFontDialog, QMenu
)
from PyQt5.QtGui import QKeySequence, QFont
from PyQt5.QtPrintSupport import QPrinter, QPrintPreviewDialog


class WordChafa(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("WordChafa Avanzado")
        self.setGeometry(180, 100, 900, 600)

        self.editor = QTextEdit()
        self.setCentralWidget(self.editor)
        self.editor.setPlaceholderText("Escribe aquí tu texto...")
        self.archivos_recientes = []

        self.crear_acciones()
        self.crear_menus()
        self.crear_toolbar()
        self.crear_barra_estado()

    def crear_acciones(self):
        self.accion_nuevo = QAction("&Nuevo", self)
        self.accion_nuevo.setShortcut(QKeySequence.New)
        self.accion_nuevo.triggered.connect(self.nuevo_archivo)

        self.accion_abrir = QAction("&Abrir", self)
        self.accion_abrir.setShortcut(QKeySequence.Open)
        self.accion_abrir.triggered.connect(self.abrir_archivo)

        self.accion_guardar = QAction("&Guardar", self)
        self.accion_guardar.setShortcut(QKeySequence.Save)
        self.accion_guardar.triggered.connect(self.guardar_archivo)

        self.accion_vista_previa = QAction("Vista previa", self)
        self.accion_vista_previa.triggered.connect(self.vista_previa_impresion)

        self.accion_salir = QAction("&Salir", self)
        self.accion_salir.setShortcut("Ctrl+Q")
        self.accion_salir.triggered.connect(self.salir)

        self.accion_cortar = QAction("&Cortar", self)
        self.accion_cortar.setShortcut(QKeySequence.Cut)
        self.accion_cortar.triggered.connect(self.editor.cut)

        self.accion_copiar = QAction("&Copiar", self)
        self.accion_copiar.setShortcut(QKeySequence.Copy)
        self.accion_copiar.triggered.connect(self.editor.copy)

        self.accion_pegar = QAction("&Pegar", self)
        self.accion_pegar.setShortcut(QKeySequence.Paste)
        self.accion_pegar.triggered.connect(self.editor.paste)

        self.accion_buscar_reemplazar = QAction("Buscar y Reemplazar", self)
        self.accion_buscar_reemplazar.triggered.connect(self.buscar_reemplazar)

        self.accion_negrita = QAction("Negrita", self)
        self.accion_negrita.triggered.connect(self.poner_negrita)

        self.accion_cursiva = QAction("Cursiva", self)
        self.accion_cursiva.triggered.connect(self.poner_cursiva)

        self.accion_fuente = QAction("Fuente...", self)
        self.accion_fuente.triggered.connect(self.cambiar_fuente)

        self.accion_acerca = QAction("&Acerca de", self)
        self.accion_acerca.triggered.connect(self.acerca_de)

    def crear_menus(self):
        menubar = self.menuBar()

        menu_archivo = menubar.addMenu("&Archivo")
        menu_archivo.addAction(self.accion_nuevo)
        menu_archivo.addAction(self.accion_abrir)
        menu_archivo.addAction(self.accion_guardar)
        menu_archivo.addAction(self.accion_vista_previa)
        menu_archivo.addSeparator()

        self.menu_recientes = QMenu("Archivos recientes", self)
        menu_archivo.addMenu(self.menu_recientes)
        menu_archivo.addSeparator()
        menu_archivo.addAction(self.accion_salir)

        menu_editar = menubar.addMenu("&Editar")
        menu_editar.addAction(self.accion_cortar)
        menu_editar.addAction(self.accion_copiar)
        menu_editar.addAction(self.accion_pegar)
        menu_editar.addSeparator()
        menu_editar.addAction(self.accion_buscar_reemplazar)

        menu_formato = menubar.addMenu("&Formato")
        menu_formato.addAction(self.accion_negrita)
        menu_formato.addAction(self.accion_cursiva)
        menu_formato.addAction(self.accion_fuente)

        menu_ayuda = menubar.addMenu("&Ayuda")
        menu_ayuda.addAction(self.accion_acerca)

    def crear_toolbar(self):
        toolbar = QToolBar("Barra de herramientas")
        self.addToolBar(toolbar)
        toolbar.addAction(self.accion_nuevo)
        toolbar.addAction(self.accion_abrir)
        toolbar.addAction(self.accion_guardar)
        toolbar.addSeparator()
        toolbar.addAction(self.accion_cortar)
        toolbar.addAction(self.accion_copiar)
        toolbar.addAction(self.accion_pegar)
        toolbar.addSeparator()
        toolbar.addAction(self.accion_negrita)
        toolbar.addAction(self.accion_cursiva)

    def crear_barra_estado(self):
        self.statusBar().showMessage("Listo")

    def nuevo_archivo(self):
        self.editor.clear()
        self.statusBar().showMessage("Nuevo archivo creado", 3000)

    def abrir_archivo(self):
        ruta, _ = QFileDialog.getOpenFileName(self, "Abrir archivo", "", "Archivos de texto (*.txt)")
        if ruta:
            try:
                with open(ruta, "r", encoding="utf-8") as f:
                    contenido = f.read()
                    self.editor.setPlainText(contenido)
                    self.statusBar().showMessage(f"Archivo '{ruta}' abierto", 3000)
                    self.agregar_archivo_reciente(ruta)
            except Exception as e:
                QMessageBox.warning(self, "Error", f"No se pudo abrir el archivo:\n{e}")
                self.statusBar().showMessage("Error al abrir archivo", 3000)

    def guardar_archivo(self):
        ruta, _ = QFileDialog.getSaveFileName(self, "Guardar archivo", "", "Archivos de texto (*.txt)")
        if ruta:
            try:
                with open(ruta, "w", encoding="utf-8") as f:
                    f.write(self.editor.toPlainText())
                    self.statusBar().showMessage(f"Archivo guardado en '{ruta}'", 3000)
                    self.agregar_archivo_reciente(ruta)
            except Exception as e:
                QMessageBox.warning(self, "Error", f"No se pudo guardar el archivo:\n{e}")
                self.statusBar().showMessage("Error al guardar archivo", 3000)

    def agregar_archivo_reciente(self, ruta):
        if ruta in self.archivos_recientes:
            self.archivos_recientes.remove(ruta)
        self.archivos_recientes.insert(0, ruta)
        self.archivos_recientes = self.archivos_recientes[:5]
        self.menu_recientes.clear()
        for archivo in self.archivos_recientes:
            action = QAction(archivo, self)
            action.triggered.connect(lambda checked, path=archivo: self.abrir_reciente(path))
            self.menu_recientes.addAction(action)

    def abrir_reciente(self, ruta):
        try:
            with open(ruta, "r", encoding="utf-8") as f:
                contenido = f.read()
                self.editor.setPlainText(contenido)
                self.statusBar().showMessage(f"Archivo '{ruta}' abierto", 3000)
        except Exception as e:
            QMessageBox.warning(self, "Error", f"No se pudo abrir el archivo:\n{e}")

    def buscar_reemplazar(self):
        texto_buscar, ok = QInputDialog.getText(self, "Buscar", "Texto a buscar:")
        if ok and texto_buscar:
            texto_reemplazar, ok2 = QInputDialog.getText(self, "Reemplazar", "Reemplazar por:")
            if ok2:
                contenido = self.editor.toPlainText()
                nuevo_contenido = contenido.replace(texto_buscar, texto_reemplazar)
                self.editor.setPlainText(nuevo_contenido)
                self.statusBar().showMessage(f"Se reemplazó '{texto_buscar}' por '{texto_reemplazar}'", 3000)

    def poner_negrita(self):
        fmt = self.editor.currentCharFormat()
        fmt.setFontWeight(75 if fmt.fontWeight() != 75 else 50)
        self.editor.setCurrentCharFormat(fmt)

    def poner_cursiva(self):
        fmt = self.editor.currentCharFormat()
        fmt.setFontItalic(not fmt.fontItalic())
        self.editor.setCurrentCharFormat(fmt)

    def cambiar_fuente(self):
        fuente, ok = QFontDialog.getFont()
        if ok:
            self.editor.setFont(fuente)

    def vista_previa_impresion(self):
        printer = QPrinter(QPrinter.HighResolution)
        preview = QPrintPreviewDialog(printer, self)
        preview.paintRequested.connect(self.editor.print_)
        preview.exec_()

    def acerca_de(self):
        QMessageBox.information(
            self,
            "Acerca de",
            "WordChafa v1.0\n\nCreado con PyQt5\nPara aprender desarrollo de interfaces."
        )

    def salir(self):
        respuesta = QMessageBox.question(
            self,
            "Salir",
            "¿Desea guardar los cambios antes de salir?",
            QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel
        )

        if respuesta == QMessageBox.Yes:
            self.guardar_archivo()
            self.close()
        elif respuesta == QMessageBox.No:
            self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    editor = WordChafa()
    editor.show()
    sys.exit(app.exec())
