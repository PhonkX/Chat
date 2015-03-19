#import socket

#servSock = socket.socket()
#servSock.bind(('',61390))
#servSock.listen(1)

#conn, addr = servSock.accept()

#print("Connected: ", addr)

#while True:
#    data = conn.recv(1024)
#    if not data:
#        break
#    print(data)
#    conn.send("Data is received".encode('utf=8'))

#conn.close()


#import socket

#serverSock = socket.socket()
#serverSock.bind(('',61390))
#serverSock.listen(10)
#print("Server")
#conn, addr = serverSock.accept()

#print("Connected: ", addr)
#conn.send("You are connected to the server: ".encode("utf-16"))

#while True:
#	data = conn.recv(1024)
#	data = data.decode("utf-16")
#	if data == "!exit":
#		print(addr, " is disconnected")
#	print(data)

#conn.close()

#import socket
#import threading



#class serverSock(threading.Thread):

#    def __init__(self, sock):
#        self.sock = sock
#        threading.Thread.__init__(self)
#    def run(self):
#        self.conn, self.addr = self.sock.accept()
#        print("Connected: ", addr)
#        self.conn.send("You are connected to the server: ".encode("utf-16"))
#        while True:
#            data = self.conn.recv(1024)
#            data = data.decode("utf-16")
#            if data == "!exit":
#                print(self.addr," is disconnected")
#                break
#            print(data)
#        self.conn.close()

#servSock = socket.socket()
#servSock.bind(('',61390))
#t = serverSock(servSock)
#t.start()

import socket
import threading



class Connection(threading.Thread):

    def __init__(self, conn, addr):
        self.conn = conn
        self.servAddr = "127.0.0.1"
        threading.Thread.__init__(self)
    def run(self):
        s = "You are connected to the server: " + self.servAddr
        self.conn.send(s.encode("utf-16"))
        self.conn.send("Please, enter your name: ".encode("utf-16"))
        name = self.conn.recv(1024)
        self.name = name.decode("utf-16")
        while True:
            data = self.conn.recv(1024)
            
            #self.conn.sendall(data)
            data = data.decode("utf-16")
            tempStr = self.name + ": " + data
            if data == "!exit":
                print(self.addr," is disconnected")
                break
            for clientThread in connArr:
                clientThread.conn.send(tempStr.encode("utf-16"))
            print(self.name,": ", data)
        self.conn.close()
   

servSock = socket.socket()
servSock.bind(('',61390))
servSock.listen(10)
print("Server")
connArr = []
while True:
    conn, addr = servSock.accept()
    print(addr, " is connected")
    t = Connection(conn, addr)
    t.start()
    connArr.append(t)
    