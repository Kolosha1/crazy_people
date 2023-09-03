from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout

app = QApplication([])

main_win = QWidget()
main_win.setWindowTitle("Визначник переморжця")
main_win.resize(400,250)

text = QLabel ("Натисни, щоб дізнатися переможця")
result = QLabel("?")
btn = QPushButton("Згенерувати")

line = QVBoxLayout()
line.addWidget(text)
line.addWidget(result)
line.addWidget(btn)
main_win.setLayout(line)

main_win.show()
app.exec_()