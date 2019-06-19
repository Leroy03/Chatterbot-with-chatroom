# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/yue/chatroom/image_path.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QLabel , QFileDialog


class image_path(object):
    def setupUi(self, image_path):
        image_path.setObjectName("image_path")
        image_path.resize(260, 207)
        self.label = QtWidgets.QLabel(image_path)
        self.label.setGeometry(QtCore.QRect(90, 40, 71, 21))
        self.label.setStyleSheet("border: 1px solid gray;\n"
"")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(image_path)
        self.pushButton.setGeometry(QtCore.QRect(70, 90, 121, 41))
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

        self.retranslateUi(image_path)
        #self.pushButton.clicked.connect(image_path.mybutton_clicked)
        QtCore.QMetaObject.connectSlotsByName(image_path)


    def retranslateUi(self, image_path):
        _translate = QtCore.QCoreApplication.translate
        image_path.setWindowTitle(_translate("image_path", "上傳圖片"))
        self.label.setText(_translate("image_path", "上傳圖片"))
        self.pushButton.setText(_translate("image_path", "選擇圖片"))



