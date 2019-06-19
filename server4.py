import socket
import threading
from example2 import bot2  # 一般人多人聊天
import os
import random
import time
from pow import ana  # Jieba

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.bind(('0.0.0.0', 5551))  # Open socket with 5551 port

sock.listen(5)
print('Server', socket.gethostbyname('localhost'), 'listening ...')

mydict = dict()
mylist = list()

SIZE = 4096

# 檢察檔案是否重複，若重複則移除
def checkFile():
    list = os.listdir('.')
    for iterm in list:
        if iterm == 'image.bmp':
            os.remove(iterm)
            print('remove')
        else:
            pass

# 建立連線
def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send('Welcome from server!'.encode())
    print('receiving, please wait for a second ...')
    while True:
        data = sock.recv(SIZE)
        if not data:
            print('reach the end of file')
            break
        elif data == 'begin to send':
            print('create file')
            checkFile()
            with open('./image.bmp', 'wb') as f:
                pass
        else:
            with open('./image.bmp', 'ab') as f:
                f.write(data)
    sock.close()
    print('receive finished')
    print('Connection from %s:%s closed.' % addr)

# 傳送檔案
def sendfile(filename, full_filename, connectNumber):
    print("sending file")
    tellOthers(connectNumber, full_filename)  # 傳送檔案名稱
    time.sleep(0.5)
    with open(filename, "rb") as file:
        buffer = file.read()
        #print(buffer)
        tellOthers(connectNumber, buffer, 1)

    print("Done sending")


# 把 whatoSay 傳給自己以外所有人
def tellOthers(exceptNum, whatToSay, sendfile=0):
    for c in mylist:
        if c.fileno() != exceptNum:  # 如果不是傳送訊息的人
            if sendfile == 1:  # 如果是傳送檔案
                try:
                    c.sendall(whatToSay)
                except:
                    pass
            else:  # 如果是傳送正常訊息
                try:
                    c.send(whatToSay.encode())
                except:
                    pass

# 接收訊息
def subThreadIn(myconnection, connNumber):
    nickname = myconnection.recv(1024).decode()
    mydict[myconnection.fileno()] = nickname
    mylist.append(myconnection)
    print('connection', connNumber, ' has nickname :', nickname)
    tellOthers(connNumber, '【系统提示：' + mydict[connNumber] + ' 進入聊天室】')
    while True:
        try:
            recvedMsg = myconnection.recv(1024).decode()
            #print("recvedMsg is: " + str(recvedMsg))
            if recvedMsg:
                bot_response = str(bot2.get_response(recvedMsg))
                if recvedMsg == "BYE" or bot_response == "違規訊息" or recvedMsg == "bye":  # 如果使用者要離開或輸入了違規訊息
                    try:
                        tellOthers(-1, '【系统提示：' + mydict[connNumber] + ' 離開聊天室】')
                        time.sleep(1)
                        mylist.remove(myconnection)  # 移除該使用者
                    except:
                        pass
                    print(mydict[connNumber], 'exit, ', len(mylist), ' person left')
                    myconnection.close()

                elif recvedMsg == "SEND FILE" or recvedMsg == "SEND PICTURE":  # 如果使用者要傳送檔案
                    extention = myconnection.recv(1024).decode()  # 抓取該檔副檔名
                    print("extention is: " + str(extention))
                    filename_new = random.randint(1, 10000)  # Random 檔案名稱
                    full_filename = str(filename_new) + "." + str(extention)   # 完整檔案名稱
                    with open(full_filename, 'wb') as file:  # Server 接收檔案
                        buffer = myconnection.recv(1024)
                        while buffer:
                            file.write(buffer)
                            if "DONE SENDING" in str(buffer):  # 如果 client 傳送完成
                                file.close()
                                break
                            buffer = myconnection.recv(1024)
                    if recvedMsg == "SEND FILE":  # 如果使用者上傳檔案
                        tellOthers(connNumber, mydict[connNumber] + ': sendingfile')
                    else:  # 如果使用者上傳圖片
                        tellOthers(connNumber, mydict[connNumber] + ': sendingpicture')
                    time.sleep(0.5)
                    sendfile(full_filename, str(full_filename), connNumber)  # 從 server 端傳給其他使用者
                    tellOthers(-1, "Done sending")

                elif recvedMsg == "傳送貼圖1" or recvedMsg == "傳送貼圖2":  # 如果使用者要傳送貼圖
                    print(mydict[connNumber], ':', recvedMsg)
                    tellOthers(connNumber, mydict[connNumber] + ': ' + recvedMsg)

                else:  # Server 接收一般訊息
                    result = ana(str(recvedMsg))  # 使用 Jieba 算使用者訊息與違規訊息的相似度
                    if result:  # 如果回傳為違規訊息
                        try:
                            tellOthers(-1, '【系统提示：' + mydict[connNumber] + ' 因違反規定踢出聊天室】')
                            time.sleep(1)
                            mylist.remove(myconnection)
                        except:
                            pass
                        print(mydict[connNumber], 'exit, ', len(mylist), ' person left')
                        myconnection.close()
                    # 如果為正常訊息則正常傳送給其他使用者
                    print(mydict[connNumber], ':', recvedMsg)
                    tellOthers(connNumber, mydict[connNumber] + ': ' + recvedMsg)

        except (OSError, ConnectionResetError):
            return


while True:
    connection, addr = sock.accept()
    print('Accept a new connection', connection.getsockname(), connection.fileno())
    try:
        # connection.set-timeout(5)
        buf = connection.recv(1024).decode()
        if buf == '1':
            connection.send(b'welcome to server!')

            # 為不斷接收訊息開 thread
            mythread = threading.Thread(target=subThreadIn, args=(connection, connection.fileno()))
            mythread.setDaemon(True)
            mythread.start()

        else:
            connection.send(b'please go out!')
            connection.close()
    except:
        pass
