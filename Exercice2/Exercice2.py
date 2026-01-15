from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QLineEdit, QLabel, QPushButton

#Création de l'application et de la fenêtre
app = QApplication([])
fen = QWidget()

# grid layout
grid = QGridLayout()
fen.setLayout(grid)


# lbl1
lbl_input1 = QLabel("Entrer la valeur de N:")
grid.addWidget(lbl_input1, 0, 0)
# input1
input1 = QLineEdit(fen)
grid.addWidget(input1, 0, 1)

# lbl2
lbl_input2 = QLabel("Voici le Double: ")
grid.addWidget(lbl_input2, 1, 0)
# input2
input2 = QLineEdit(fen)
grid.addWidget(input2, 1, 1)