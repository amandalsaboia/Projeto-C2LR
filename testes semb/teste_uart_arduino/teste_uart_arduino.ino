#include <SoftwareSerial.h>

SoftwareSerial comando( A0 , -1 ); //A0 Rx, -1 para nao usar nenhuma porta
int led=13;

void setup() {
  pinMode(led, OUTPUT);
  comando.begin(9600); //taxa de frequencia

}

void loop() {
  if(comando.available()){
    char c = comando.read(); // c recebe o que for lido da uart
    if (c == 'H'){
      digitalWrite(led, HIGH); // se receber H acende o led
    }
    else if (c=='L'){
      digitalWrite(led, LOW); // se teceber L apaga o led
    }
  }

}
