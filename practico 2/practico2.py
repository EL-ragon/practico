import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QGridLayout, QComboBox, QDateEdit, QRadioButton, QButtonGroup, QSpinBox, QCheckBox, QPushButton, QMessageBox, QVBoxLayout, QSpacerItem, QSizePolicy
from PyQt5.QtCore import Qt, QDate

class Ventana(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Compra de Pasaje Aéreo")
        self.setGeometry(100, 100, 500, 500)
        self.setStyleSheet("background-color: #f0f4f7;")

        main_layout = QVBoxLayout()
        self.setLayout(main_layout)
        main_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        layout = QGridLayout()
        main_layout.addLayout(layout)
        main_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        titulo = QLabel("Formulario de Compra")
        titulo.setAlignment(Qt.AlignCenter)
        titulo.setStyleSheet("font-size: 22px; font-weight: bold; color: #2c3e50;")
        layout.addWidget(titulo, 0, 0, 1, 2)

        nombre_label = QLabel("Nombre:")
        self.nombre_input = QLineEdit()
        self.nombre_input.setStyleSheet("padding: 5px; font-size: 14px;")
        layout.addWidget(nombre_label, 1, 0)
        layout.addWidget(self.nombre_input, 1, 1)

        apellido_label = QLabel("Apellido:")
        self.apellido_input = QLineEdit()
        self.apellido_input.setStyleSheet("padding: 5px; font-size: 14px;")
        layout.addWidget(apellido_label, 2, 0)
        layout.addWidget(self.apellido_input, 2, 1)

        dni_label = QLabel("DNI:")
        self.dni_input = QLineEdit()
        self.dni_input.setStyleSheet("padding: 5px; font-size: 14px;")
        layout.addWidget(dni_label, 3, 0)
        layout.addWidget(self.dni_input, 3, 1)

        origen_label = QLabel("Origen:")
        self.origen_combo = QComboBox()
        self.origen_combo.addItems(["Buenos Aires", "Santiago", "Montevideo"])
        self.origen_combo.setStyleSheet("padding: 5px; font-size: 14px;")
        layout.addWidget(origen_label, 4, 0)
        layout.addWidget(self.origen_combo, 4, 1)

        destino_label = QLabel("Destino:")
        self.destino_combo = QComboBox()
        self.destino_combo.addItems(["Madrid", "Miami", "Londres"])
        self.destino_combo.setStyleSheet("padding: 5px; font-size: 14px;")
        layout.addWidget(destino_label, 5, 0)
        layout.addWidget(self.destino_combo, 5, 1)

        fecha_label = QLabel("Fecha de vuelo:")
        self.fecha_vuelo = QDateEdit()
        self.fecha_vuelo.setDate(QDate.currentDate())
        self.fecha_vuelo.setCalendarPopup(True)
        layout.addWidget(fecha_label, 6, 0)
        layout.addWidget(self.fecha_vuelo, 6, 1)

        turista_radio = QRadioButton("Turista")
        ejecutiva_radio = QRadioButton("Ejecutiva")
        self.clase_group = QButtonGroup(self)
        self.clase_group.addButton(turista_radio)
        self.clase_group.addButton(ejecutiva_radio)
        layout.addWidget(turista_radio, 7, 0)
        layout.addWidget(ejecutiva_radio, 7, 1)

        cant_label = QLabel("Cantidad de pasajeros:")
        self.cant_spin = QSpinBox()
        self.cant_spin.setRange(1, 10)
        self.cant_spin.setStyleSheet("padding: 5px; font-size: 14px;")
        layout.addWidget(cant_label, 8, 0)
        layout.addWidget(self.cant_spin, 8, 1)

        self.boton_comprar = QPushButton("Comprar")
        self.boton_comprar.setStyleSheet(
            "background-color: #27ae60; color: white; font-size: 16px; padding: 8px; border-radius:5px;"
        )
        self.boton_comprar.clicked.connect(self.mostrar_resumen)
        layout.addWidget(self.boton_comprar, 9, 0, 1, 2)

    def mostrar_resumen(self):
        nombre = self.nombre_input.text()
        apellido = self.apellido_input.text()
        dni = self.dni_input.text()
        origen = self.origen_combo.currentText()
        destino = self.destino_combo.currentText()
        fecha = self.fecha_vuelo.date().toString("dd/MM/yyyy")

        clase = ""
        if self.clase_group.checkedButton():
            clase = self.clase_group.checkedButton().text()

        pasajeros = self.cant_spin.value()

        resumen = (
            f"Nombre: {nombre} {apellido}\n"
            f"DNI: {dni}\n"
            f"Origen: {origen}\n"
            f"Destino: {destino}\n"
            f"Fecha: {fecha}\n"
            f"Clase: {clase}\n"
            f"Pasajeros: {pasajeros}"
        )

        QMessageBox.information(self, "Resumen de Compra", resumen)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec_())
