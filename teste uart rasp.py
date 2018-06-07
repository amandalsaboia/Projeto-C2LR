import serial

arduino = serial.Serial('/dev/ttyAMA0',9600) 

while True:
       comando = raw_input("coloque o comando:")
       arduino.write(comando) # envia para o arduino via uart o comando escrito
       if comando == "H":
          print("led ligado")
       else comando =="L":
          print ("led apagado")