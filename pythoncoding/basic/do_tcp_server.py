# 导入socket库:
import socket, threading, time

# 创建一个socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 监听窗口：
s.bind(('127.0.0.1', 9999))
s.listen(5)
print('Waiting for connnection...')

# 创建新线程（或进程）处理每个连接，单线程在处理连接的过程中，无法接受其他客户端的连接
def tcplink(sock, addr):
    print('Accept new connnection from %s:%s...' % addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed' % addr)
    
# 通过一个永久循环来接收来自客户端的连接
while True:
    # 接受一个新连接：
    sock, addr = s.accept()
    # 创建新线程来处理ICP连接：
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()