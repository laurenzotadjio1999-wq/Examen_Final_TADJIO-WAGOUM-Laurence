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

# lbl_Valider_opération
lbl_valider = QLabel(fen)
grid.addWidget(lbl_valider, 1, 1)

# btn_Valider l'opération
btn_calculer = QPushButton("Valider l'opération")
btn_calculer.clicked.connect()
grid.addWidget(btn_calculer, 3, 1)


#bouton2
btn_save = QPushButton(fen)
btn_save.setText("Sauvegarder le résultat")
grid.addWidget(btn_save, 4, 0)
#btn_save.clicked.connect()
#bouton3
btn3_calcul = QPushButton(fen)
btn3_calcul.setText("Charger résultat")
grid.addWidget(btn3_calcul, 4, 4)
#btn3_calcul.clicked.connect()