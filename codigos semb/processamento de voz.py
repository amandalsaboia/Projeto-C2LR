import pyaudio
import serial
import speech_recognition as sr

arduino = serial.Serial('/dev/ttyAMA0',9600)
while (True == True):
# obt�m �udio do microfone
  r = sr.Recognizer()
  with sr.Microphone() as source:
    # escuta por 1 segundo and ajusta o n�vel de energia  considerando o ru�do do ambiente 
    r.adjust_for_ambient_noise(source, duration=1)
    print("Say something!")
    audio = r.listen(source,phrase_time_limit=3)#come�a a capturar som e define que essa captura durar� 3 segundos e retornar a parte da frase processada antes que o limite de tempo seja atingido
 
# reconhece fala usando a api do Google
  try:
    response = r.recognize_google(audio)
    print("I think you said: '" + response + "'") #imprime o som capturado convertido em texto
#verifica utilizando o conceito de substring se no texto convertido tem alguma dessas tr�s palavras
    if ( "help" in response or "hello" in response  or "assistance" in response): 
        print("Pessoa encontrada")
        comando ="h" #se uma pessoa for encontrada salva esse comando para posteriormente ser enviado para o arduino
        arduino.write(comando.encode()) #envia a informacao para o arduino  de  que uma vitima foi encontrada
    #se no texto convertido n�o tiver nenhuma das palavras acima, o c�digo entrar� no else e dir� q eu nenhuma pessoa foi encontrada
    else:
        print("Nao e uma pessoa")
#caso por algum motivo a aplica��o n�o consiga capturar um som em ingl�s que d� para realizar a convers�o(som para texto) imiprimir� "I could not understand audio" 
  except sr.UnknownValueError:
    print("I could not understand audio")

#arduino.close()
