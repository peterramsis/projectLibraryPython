import sys

import pymysql
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
        self.db_connect()
        self.handel_buttons()
        self.ui_changes()
    def ui_changes(self):
        self.tabWidget.tabBar().setVisible(0)

    def db_connect(self):
     self.db =pymysql.Connect(db='library', user='root', password='')
     self.cur = self.db.cursor()
     print("Connection accepted")

    def handel_buttons(self):
        self.pushButton.clicked.connect(self.open_today_tab)
        self.pushButton_2.clicked.connect(self.open_book_tab)
        self.pushButton_3.clicked.connect(self.open_client_tab)
        self.pushButton_4.clicked.connect(self.open_dashboard_tab)
        self.pushButton_5.clicked.connect(self.open_history_tab)
        self.pushButton_6.clicked.connect(self.open_report_tab)
        self.pushButton_7.clicked.connect(self.open_settings_tab)
        #add branch
        self.pushButton_23.clicked.connect(self.add_branch)
        #add publisher
        self.pushButton_24.clicked.connect(self.add_publisher)
        #add author
        self.pushButton_25.clicked.connect(self.add_author)
        #add category
        self.pushButton_26.clicked.connect(self.add_category)
        self.getAll(self.comboBox_5, "category")
        self.getAll(self.comboBox_2, "category")
        self.getAll(self.comboBox_3, "category")
        self.getAll(self.comboBox_4, "category")
        self.getAll(self.comboBox_13, "author")
        self.getAll(self.comboBox_14, "author")





    def add_client(self):
        pass
    def add_branch(self):
        name= self.lineEdit_36.text()
        code= self.lineEdit_37.text()
        location = self.lineEdit_38.text()
        self.cur.execute('''Insert into branch(name, code , location) Values(%s,%s,%s)''',(name,code,location))
        self.db.commit()
        print("Branch added")
    def add_publisher(self):
        name = self.lineEdit_39.text()
        location = self.lineEdit_40.text()
        self.cur.execute('''Insert into publisher(name , location) Values(%s,%s)''',(name,location))
        self.db.commit()
        print("Publisher added")
    def add_author(self):
        name = self.lineEdit_41.text()
        location = self.lineEdit_42.text()
        self.cur.execute('''Insert into author(name , location) Values(%s,%s)''', (name, location))
        self.db.commit()
        print("author added")

    def add_category(self):
        name = self.lineEdit_43.text()
        parentText = self.comboBox_5.currentText()
        self.cur.execute('''select id from category where name = %s ''' , (parentText))
        if parentText == "---select---" :
            parent = 0
        else:
            parent= self.cur.fetchone()[0]
        print(parent)
        self.cur.execute('''Insert into category(name , parent_category) Values(%s,%s)''', (name, parent))
        self.db.commit()
        print("category added")
        self.getAllCategory()


    def getAll(self,comboBox , table):
        comboBox.clear()
        comboBox.addItem("---select---")
        self.cur.execute('select name from {0}'.format(table))
        data = self.cur.fetchall()
        for item in data:
            comboBox.addItem(str(item[0]))



    def open_today_tab(self):
        self.tabWidget.setCurrentIndex(2)
    def open_book_tab(self):
       self.tabWidget.setCurrentIndex(3)
       self.tabWidget_2.setCurrentIndex(0)
    def open_client_tab(self):
       self.tabWidget.setCurrentIndex(4)
       self.tabWidget_3.setCurrentIndex(0)
    def open_dashboard_tab(self):
       self.tabWidget.setCurrentIndex(5)
    def open_history_tab(self):
       self.tabWidget.setCurrentIndex(6)

    def open_report_tab(self):
        self.tabWidget.setCurrentIndex(7)
        self.tabWidget_5.setCurrentIndex(0)

    def open_settings_tab(self):
        self.tabWidget.setCurrentIndex(8)
        self.tabWidget_4.setCurrentIndex(0)

def main():
    app = QApplication(sys.argv)
    windows = Main()
    windows.show()
    app.exec_()


main()