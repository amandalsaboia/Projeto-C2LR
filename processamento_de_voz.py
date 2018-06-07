import pyaudio
import serial
import speech_recognition as sr

arduino = serial.Serial('/dev/ttyAMA0',9600)
while (True == True):
# obtain audio from the microphone
  r = sr.Recognizer()
  with sr.Microphone() as source:
    # listen for 1 second and create the ambient noise energy level
    r.adjust_for_ambient_noise(source, duration=1)
    print("Say something!")
    audio = r.listen(source,phrase_time_limit=3)
 
# recognize speech using Google
  try:
    response = r.recognize_google(audio)
    print("I think you said: '" + response + "'")
    if ( "help" in response or "hello" in response  or "assistance" in response):
        print("Pessoa encontrada")
        comando ="h"
        arduino.write(comando.encode()) #envia a informacao para o arduino  de  que uma vitima foi encontrada
        

    else:
        print("Nao e uma pessoa") 
  except sr.UnknownValueError:
    print("I could not understand audio")

#arduino.close()
