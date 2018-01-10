
#include <Servo.h>                           // Include servo library.

Servo servoLeft;                             // Declare left servo signal.
Servo servoRight;                            // Declare right servo signal.


// Declare pin that the piezo is connected to.
int PIEZOPIN = 5;

// DECLARE LED PINS HERE
int LED1 = 2;
int LED2 = 3;
int LED3 = 4;

// One octave of notes between A4 and A5, for Piezo Greeting
int note_A4 = 440;
int note_As4 = 466; int note_Bb4 = note_As4;
int note_B4 = 494;
int note_C5 = 523;
int note_Cs5 = 554; int note_Db5 = note_Cs5;
int note_D5 = 587;
int note_Ds5 = 622; int note_Eb5 = note_Ds5;
int note_E5 = 659;
int note_F5 = 698;
int note_Fs5 = 740; int note_Gb5 = note_Fs5;
int note_G5 = 784;
int note_Gs5 = 830; int note_Ab5 = note_Gs5;

void setup()
{
  pinMode(PIEZOPIN, OUTPUT);                 // Attach piezo to pin 5. 
  
  servoLeft.attach(13);                      // Attach left signal to pin 13.
  servoRight.attach(12);                     // Attach right signal to pin 12.
  servoLeft.writeMicroseconds(1500);         // Stop left servo.
  servoRight.writeMicroseconds(1500);        // Stop right servo.
  
  pinMode(LED1, OUTPUT);                     // Set all LED pins to output.  
  pinMode(LED2, OUTPUT);
  pinMode(LED3, OUTPUT);
  
}  

// Example function that defines a dance move.
void twirlStopShake(){

  // Twirl
  servoLeft.writeMicroseconds(1700);
  delay(4000);

  // Stop
  servoLeft.writeMicroseconds(1500);
  delay(1000);

  // Shake
  for(int x = 1; x < 20; x += 1){
    servoLeft.writeMicroseconds(1700);
    servoRight.writeMicroseconds(1300);
    delay(50);

    servoLeft.writeMicroseconds(1300);
    servoRight.writeMicroseconds(1700);
    delay(50);
  }

  // Stop motion
  servoLeft.writeMicroseconds(1500);
  servoRight.writeMicroseconds(1500);

}

// Example function that results in 3 LEDs lighting up in sequence.
void ledSwirl(){
  
  for( int x = 0; x < 3; x++){
      digitalWrite(LED1, HIGH);
      delay(100);
      digitalWrite(LED2, HIGH);
      delay(100);
      digitalWrite(LED3, HIGH);
      digitalWrite(LED1, LOW);
      delay(100);
      digitalWrite(LED2, LOW);
      delay(100);
      digitalWrite(LED3, LOW);
  }
}

// Sample piezo greeting, using the note declarations from above.
void piezoGreeting(){

  for( int x = 0; x < 5; x++){
      tone(PIEZOPIN, note_C5, 200);
      delay(500);
      tone(PIEZOPIN, note_E5, 200);
      delay(500);
      tone(PIEZOPIN, note_G5, 200);
      delay(500);
  } 
}

// Sample main program.
// The robot will play its greeting, then flash its lights, then dance.
// If you want the lights and the dance to happen simultaneously,
// those two functions must be combined because they currently execute
// sequentially.
void loop()
{
  piezoGreeting();

  for( int x = 0; x < 5; x++){
      ledSwirl();   
      twirlStopShake();
  }

  delay(1000);
}



