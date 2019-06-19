import socket
import threading
from example import bot  # 與 bot 聊天

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.bind(('0.0.0.0', 5550))  # Open socket with 5550 port

sock.listen(5)
print('Server', socket.gethostbyname('localhost'), 'listening ...')

mydict = dict()
mylist = list()


# 把whatoSay傳給自己以外所有人
def tellOthers(exceptNum, whatToSay):
    for c in mylist:
        if c.fileno() != exceptNum:
            try:
                c.send(whatToSay.encode())
            except:
                pass


def subThreadIn(myconnection, connNumber):
    nickname = myconnection.recv(1024).decode()  # 第一次連線時存該使用者的暱稱
    mydict[myconnection.fileno()] = nickname
    mylist.append(myconnection)
    print('connection', connNumber, ' has nickname :', nickname)
    tellOthers(connNumber, '【系统提示：' + mydict[connNumber] + ' 進入聊天室】')
    while True:
        try:
            recvedMsg = myconnection.recv(1024).decode()
            if recvedMsg:
                if recvedMsg == "BYE" or recvedMsg == "bye":  # 如果使用者要退出
                    try:
                        mylist.remove(myconnection)
                    except:
                        pass
                    print(mydict[connNumber], 'exit, ', len(mylist), ' person left')
                    tellOthers(connNumber, '【系统提示：' + mydict[connNumber] + ' 離開聊天室】')
                    myconnection.close()
                else:  # 正常訊息傳送
                    print(mydict[connNumber], ':', recvedMsg)
                    bot_response = bot.get_response(recvedMsg)
                    tellOthers(connNumber, mydict[connNumber] + ': ' + recvedMsg)
                    tellOthers(-1, "bot to " + mydict[connNumber] + ": " + str(bot_response))

        except (OSError, ConnectionResetError):
            return


while True:
    connection, addr = sock.accept()
    print('Accept a new connection', connection.getsockname(), connection.fileno())
    try:
        # connection.settimeout(5)
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
