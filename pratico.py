import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QGridLayout, QRadioButton, QButtonGroup
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QComboBox
from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtWidgets import QPushButton, QMessageBox

class Ventana(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Registro de Usuario")
        self.setGeometry(100, 100, 400, 300)

        layout = QGridLayout()
        self.setLayout(layout)

        titulo = QLabel("Formulario de Refistro")
        titulo.setAlignment(Qt.AlignCenter)
        titulo.setStyleSheet("font-size: 20px; font-weight: bold;")

        layout.addWidget(titulo,0,0,1,2)

        nombre_label = QLabel("Nombre:")
        self.nombre_input = QLineEdit()
        layout.addWidget(nombre_label,1,0)
        layout.addWidget(self.nombre_input,1,1)

        self.email_label = QLabel("Email:")
        self.email_input = QLineEdit()
        layout.addWidget(self.email_label,2,0)
        layout.addWidget(self.email_input,2,1)

        password_label = QLabel("Contraseña:")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(password_label,3,0)
        layout.addWidget(self.password_input,3,1)

        masculino_radio = QRadioButton("Masculino")
        femenino_radio = QRadioButton("Femenino")
        genero_group = QButtonGroup(self)
        genero_group.addButton(masculino_radio)
        genero_group.addButton(femenino_radio)
        layout.addWidget(masculino_radio,4,0)
        layout.addWidget(femenino_radio,4,1)

        pais_label = QLabel("Pais:")
        self.pais_combo = QComboBox()
        self.pais_combo.addItems(["Argentina","Brazil","Chile","Mexico","España","Rusia"])
        layout.addWidget(pais_label,5,0)
        layout.addWidget(self.pais_combo,5,1)

        self.terminos_checkbox = QCheckBox("Acepto los terminos y condiciones")
        layout.addWidget(self.terminos_checkbox,6,0,1,2)

        self.boton_registro = QPushButton("Registrarte")
        self.boton_registro.setStyleSheet(
            """
            QPushBotton{
            background-color: #3498db;
            color: white;
            font-size: 16px;
            padding: 8px;
            border-radius: 5px
            }
            QPushBotton{
            background-color: #2980b9;
            }
            """
        )
        self.boton_registro.clicked.connect(self.validar_formulario)
        layout.addWidget(self.boton_registro,7,0,1,2)

    def validar_formulario(self):
        nombre = self.nombre_input.text()
        email = self.email_input.text()
        contraseña = self.password_input.text()
        pais = self.pais_combo.currentText()
        acepta = self.terminos_checkbox.isChecked()

        if not nombre or not email or not contraseña:
            QMessageBox.warning(self,"Error","Por favor completa todos los campos.")
            return
        if not acepta:
            QMessageBox.warning(self,"Error","Debes acaptar los terminos y condiciones.")
            return
        QMessageBox.information(self,"Exito",f"¡Registro exitoso!\nBienvenido, {nombre} de {pais}.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec_())