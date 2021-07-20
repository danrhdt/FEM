#7/20/2021-Python-vscode
#Author: DAN-HDT
#-----------------------
#Open QtDesigner: python -u .\env\Lib\site-packages\qt5_applications\Qt\designer.exe
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
class MainWindow(QWindow):
    def __init__(self):
        QWindow.__init__(self)
        self.setTitle("Window")
        self.resize(800, 800)
app = QApplication(sys.argv)
screen = MainWindow()
screen.show()
sys.exit(app.exec_())
