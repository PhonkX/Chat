#import socket

#clientSock = socket.socket()

#clientSock.connect(('localhost', 61390))
#clientSock.send("Llala".encode('utf-8'))
#data = clientSock.recv(1024)

#clientSock.close()
#print(data)
import socket
import threading
class serverMsg(threading.Thread):
    def __init__(self, sock):
        self.sock = sock
        threading.Thread.__init__(self)
    def run(self):
        while True:
            data = self.sock.recv(1024)
            print(data.decode("utf-16"))
#class clientMsg(threading.Thread):
#    def __init__(self, sock):
#        self.sock = sock
#        threading.Thread.__init__(self)
#    def run(self):
#        while True:
#            data = input()
#            self.sock.send(data.encode("utf-16"))
#            if data == "!exit":
#                break

clientSock = socket.socket()
print("Client")
print("Enter address: ")
addr = input()
clientSock.connect((addr, 61390))
info = clientSock.recv(1024)
print(info.decode("utf-16"))
info = clientSock.recv(1024)
print(info.decode("utf-16"))
srvMsg = serverMsg(clientSock)
srvMsg.start()
#clMsg = clientMsg(clientSock)
#clMsg.start()
while True:
    data = input()
    clientSock.send(data.encode("utf-16"))
    if data == "!exit":
        break
clientSock.close()
