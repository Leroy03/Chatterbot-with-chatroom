# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/yue/chatroom/chatroom.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Chat_interface(object):
    def setupUi(self, chatroom):
        chatroom.setObjectName("chatroom")
        chatroom.resize(591, 450)
        chatroom.setStyleSheet("background:black;")
        self.label = QtWidgets.QLabel(chatroom)
        self.label.setGeometry(QtCore.QRect(0, 0, 59, 21))
        self.label.setStyleSheet("background:orange;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(chatroom)
        self.pushButton.setGeometry(QtCore.QRect(510, 380, 63, 51))
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
        self.textEdit_2 = QtWidgets.QTextEdit(chatroom)
        self.textEdit_2.setGeometry(QtCore.QRect(10, 30, 571, 321))
        self.textEdit_2.setStyleSheet("background:white;")
        self.textEdit_2.setObjectName("textEdit_2")
        self.lineEdit = QtWidgets.QLineEdit(chatroom)
        self.lineEdit.setGeometry(QtCore.QRect(10, 390, 491, 41))
        self.lineEdit.setMaximumSize(QtCore.QSize(500, 500))
        self.lineEdit.setBaseSize(QtCore.QSize(200, 0))
        self.lineEdit.setStyleSheet("background:white")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_2 = QtWidgets.QPushButton(chatroom)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 360, 51, 21))
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
        self.pushButton_3 = QtWidgets.QPushButton(chatroom)
        self.pushButton_3.setGeometry(QtCore.QRect(500, 0, 81, 31))
        self.pushButton_3.setStyleSheet("QPushButton\n"
"{\n"
"background-color:white;\n"
"border:2px solid gray;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"   background-color:qlineargradient(x1:0,y1:0,x2:0,y2:1,stop: 0 #dadbde,stop: 1 #f6f7fa); \n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(chatroom)
        self.pushButton_4.setGeometry(QtCore.QRect(80, 360, 51, 21))
        self.pushButton_4.setStyleSheet("QPushButton\n"
"{\n"
"background-color:white;\n"
"border:2px solid gray;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"   background-color:qlineargradient(x1:0,y1:0,x2:0,y2:1,stop: 0 #dadbde,stop: 1 #f6f7fa); \n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(chatroom)
        self.pushButton_5.setGeometry(QtCore.QRect(150, 360, 51, 21))
        self.pushButton_5.setStyleSheet("QPushButton\n"
"{\n"
"background-color:white;\n"
"border:2px solid gray;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"   background-color:qlineargradient(x1:0,y1:0,x2:0,y2:1,stop: 0 #dadbde,stop: 1 #f6f7fa); \n"
"}")
        self.pushButton_5.setObjectName("pushButton_5")

        self.retranslateUi(chatroom)
        QtCore.QMetaObject.connectSlotsByName(chatroom)

    def retranslateUi(self, chatroom):
        _translate = QtCore.QCoreApplication.translate
        chatroom.setWindowTitle(_translate("chatroom", "Form"))
        self.label.setText(_translate("chatroom", "聊天室"))
        self.pushButton.setText(_translate("chatroom", "發送"))
        self.pushButton_2.setText(_translate("chatroom", "貼圖"))
        self.pushButton_3.setText(_translate("chatroom", "離開"))
        self.pushButton_4.setText(_translate("chatroom", "圖片"))
        self.pushButton_5.setText(_translate("chatroom", "檔案"))


