#include <Servo.h>

int rightWhiskerPin = 7;
int leftWhiskerPin = 5;
int rightWhiskerState = 0;
int leftWhiskerState = 0;
Servo servoRight;
Servo servoLeft;

void setup() {
  // put your setup code here, to run once:
  //tone(4, 3000, 1000);                      
  delay(1000);    
  pinMode(rightWhiskerPin, INPUT);
  pinMode(leftWhiskerPin, INPUT);
  Serial.begin(9600);
  servoLeft.attach(12);
  servoRight.attach(13);
  servoLeft.writeMicroseconds(1500);
  servoRight.writeMicroseconds(1300);
  
}

void loop() {
  // put your main code here, to run repeatedly:
  rightWhiskerState = digitalRead(rightWhiskerPin);
  leftWhiskerState = digitalRead(leftWhiskerPin);
  // whisker state is 1 if unpressed and 0 if pressed.
  if(rightWhiskerState == 0 && leftWhiskerState == 0){
    backward(1000);
    turnRight(800);
  }
  else if(leftWhiskerState == 0){
    backward(1000);
    turnRight(800);
  }
  else if(rightWhiskerState == 0){
    backward(1000);
    turnLeft(800);
  }
  else{
    forward(20);
  }
}

void stopnow(){
  servoLeft.writeMicroseconds(1500);
  servoRight.writeMicroseconds(1500);
}

void forward(int time)                       // Forward function
{
  servoLeft.writeMicroseconds(1700);         // Left wheel counterclockwise
  servoRight.writeMicroseconds(1300);        // Right wheel clockwise
  delay(time);                               // Maneuver for time ms
}

void turnLeft(int time)                      // Left turn function
{
  servoLeft.writeMicroseconds(1300);         // Left wheel clockwise
  servoRight.writeMicroseconds(1300);        // Right wheel clockwise
  delay(time);                               // Maneuver for time ms
}

void turnRight(int time)                     // Right turn function
{
  servoLeft.writeMicroseconds(1700);         // Left wheel counterclockwise
  servoRight.writeMicroseconds(1700);        // Right wheel counterclockwise
  delay(time);                               // Maneuver for time ms
}

void backward(int time)                      // Backward function
{
  servoLeft.writeMicroseconds(1300);         // Left wheel clockwise
  servoRight.writeMicroseconds(1700);        // Right wheel counterclockwise
  delay(time);                               // Maneuver for time ms
}
