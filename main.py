from lib.MainWindow import MainWindow
from PyQt6.QtWidgets import QApplication, QWidget


app = QApplication([])
window = MainWindow()


window.show()
app.exec()