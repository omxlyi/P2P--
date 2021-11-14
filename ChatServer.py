# Echo server program
import socket
import threading


def recvAndPrint(s):
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


HOST = ''  # Symbolic name meaning all available interfaces
PORT = 50007  # Arbitrary non-privileged port

s = socket.socket()
s.bind((HOST, PORT))
s.listen()
print("开始监听...")

con, addr = s.accept()
print('有一个新的连接来自', addr)

t = threading.Thread(target=recvAndPrint, args=(con,))
t.start()

while True:
    # print(con.recv(1024).decode())
    str = input()
    con.send(str.encode())

##注意
# 服务器必须按序执行 socket(),
# bind(), listen(), accept()
# （可能需要重复执行 accept() 以服务多个客户端）

# 客户端仅需要按序执行 socket(), connect()

# 还须注意，服务器不在侦听套接字上发送 sendall()/recv()，
# 而是在 accept() 返回的新套接字上发送。

# 通常有 3 种方法可以让这个循环工作起来
# 调度一个线程来处理 客户端套接字
# 把这个应用改成使用非阻塞模式套接字
# 使用 select 库来实现「服务端」套接字与任意活动 客户端套接字 之间的多路复用


# 套接字对象
# s.accept()
# return    (conn,address)
# conn:是一个新的套接字对象，用于在此连接上收发数据
# address:另一端套接字所绑定的地址
# s.bind(address)
# address:格式取决于地址簇(AF_INET)
# s.listen([backlog])
# 启动一个服务器用于接受连接
# backlog:指定连接数，超过则拒绝新连接
# s.close()
# 将套接字标记为关闭，如果要及时关闭连接，在之前调用shutdown()
# s.connect(address)
# 连接到address处的远程套接字
# s.getpeername()
# 返回套接字连接到的远程地址
# s.getsockname()
# 返回套接字本身的地址
# s.getblocking()
# 如果套接字处于阻塞模式，返回True
# s.gettimeout()
# 返回套接字操作相关的超时秒数

# s.send(bytes)
# return:已发送的字节数
# s.sendall(bytes)
# 持续从 bytes 发送数据，直到所有数据都已发送或发生错误为止。
# 成功后会返回 None
# s.sendto(bytes,address)
# return:已发送的字节数
# s.sendfile(file,offset=0,count=None)
# return:已发送的字节总数
# file:以二进制模式打开的常规文件对象
# offset:从哪里开始读取文件
# count:要发送的字节总数

# s.recv(bufsize)
# return:一个字节对象
# bufsize:最大可接收数据量
# s.recvfrom(bufsize)
# return:(bytes,address)
# s.recvfrom_into(buffer[,nbytes])
# 从套接字接收数据，将其写入 buffer 而不是创建新的字节串。
# return:(nbytes,address)
# nbytes:收到的字节数
# s.recv_into(buffer[,nbytes])
# 从套接字接收至多 nbytes 个字节，将其写入缓冲区而不是创建新的字节串

# s.setblocking(flag)
# 设置套接字为阻塞或非阻塞模式：如果 flag 为 false，则将套接字设置为非阻塞，否则设置为阻塞
# s.shudown(how)
# 关闭一半或全部的连接
# 如果 how 为 SHUT_RD，则后续不再允许接收
# 如果 how 为 SHUT_WR，则后续不再允许发送
# 如果 how 为 SHUT_RDWR，则后续的发送和接收都不允许
