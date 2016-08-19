from jsonsocket import Client

cl = Client()
port = input("Port?")
cl.connect('192.168.1.8',port)
while 1:
 data=cl.recv()
 if(data['mainGauche']['x']!=0):
  print("main gauche")
 elif(data['mainDroite']['x']!=0):
  print("main Droite")
 else:
  print("")
 if data == "":
   break
cl.close()
