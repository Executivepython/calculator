from PyQt5 import *
from PyQt5.QtWidgets import *

app = QApplication([])

main_win = QWidget()
txtbox = QLineEdit()
txtbox2 = QLineEdit()
output = QLabel()
add = QPushButton("+")
sub = QPushButton("-")
multi = QPushButton("×")
div = QPushButton("÷")

VB = QVBoxLayout()
HB = QHBoxLayout()

VB.addWidget(txtbox)
VB.addWidget(txtbox2)
VB.addWidget(output)
VB.addLayout(HB)

HB.addWidget(add)
HB.addWidget(sub)
HB.addWidget(multi)
HB.addWidget(div)

def addition():
    try:
        num1 = float(txtbox.text())
        num2 = float(txtbox2.text())
        ans = num1 + num2
        output.setText(f"Result: {ans}")
    except ValueError:
        output.setText("Please enter valid numbers.")

def subtraction():
    try:
        num1 = float(txtbox.text())
        num2 = float(txtbox2.text())
        ans = num1 - num2
        output.setText(f"Result: {ans}")
    except ValueError:
        output.setText("Please enter valid numbers.")

def multiplication():
    try:
        num1 = float(txtbox.text())
        num2 = float(txtbox2.text())
        ans = num1 * num2
        output.setText(f"Result: {ans}")
    except ValueError:
        output.setText("Please enter valid numbers.")

def division():
    try:
        num1 = float(txtbox.text())
        num2 = float(txtbox2.text())
        if num2 == 0:
            output.setText("Division by zero is not allowed.")
        else:
            ans = num1 / num2
            output.setText(f"Result: {ans}")
    except ValueError:
        output.setText("Please enter valid numbers.")

add.clicked.connect(addition)
sub.clicked.connect(subtraction)
multi.clicked.connect(multiplication)
div.clicked.connect(division)

main_win.setLayout(VB)
main_win.show()
#hi
app.exec()
