# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainPage.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SecondWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(410, 310, 93, 28))
        self.pushButton.setObjectName("pushButton")

    def lines(self, MainWindow):

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 150, 81, 31))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(292, 150, 151, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(150, 200, 81, 31))
        self.label_2.setObjectName("label_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(290, 200, 151, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        ###################################################Check#######################################
        # self.pushButton.clicked.connect(self.loginCheck)
        ###################################################Check#######################################
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Confirm"))
        self.label.setText(_translate("MainWindow", "Username"))
        self.label_2.setText(_translate("MainWindow", "Password"))
    ##################################################Login#####################################################
    def loginAdmin(self):

        client = MongoClient(MONGO_URI)

        employee_Db = client["database"]
        employee_Collection = employee_Db["employee"]

        admin_Db = client["Secret"]
        admin_Collection = admin_Db["admin"]

        for datas in admin_Collection.find():
            if datas.get("username") == self.lineEdit.text() and datas.get("password") == self.lineEdit_3.text():
                print("Login Confirmed")


    def initializer(self):
        if __name__ == "__main__":
            import sys
            app = QtWidgets.QApplication(sys.argv)
            MainWindow = QtWidgets.QMainWindow()
            ui = Ui_MainWindow()
            ui.setupUi(MainWindow)
            MainWindow.show()
            sys.exit(app.exec_())



class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Age = QtWidgets.QLabel(self.centralwidget)
        self.Age.setGeometry(QtCore.QRect(210, 290, 61, 20))
        self.Age.setObjectName("Age")
        self.Title = QtWidgets.QLabel(self.centralwidget)
        self.Title.setGeometry(QtCore.QRect(210, 360, 61, 20))
        self.Title.setObjectName("Title")
        self.Surname = QtWidgets.QLabel(self.centralwidget)
        self.Surname.setGeometry(QtCore.QRect(210, 220, 81, 20))
        self.Surname.setObjectName("Surname")
        self.Name = QtWidgets.QLabel(self.centralwidget)
        self.Name.setGeometry(QtCore.QRect(210, 150, 81, 20))
        self.Name.setObjectName("Name")
        self.nameBlank = QtWidgets.QLineEdit(self.centralwidget)
        self.nameBlank.setGeometry(QtCore.QRect(370, 150, 113, 22))
        self.nameBlank.setObjectName("nameBlank")
        self.surnameBlank = QtWidgets.QLineEdit(self.centralwidget)
        self.surnameBlank.setGeometry(QtCore.QRect(370, 220, 113, 22))
        self.surnameBlank.setObjectName("surnameBlank")
        self.ageBlank = QtWidgets.QLineEdit(self.centralwidget)
        self.ageBlank.setGeometry(QtCore.QRect(370, 290, 111, 22))
        self.ageBlank.setObjectName("ageBlank")
        self.titleBlank = QtWidgets.QLineEdit(self.centralwidget)
        self.titleBlank.setGeometry(QtCore.QRect(370, 360, 113, 22))
        self.titleBlank.setObjectName("titleBlank")

    def label_button(self,MainWindow):
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(250, 20, 301, 81))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setLineWidth(2)
        self.label.setMidLineWidth(0)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.confirmButton = QtWidgets.QPushButton(self.centralwidget)
        self.confirmButton.setGeometry(QtCore.QRect(500, 420, 93, 28))
        self.confirmButton.setObjectName("confirmButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menuAdmin_Page = QtWidgets.QMenu(self.menubar)
        self.menuAdmin_Page.setObjectName("menuAdmin_Page")
        self.menuUser_Page = QtWidgets.QMenu(self.menubar)
        self.menuUser_Page.setObjectName("menuUser_Page")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

    def windows(self,MainWindow):
        self.registerWin = QtWidgets.QAction(MainWindow)
        self.registerWin.setObjectName("registerWin")
        self.loginWin = QtWidgets.QAction(MainWindow)
        self.loginWin.setObjectName("loginWin")
        self.databaseWin = QtWidgets.QAction(MainWindow)
        self.databaseWin.setObjectName("databaseWin")
        self.userloginWin = QtWidgets.QAction(MainWindow)
        self.userloginWin.setObjectName("userloginWin")
        self.userWin = QtWidgets.QAction(MainWindow)
        self.userWin.setObjectName("userWin")
        self.menuAdmin_Page.addAction(self.registerWin)
        self.menuAdmin_Page.addSeparator()
        self.menuAdmin_Page.addAction(self.loginWin)
        self.menuAdmin_Page.addSeparator()
        self.menuAdmin_Page.addAction(self.databaseWin)
        self.menuUser_Page.addAction(self.userloginWin)
        self.menuUser_Page.addSeparator()
        self.menuUser_Page.addAction(self.userWin)
        self.menubar.addAction(self.menuAdmin_Page.menuAction())
        self.menubar.addAction(self.menuUser_Page.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Age.setText(_translate("MainWindow", "Age"))
        self.Title.setText(_translate("MainWindow", "Title"))
        self.Surname.setText(_translate("MainWindow", "Surname"))
        self.Name.setText(_translate("MainWindow", "Name"))
        self.label.setText(_translate("MainWindow", "Register"))
        self.confirmButton.setText(_translate("MainWindow", "Confirm"))
        self.menuAdmin_Page.setTitle(_translate("MainWindow", "Admin Page"))
        self.menuUser_Page.setTitle(_translate("MainWindow", "User Page"))
        self.registerWin.setText(_translate("MainWindow", "Register"))
        self.registerWin.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.loginWin.setText(_translate("MainWindow", "Login"))
        self.loginWin.setShortcut(_translate("MainWindow", "Ctrl+L"))
        self.databaseWin.setText(_translate("MainWindow", "Database"))
        self.databaseWin.setShortcut(_translate("MainWindow", "Ctrl+D"))
        self.userloginWin.setText(_translate("MainWindow", "Login"))
        self.userWin.setText(_translate("MainWindow", "User Information"))

        ##########################################        #############################################
        self.loginWin.clicked.connect(Ui_SecondWindow.initializer())
        self.confirmButton.clicked.connect(self.saveUser)
    # def loginCheck(self):


        # menuAdmin_Page
        # registerWin#ctrl+R
        # loginWin#ctrl+L
        # databaseWin#ctrl+D

        #############################################"
        #             To check login section for admin
        # self.loginWin.clicked.connect(self.setupLogin)
        #############################################
        #             To activate function with click
        # self.confirmButton.clicked.connect(self.saveUser)
        #############################################

        ##### Function to get user information and save them on a database ########

        ####### if any textblank is empty then takes it as empty ########

    def saveUser(self):
        default = ""
        name = self.nameBlank.text() or default
        surname = self.surnameBlank.text() or default
        title = self.titleBlank.text() or default
        age = self.ageBlank.text() or default

        d = {"Name": ["{}".format(name)], 'Surname': ["{}".format(surname)], "Age": ["{}".format(age)],
             "Title": ["{}".format(title)]}

        myClient = pm.MongoClient("mongodb://localhost:27017/")
        mydb = myClient["database"]
        mycol = mydb["employee"]

        x=mycol.insert_one(d)

    ##################################################################################

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
