# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/yue/chatroom/texture.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_chatroom_texture(object):
    def setupUi(self, Texture):
        Texture.setObjectName("Texture")
        Texture.resize(392, 222)
        self.label = QtWidgets.QLabel(Texture)
        self.label.setGeometry(QtCore.QRect(20, 20, 131, 121))
        self.label.setStyleSheet("background-color:white;\n"
"border:2px solid gray;")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../Downloads/１５９.jpg"))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Texture)
        self.pushButton.setGeometry(QtCore.QRect(40, 160, 81, 31))
        self.pushButton.setStyleSheet("QPushButton\n"
"{\n"
"background-color:white;\n"
"border:2px solid gray;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"   background-color:qlineargradient(x1:0,y1:0,x2:0,y2:1,stop: 0 #dadbde,stop: 1 #f6f7fa); \n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(Texture)
        self.label_2.setGeometry(QtCore.QRect(220, 20, 131, 121))
        self.label_2.setStyleSheet("background-color:white;\n"
"border:2px solid gray;")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../Downloads/４１２.png"))
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(Texture)
        self.pushButton_2.setGeometry(QtCore.QRect(250, 160, 81, 32))
        self.pushButton_2.setStyleSheet("QPushButton\n"
"{\n"
"background-color:white;\n"
"border:2px solid gray;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"   background-color:qlineargradient(x1:0,y1:0,x2:0,y2:1,stop: 0 #dadbde,stop: 1 #f6f7fa); \n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Texture)
        QtCore.QMetaObject.connectSlotsByName(Texture)

    def retranslateUi(self, Texture):
        _translate = QtCore.QCoreApplication.translate
        Texture.setWindowTitle(_translate("Texture", "貼圖"))
        self.pushButton.setText(_translate("Texture", "貼圖１"))
        self.pushButton_2.setText(_translate("Texture", "貼圖２"))

