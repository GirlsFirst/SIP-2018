// This version of the catbot uses the piezo as an input.

#include <Servo.h>                    // Include servo library

Servo servoRight;
Servo servoLeft;
int piezo = A0;

int sensorReading = 0;
int threshold = 10;

void moveKitty() {
  servoLeft.writeMicroseconds(1300);
  servoRight.writeMicroseconds(1700);
}

void stopKitty() {
  servoLeft.writeMicroseconds(1500);
  servoRight.writeMicroseconds(1500);
}

void setup() {
  // put your setup code here, to run once:
  servoLeft.attach(13);      // Attach left signal to pin 13
  servoRight.attach(12);     // Attach right signal to pin 12
  stopKitty();
  
  Serial.begin(9600);       // use the serial port
}

void loop() {
  // put your main code here, to run repeatedly:
  sensorReading = analogRead(piezo);

  //Serial.println(sensorReading);

  if (sensorReading <= threshold) {
    moveKitty();
    Serial.println("You pet me! <3");
    delay(1000);
  }
  stopKitty();
  delay(100);
}
