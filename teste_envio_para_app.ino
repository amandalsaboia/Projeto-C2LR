#include <SoftwareSerial.h>

SoftwareSerial comando( A0 , -1 ); //cria nova porta uart no pino A0
void setup() {
  comando.begin (9600); //recebe informacoes da rasp
  Serial.begin(9600); //recebe e envia informacoes dos pinos 0 e 1 (onde esta conectado o bluetooth)
}

void loop() {
    if(comando.available()>0){
    char c =  comando.read(); // c recebe informacoes da rasp
    if (c == 'h'){  //se receber h envia help para o android via bluetooth
      Serial.write("help");
      c == " ";
    }
  }

}
