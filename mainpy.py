
from PyQt5 import QtCore, QtGui, QtWidgets

import pymongo as pm

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
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        #############################################
        #             To activate function with click
        self.confirmButton.clicked.connect(self.saveUser)
        #############################################


##### Function to get user information and save them on a database ########
    ####### if any textblank is empty then takes it as empty ########

    def saveUser(self):

        default = ""
        name = self.nameBlank.text() or default
        surname = self.surnameBlank.text() or default
        title = self.titleBlank.text() or default
        age = self.ageBlank.text() or default

        d = {"Name": ["{}".format(name)], 'Surname': ["{}".format(surname)], "Age" : ["{}".format(age)],"Title":["{}".format(title)]}

        myClient = pm.MongoClient("mongodb://localhost:27017/")
        mydb = myClient["database"]
        mycol = mydb["employee"]

        x=mycol.insert_one(d)

##################################################################################






    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Age.setText(_translate("MainWindow", "Age"))
        self.Title.setText(_translate("MainWindow", "Title"))
        self.Surname.setText(_translate("MainWindow", "Surname"))
        self.Name.setText(_translate("MainWindow", "Name"))
        self.label.setText(_translate("MainWindow", "Register"))
        self.confirmButton.setText(_translate("MainWindow", "Confirm"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
