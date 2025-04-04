from modelo import *


if __name__ == "__main__":
    app = QApplication(sys.argv)

    w = AppContador()
    w.show()

    sys.exit(app.exec())