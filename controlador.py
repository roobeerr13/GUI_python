import sys
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QSpinBox, QApplication


class TorresDeHanoi(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Torres de Hanoi")
        self.setGeometry(100, 100, 400, 300)

        self.layout_principal = QVBoxLayout()

        # Selector de número de discos
        self.layout_selector = QHBoxLayout()
        self.label_selector = QLabel("Número de discos:")
        self.spin_box = QSpinBox()
        self.spin_box.setMinimum(1)
        self.spin_box.setMaximum(10)
        self.spin_box.setValue(3)
        self.boton_resolver = QPushButton("Resolver")
        self.boton_resolver.clicked.connect(self.resolver_hanoi)

        self.layout_selector.addWidget(self.label_selector)
        self.layout_selector.addWidget(self.spin_box)
        self.layout_selector.addWidget(self.boton_resolver)

        # Área de salida
        self.label_resultado = QLabel("")
        self.label_resultado.setStyleSheet("font-size: 16px;")

        self.layout_principal.addLayout(self.layout_selector)
        self.layout_principal.addWidget(self.label_resultado)

        self.setLayout(self.layout_principal)

    def resolver_hanoi(self):
        num_discos = self.spin_box.value()
        self.label_resultado.setText("Resolviendo...")
        pasos = []
        self.hanoi(num_discos, 'A', 'C', 'B', pasos)
        resultado = "\n".join(pasos)
        self.label_resultado.setText(resultado)

    def hanoi(self, n, origen, destino, auxiliar, pasos):
        if n == 1:
            pasos.append(f"Mover disco de {origen} a {destino}")
        else:
            self.hanoi(n - 1, origen, auxiliar, destino, pasos)
            pasos.append(f"Mover disco de {origen} a {destino}")
            self.hanoi(n - 1, auxiliar, destino, origen, pasos)