# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/yue/chatroom/file.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class file_path(object):
    def setupUi(self, file):
        file.setObjectName("file")
        file.resize(260, 207)
        self.label = QtWidgets.QLabel(file)
        self.label.setGeometry(QtCore.QRect(90, 50, 71, 21))
        self.label.setStyleSheet("border: 1px solid gray;\n"
"")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(file)
        self.pushButton.setGeometry(QtCore.QRect(70, 100, 121, 41))
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

        self.retranslateUi(file)
        QtCore.QMetaObject.connectSlotsByName(file)

    def retranslateUi(self, file):
        _translate = QtCore.QCoreApplication.translate
        file.setWindowTitle(_translate("file", "Form"))
        self.label.setText(_translate("file", "上傳檔案"))
        self.pushButton.setText(_translate("file", "選擇檔案"))


