
import Leap,sys
from jsonsocket import Server
import socket

class SampleListener(Leap.Listener):
 def __init__(self,_server):
  super(SampleListener,self).__init__()
  self.server = _server
 def on_connect(self, controller):
  print("connected")

 def on_frame(self, controller):
  frame = controller.frame()
  #print(len(frame.fingers))
  hand = frame.hands.rightmost
  data = {'mainGauche':{'x':0,'y':0}, 'mainDroite':{'x':0,'y':0}}
  if hand.is_valid:
   if hand.is_left: 
    data['mainGauche']['x'] = hand.palm_position.x
    data['mainGauche']['y'] = hand.palm_position.y
   if hand.is_right:
    data['mainDroite']['x'] = hand.palm_position.x
    data['mainDroite']['y'] = hand.palm_position.y
  self.server.send(data)
  #print("Frame available")

def main():
  port = input("Port?:")
  server = Server('',port)
  print "Server cree"
  getIp()
  print "sur le port", port
  print "Attente de connection"
  server.accept()
  print "connection etablie"
  listener = SampleListener(server)
  controller = Leap.Controller()
  controller.add_listener(listener)
  print "Appuyez sur un bouton"
  try:
   sys.stdin.readline()
  except KeyboardInterrupt:
   pass
  server.close()

def getIp():
 s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
 s.connect(('8.8.8.8',80))
 print "Adresse du server Leap : ",s.getsockname()[0]
 s.close()


if __name__== "__main__":
  main()
