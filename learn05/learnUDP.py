import socket,threading

def UDPloop(sock,addr):
    print('accept connection from %s ' % addr)

    sock.close('closed connection from %s ' % addr)

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('127.0.0.1',9999))
while True:
    sock,addr=s.recvfrom(1024)
    #t=threading.Thread(target=UDPloop,args=(sock,addr))
    #t.start()
    print('Received from %s:%s' % addr)
    s.sendto(b'Hello, %s!' % sock, addr)
