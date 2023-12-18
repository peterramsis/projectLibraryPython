import datetime
import sys
import time
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
        self.getAll(self.comboBox_5,  "category")
        self.getAll(self.comboBox_2,  "category")
        self.getAll(self.comboBox_3,  "category")
        self.getAll(self.comboBox_4,  "category")
        self.getAll(self.comboBox_13, "author")
        self.getAll(self.comboBox_14, "author")
        self.getAll(self.comboBox_15, "branch")
        self.getAll(self.comboBox_16, "publisher")
        # add category
        self.pushButton_9.clicked.connect(self.add_book)

        self.pushButton_13.clicked.connect(self.add_client)

        self.getBooks()
        self.getClient()
        self.pushButton_15.clicked.connect(self.searchByClient)
        self.pushButton_16.clicked.connect(self.update_clinet)
        self.pushButton_14.clicked.connect(self.delete_client)




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
        self.getAll(self.comboBox_5, "category")

    def add_book(self):
        try:
            title = self.lineEdit_3.text()
            description = self.lineEdit_2.text()
            price = self.lineEdit_4.text()
            code = self.lineEdit_7.text()
            part = self.lineEdit_6.text()
            barcode = self.lineEdit_8.text()
            categoryText = self.comboBox_3.currentText()
            branchText = self.comboBox_15.currentText()
            authorText = self.comboBox_13.currentText()
            publisherText = self.comboBox_16.currentText()
            status = self.lineEdit_52.text()

            date = time.strftime('%Y-%m-%d %H:%M:%S')

            self.cur.execute('''select id from category where name = %s ''' , (categoryText))
            category= self.cur.fetchone()[0]

            self.cur.execute('''select id from branch where name = %s ''', (branchText))
            branch = self.cur.fetchone()[0]

            self.cur.execute('''select id from author where name = %s ''', (authorText))
            author = self.cur.fetchone()[0]

            self.cur.execute('''select id from publisher where name = %s ''', (publisherText))
            publisher = self.cur.fetchone()[0]


            self.cur.execute('''Insert into book(title , description , category_id , code , barcode , part_order , publisher_id , price, author_id ,branch_id,status,date) Values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)''',(title, description, category , code,barcode ,part ,publisher,price ,author,branch,status,date))
            self.db.commit()
            print("book added")



        except:
            print("error")


    def add_client(self):
        name = self.lineEdit_15.text()
        mail = self.lineEdit_16.text()
        phone = self.lineEdit_17.text()
        national_id = self.lineEdit_22.text()
        date = time.strftime('%Y-%m-%d %H:%M:%S')
        self.cur.execute('''Insert into client(name , mail, phone, date , national_id) Values(%s,%s,%s,%s,%s)''', (name , mail , phone , date , national_id))
        self.db.commit()
        print("client added")
        self.getClient()



    def getAll(self,comboBox , table):
        comboBox.clear()
        comboBox.addItem("---select---")
        self.cur.execute('select name from {0}'.format(table))
        data = self.cur.fetchall()
        for item in data:
            comboBox.addItem(str(item[0]))

    def getBooks(self):
        self.cur.execute('select code,title,description,author_id,category_id,price from book')
        self.tableWidget_2.insertRow(0)
        data = self.cur.fetchall()
        for row, form in enumerate(data):
            self.tableWidget_2.insertRow(row)
            for col, item in enumerate(form):
                self.tableWidget_2.setItem(row, col, QTableWidgetItem(str(item)))
                col += 1
        row_position = self.tableWidget_2.rowCount()
    def searchByClient(self):
       print("click")
       search =  self.lineEdit_26.text()
       self.cur.execute('''select * from client where name = %s''' , (search))
       data = self.cur.fetchone()
       print(data)
       self.lineEdit_24.setText(data[1])
       self.lineEdit_21.setText(data[2])
       self.lineEdit_23.setText(data[3])
       self.lineEdit_25.setText(str(data[5]))




    def getClient(self):
        self.cur.execute('select name,mail,phone,national_id from client')
        self.tableWidget_3.insertRow(0)
        data = self.cur.fetchall()
        for row, form in enumerate(data):
            self.tableWidget_3.insertRow(row)
            for col, item in enumerate(form):
                self.tableWidget_3.setItem(row, col, QTableWidgetItem(str(item)))
                col += 1
        row_position = self.tableWidget_3.rowCount()
        print(row_position)

    def update_clinet(self):
        search =  self.lineEdit_26.text()
        name = self.lineEdit_24.text()
        mail = self.lineEdit_21.text()
        phone = self.lineEdit_23.text()
        national_id =  self.lineEdit_25.text()

        self.cur.execute('''update client set name = %s , mail = %s , phone = %s , national_id = %s  where name = %s''' , (name , mail , phone , national_id,search))
        self.db.commit()
        print("update client")
        self.statusBar().showMessage("Update client")
        QMessageBox.information(self, "success","Update client")

    def delete_client(self):
        search = self.lineEdit_26.text()
        self.cur.execute('''delete from client where name = %s''',(search))
        self.db.commit()
        print("delete client")

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