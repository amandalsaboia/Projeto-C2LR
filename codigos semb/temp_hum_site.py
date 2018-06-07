import sys
import RPi.GPIO as GPIO
from time import sleep  
import Adafruit_DHT
import urllib2
    
def getSensorData():
    RH, T = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 4)
    # retorna umidade e temperatura
    return (str(RH), str(T))
    
#funcao main
def main():
    # usa sys.argv se necessario
    if len(sys.argv) < 2:
        print("usando: python teste.py chave privada")
        exit(0)
    print ("iniciando envio de dados")

    baseURL = "https://api.thingspeak.com/update?api_key=%s" % sys.argv[1] #url do site especializado em receber informações dos sensores
   
    while True:
        try:
            RH, T = getSensorData()
            f = urllib2.urlopen(baseURL + 
                                "&field1=%s&field2=%s" % (RH, T))
            print (f.read())
            f.close()
            sleep(15)
        except:
            print ("saindo.")
            break

# chamada a funcao princial (main)
if __name__ == "__main__":
    main()
