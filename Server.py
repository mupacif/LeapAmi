from jsonsocket import Server
import socket

def getIp():
 s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
 s.connect(('8.8.8.8',80))
 print "Adresse du server Leap : ",s.getsockname()[0], "port: 8000"
 s.close()


server = Server('',8001)
print "Server cree"
getIp()
print "Attente de connection"
server.accept()
data = {'msg':'bonjour'}
while 1:
 msg = input("Write something:")
 if msg == "":
  break
 server.send({'msg':msg})
server.close()
 
