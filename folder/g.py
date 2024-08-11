'''
    流式套接字
'''
import socket

# 创建tcp套接字 
sock = socket.socket(socket.AF_INET,
                       socket.SOCK_STREAM)
# 绑定地址
sock.bind(('127.0.0.1',12345))
# 设置监听队列
sock.listen(5)
# 阻塞等待连接处理
while True:
    print('Waiting for connect~')
    try:
        connfd,addr = sock.accept() # 返回值是个元组,客户和地址
        print('Connect from',addr)
    except KeyboardInterrupt:
        print('服务器退出')
        break
    except Exception as e:
        print(e)
        break
    # 收发消息
    while True:
        data = connfd.recv(1024) # 如果连接端断开返回个空
        if not data:
            break
        print('收到:', data)
        n = connfd.send(b'Thanks')
        print('发送%d个字节'%n)
    # 关
    connfd.close()
sock.close()