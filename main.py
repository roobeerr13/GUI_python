from controlador import TorresDeHanoi
import sys
from PyQt6.QtWidgets import QApplication
from modelo import guardar_estado

# Este es el punto de entrada de la aplicación
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = TorresDeHanoi()
    ventana.show()
    guardar_estado(ventana)
    sys.exit(app.exec())