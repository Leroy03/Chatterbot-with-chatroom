import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QIcon, QPixmap
from ui_chatroom import Ui_Chatmenu
from ui_chatroom_interface import Ui_Chat_interface
from ui_chatroom_texture import Ui_chatroom_texture
from Ui_image_path import image_path
from Ui_file import file_path  # 引入介面檔案
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QFileDialog
from ui_botchat import bot_chat
import socket
import time
import threading
import random

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 設定好socket連線參數
SIZE = 4096
nickName = ""
buttoned = 0
message = ""
fileName = ""


class menu(QtWidgets.QMainWindow, Ui_Chatmenu, Ui_Chat_interface, Ui_chatroom_texture, image_path, file_path, bot_chat):
    def __init__(self, parent=None):  # 程式主畫面 menu部分
        super(menu, self).__init__(parent)
        self.window = QtWidgets.QMainWindow()
        self.window.setFixedSize(591, 450)
        self.setFixedSize(456, 370)
        self.ui = Ui_Chat_interface()
        label = QLabel(self)
        label.setFixedSize(456, 370)
        pixmap = QPixmap('/Users/yue/Desktop/chatroom/people.jpg')  # 建立主畫面背景圖片
        pixmap4 = pixmap.scaled(555, 370, QtCore.Qt.KeepAspectRatio)
        label.setPixmap(pixmap4)
        self.setupUi(self)
        # self.show()
        self.pushButton.clicked.connect(self.enter_chat)  # 按鈕１與其他使用者聊天
        self.pushButton_2.clicked.connect(self.chat_bot)  # 按鈕２與機器人聊天

    def enter_chat(self):
        if self.lineEdit.text() != "":  # 建立連線
            sock.connect(('ttyl.ddns.net', 5551))
            sock.send(b'1')
            print(sock.recv(1024).decode())
            global nickName
            global message
            nickName = self.lineEdit.text()  # 傳送輸入的暱稱給server端
            sock.send(nickName.encode())
            print(nickName)
            self.ui.setupUi(self.window)
            self.hide()
            self.window.show()  # 建立聊天室介面
            self.ui.textEdit_2.setReadOnly(True)  # 讓textEdit只可讀寫
            if self.ui.lineEdit.text() != " ":  # 要輸入暱稱才可以進入聊天室介面
                th2 = threading.Thread(target=self.recvThreadFunc)  # 利用thread來接收訊息
                th2.setDaemon(True)
                th2.start()
                # th2.join()
                self.ui.lineEdit.returnPressed.connect(self.sendmessage)  # 按enter鍵傳送訊息
                self.ui.pushButton.clicked.connect(self.sendmessage)  # 按傳送button傳送訊息
                self.ui.pushButton_3.clicked.connect(self.exit_sys)  # 離開按鈕
                self.ui.pushButton_2.clicked.connect(self.texture_win)  # 設立與彈出貼圖視窗
                self.ui.pushButton_4.clicked.connect(self.get_path)  # 傳送圖片
                self.ui.pushButton_5.clicked.connect(self.get_file_path)  # 傳送檔案

    def chat_bot(self):  # 與機器人聊天
        if self.lineEdit.text() != "":
            self.ui = bot_chat()
            sock.connect(('ttyl.ddns.net', 5550))  # 建立連線
            sock.send(b'1')
            print(sock.recv(1024).decode())
            global nickName
            global message
            nickName = self.lineEdit.text()
            sock.send(nickName.encode())
            print(nickName)
            self.ui.setupUi(self.window)
            self.hide()
            self.window.show()
            self.ui.textEdit_2.setReadOnly(True)
            if self.ui.lineEdit.text() != " ":
                th2 = threading.Thread(target=self.recvThreadFunc)
                th2.setDaemon(True)
                th2.start()
                # th2.join()
                self.ui.lineEdit.returnPressed.connect(self.sendmessage)  # 同上
                self.ui.pushButton.clicked.connect(self.sendmessage)
                self.ui.pushButton_3.clicked.connect(self.exit_sys)

    def file_clicked(self):  # 當點擊傳送檔案的按鈕則彈出選擇檔案路徑的列表
        global fileName, myword
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "", "All Files (*)",
                                                  options=options)
        if fileName:
            print(fileName)
            file = str(fileName).split('.')
            myword = "SEND FILE"  # 告知server準備傳送檔案
            buttoned = 1
            print(file[1])
            th1 = threading.Thread(target=self.sendThreadFunc)
            th1.setDaemon(True)
            th1.start()
            th1.join()
            sock.send(file[1].encode())
            time.sleep(0.5)
            self.file_delivery(fileName)  # 負責檔案傳送的函示
            myword = "DONE SENDING"  # 告知檔案傳送完成
            th4 = threading.Thread(target=self.sendThreadFunc)
            th4.setDaemon(True)
            th4.start()
            th4.join()
            self.window4.hide()  # 傳送完畢關掉傳送檔案的介面

    def mybutton_clicked(self):  # 圖片傳送
        global fileName, myword
        options = QFileDialog.Options()  # 彈出檔案列表
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "", "All Files (*)",
                                                  options=options)
        if fileName:
            print(fileName)
            file = str(fileName).split('.')
            myword = "SEND PICTURE"  # 告知要傳送圖片
            buttoned = 1
            print(file[1])
            th1 = threading.Thread(target=self.sendThreadFunc)
            th1.setDaemon(True)
            th1.start()
            th1.join()
            sock.send(file[1].encode())
            time.sleep(0.5)
            self.file_delivery(fileName)
            myword = "DONE SENDING"  # 告知圖片傳送完成
            th4 = threading.Thread(target=self.sendThreadFunc)
            th4.setDaemon(True)
            th4.start()
            th4.join()
            self.window3.hide()  # 傳送完畢關掉介面
            string1 = nickName + ": "
            self.ui.textEdit_2.append(string1)
            cursor = self.ui.textEdit_2.textCursor()  # 訊息列呈現傳送的圖片
            icon = QPixmap(fileName)
            pixmap4 = icon.scaled(128, 128, QtCore.Qt.KeepAspectRatio)
            image = pixmap4.toImage()
            cursor.insertImage(image)

    def file_delivery(self, filename):  # 檔案傳送
        with open(str(fileName), "rb") as video:  # 讀取檔案
            buffer = video.read()
            print(buffer)
            sock.sendall(buffer)  # 透過socket傳送

    def get_file_path(self):  # 傳送檔案的介面
        self.window4 = QtWidgets.QDialog()
        self.window4.setFixedSize(260, 207)
        self.ui4 = file_path()
        self.ui4.setupUi(self.window4)  # 設立並呈現介面
        # self.window.hide()
        self.window4.show()
        self.ui4.pushButton.clicked.connect(self.file_clicked)

    def get_path(self):  # 傳送圖片的介面
        self.window3 = QtWidgets.QDialog()
        self.window3.setFixedSize(260, 207)
        self.ui3 = image_path()
        self.ui3.setupUi(self.window3)
        # self.window.hide()
        self.window3.show()
        self.ui3.pushButton.clicked.connect(self.mybutton_clicked)

    def texture_win(self):  # 貼圖呈現的介面
        self.window2 = QtWidgets.QDialog()
        self.window2.setFixedSize(392, 222)
        self.ui2 = Ui_chatroom_texture()
        self.ui2.setupUi(self.window2)
        # self.window.hide()
        self.window2.show()  # 利用label呈現貼圖圖檔
        pixmap = QPixmap('159.jpg')
        self.ui2.label.setPixmap(pixmap)
        # self.resize(pixmap.width(), pixmap.height())
        pixmap = QPixmap('357.PNG')
        self.ui2.label_2.setPixmap(pixmap)
        self.ui2.pushButton.clicked.connect(self.send_texture1)  # 透過button取得傳送的貼圖資訊
        self.ui2.pushButton_2.clicked.connect(self.send_texture2)

    def send_texture1(self):  # 傳送貼圖１
        global myword
        global buttoned
        # self.window3 = QtWidgets.QDialog()
        # self.ui_texture = chat_texture()
        # self.ui_texture.initUI()
        # self.ui_texture.show()
        myword = "傳送貼圖1"  # 告知server傳送貼圖
        buttoned = 1
        th1 = threading.Thread(target=self.sendThreadFunc)
        th1.setDaemon(True)
        th1.start()
        string1 = nickName + ": "
        self.ui.textEdit_2.append(string1)
        cursor = self.ui.textEdit_2.textCursor()  # 在訊息列呈現
        icon = QPixmap('159.jpg')
        image = icon.toImage()
        cursor.insertImage(image)
        self.ui.textEdit_2.setTextCursor(cursor)
        self.window2.hide()

    def send_texture2(self):  # 同上 貼圖２
        global myword
        global buttoned
        # self.window3 = QtWidgets.QDialog()
        # self.ui_texture = chat_texture()
        # self.ui_texture.initUI()
        # self.ui_texture.show()
        myword = "傳送貼圖2"
        buttoned = 1
        th1 = threading.Thread(target=self.sendThreadFunc)
        th1.setDaemon(True)
        th1.start()
        string1 = nickName + ": "
        self.ui.textEdit_2.append(string1)
        cursor = self.ui.textEdit_2.textCursor()
        icon = QPixmap('357.png')
        image = icon.toImage()
        cursor.insertImage(image)
        self.ui.textEdit_2.setTextCursor(cursor)
        self.window2.hide()

    def sendmessage(self):  # 傳送訊息
        global myword
        global buttoned
        myword = self.ui.lineEdit.text()  # 讀取輸入的訊息
        buttoned = 1
        th1 = threading.Thread(target=self.sendThreadFunc)  # 透過socket連線 使用thread進行傳送
        th1.setDaemon(True)
        th1.start()
        self.ui.lineEdit.setText("")
        message = nickName + ": " + myword
        self.ui.textEdit_2.append(message)
        th1.join()

    def exit_sys(self):  # 離開按鈕
        global myword
        global buttoned
        myword = "bye"  # 告知server 該使用者要離線
        buttoned = 1
        th1 = threading.Thread(target=self.sendThreadFunc)
        th1.setDaemon(True)
        th1.start()
        self.ui.lineEdit.setText("")
        message = nickName + ": " + myword
        self.ui.textEdit_2.append(message)
        th1.join()
        sys.exit(app.exec_())

    def sendThreadFunc(self, enc_byte=0):  # 傳送訊息 thread函式
        global nickName
        global myword
        global buttoned
        try:
            # print(myword)
            if enc_byte == 0:
                sock.send(myword.encode())  # 訊息先encode在傳送
            else:
                sock.send(myword)  # 檔案或圖檔的位元組不能encode 所以透過變數做判斷
            # print(sock.recv(1024).decode())
        except ConnectionAbortedError:
            print('Server closed this connection!')
        except ConnectionResetError:
            print('Server is closed!')

    def recvThreadFunc(self):  # 透過thread接收訊息
        global message
        while True:
            try:
                otherword = sock.recv(1024)  # 取得server傳送過來的訊息
                if otherword:
                    message = otherword.decode()  # 先將訊息decode
                    print("message is: " + message)
                    # message = self.ui.textEdit_2.toPlainText() + message
                    # self.ui.textEdit_2.setText(message)
                    lis = message.split(" ")  # 將字串切割 lis[0]儲存傳送的使用者暱稱 lis[1]則為訊息內容來做判斷
                    lis[0] += " "
                    if lis[1] == "傳送貼圖1":  # 代表該使用者傳送貼圖１
                        self.ui.textEdit_2.append(lis[0])
                        cursor = self.ui.textEdit_2.textCursor()  # 將貼圖呈現
                        icon = QPixmap('159.jpg')
                        image = icon.toImage()
                        cursor.insertImage(image)
                        self.ui.textEdit_2.setTextCursor(cursor)
                        self.ui.textEdit_2.append("")
                    elif lis[1] == "傳送貼圖2":  # 同上 貼圖2
                        self.ui.textEdit_2.append(lis[0])
                        cursor = self.ui.textEdit_2.textCursor()
                        icon = QPixmap('357.png')
                        image = icon.toImage()
                        cursor.insertImage(image)
                        self.ui.textEdit_2.setTextCursor(cursor)
                        self.ui.textEdit_2.append("")
                    elif lis[1] == "sendingpicture":  # 判斷該使用者傳送照片
                        filename = sock.recv(1024).decode()  # 從server取得亂數檔名以做檔案驗證
                        print(filename)
                        with open(filename, 'wb') as file:  # 將收到的位元組做寫入
                            buffer = sock.recv(1024)  # 不斷取得位元組 直到取得完整檔案資訊
                            while buffer:
                                print("word is " + str(buffer))
                                file.write(buffer)
                                if "Done sending" in str(buffer):  # 透過server傳送此訊息告知使用者檔案資訊傳送完畢
                                    file.close()
                                    break
                                buffer = sock.recv(1024)
                        print('receive finished')
                        self.ui.textEdit_2.append(lis[0])
                        cursor = self.ui.textEdit_2.textCursor()  # 將圖檔呈現在訊息列
                        icon = QPixmap(filename)
                        pixmap4 = icon.scaled(128, 128, QtCore.Qt.KeepAspectRatio)
                        image = pixmap4.toImage()
                        cursor.insertImage(image)
                        self.ui.textEdit_2.append("")
                    elif lis[1] == "sendingfile":  # 判斷傳送檔案
                        filename = sock.recv(1024).decode()
                        print(filename)
                        with open(filename, 'wb') as file:  # 做寫入動作
                            buffer = sock.recv(1024)
                            while buffer:
                                print("word is " + str(buffer))
                                file.write(buffer)
                                if "Done sending" in str(buffer):
                                    file.close()
                                    break
                                buffer = sock.recv(1024)
                        print('receive finished')
                        self.ui.textEdit_2.append(lis[0] + "已傳送檔案：" + filename)  # 訊息列顯示某個使用者傳送了某檔案

                    else:
                        self.ui.textEdit_2.append(message)  # 判斷傳送訊息,獲得其他使用者傳送的訊息直接顯示
                else:
                    pass
            except ConnectionAbortedError:
                print('Server closed this connection!')

            except ConnectionResetError:
                print('Server is closed!')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = menu()
    ex.show()
    sys.exit(app.exec_())
