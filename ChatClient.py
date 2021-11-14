# Echo client program
import socket
import threading

def recvAndPrint(socket):
    '''接收消息并打印'''
    while True:
        data = s.recv(1024)
        if not data:
            break
        print(data.decode())

def recvAndSend(socket):
    while True:
        s = input()
        socket.send(s.encode())

HOST = 'localhost'    # The remote host
PORT = 50007              # The same port as used by the server
s = socket.socket()
s.connect((HOST, PORT))

print("Connected to",s.getpeername())
    #print(s.getsockname())


#recvAndSend(s)
t = threading.Thread(target=recvAndSend,args=(s,))
t.start()

t1 = threading.Thread(target=recvAndPrint,args=(s,))
t1.start()
t1.join()
