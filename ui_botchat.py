# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/yue/chatroom/bot_chat.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class bot_chat(object):
    def setupUi(self, bot_chat):
        bot_chat.setObjectName("bot_chat")
        bot_chat.resize(591, 450)
        bot_chat.setStyleSheet("background:black;")
        self.label = QtWidgets.QLabel(bot_chat)
        self.label.setGeometry(QtCore.QRect(0, 0, 59, 21))
        self.label.setStyleSheet("background:orange;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.textEdit_2 = QtWidgets.QTextEdit(bot_chat)
        self.textEdit_2.setGeometry(QtCore.QRect(10, 30, 571, 321))
        self.textEdit_2.setStyleSheet("background:white;")
        self.textEdit_2.setObjectName("textEdit_2")
        self.pushButton_3 = QtWidgets.QPushButton(bot_chat)
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
        self.lineEdit = QtWidgets.QLineEdit(bot_chat)
        self.lineEdit.setGeometry(QtCore.QRect(10, 380, 491, 41))
        self.lineEdit.setMaximumSize(QtCore.QSize(500, 500))
        self.lineEdit.setBaseSize(QtCore.QSize(200, 0))
        self.lineEdit.setStyleSheet("background:white")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(bot_chat)
        self.pushButton.setGeometry(QtCore.QRect(510, 370, 63, 51))
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

        self.retranslateUi(bot_chat)
        QtCore.QMetaObject.connectSlotsByName(bot_chat)

    def retranslateUi(self, bot_chat):
        _translate = QtCore.QCoreApplication.translate
        bot_chat.setWindowTitle(_translate("bot_chat", "Form"))
        self.label.setText(_translate("bot_chat", "聊天室"))
        self.pushButton_3.setText(_translate("bot_chat", "離開"))
        self.pushButton.setText(_translate("bot_chat", "發送"))


