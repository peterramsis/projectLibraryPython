import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType #error appears here
import sys
import os
from os import path

MainUI,_ = loadUiType("main.ui")
class Main:
    def __init__(self,parent=None):
        super(Main, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)


def main():
    app = QApplication(sys.argv)
    windows = Main()
    windows.show()
    app.exec_()
