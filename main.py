import sys

from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import PyQt5.uic
import sys
import os
from os import path

MainUI,_ = uic.loadUiType("project.ui")
class Main(QMainWindow,MainUI):
    def __init__(self,parent=None):
        super(Main, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)


def main():
    app = QApplication(sys.argv)
    windows = Main()
    windows.show()
    app.exec_()


main()