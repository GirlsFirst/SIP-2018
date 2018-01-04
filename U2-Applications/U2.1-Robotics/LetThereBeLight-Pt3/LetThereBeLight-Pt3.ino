// Let There Be Light: Part 3

int unit = 300;
int pin = 10; // Make sure your circuit is using digital pin 10!

void setup() {
  // put your setup code here, to run once:
  pinMode(pin, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:

  /* 
   *  Secret message: "GWC ROCKS."
   *  Letters needed: C G K O R S W
   */

  // Spell out message:
  // "GWC "
  flashG();
  delay(unit * 3); // 3 units between each letter
  flashW();
  delay(unit * 3);
  flashC();
  flashSpace(); // 7 units between each word

  // "ROCKS. "
  flashR();
  delay(unit * 3);
  flashO();
  delay(unit * 3);
  flashC();
  delay(unit * 3);
  flashK();
  delay(unit * 3);
  flashS();
  delay(unit * 3);
  flashPeriod();
  flashSpace();
  
}

void dot() {
  digitalWrite(pin, HIGH);
  delay(unit);
  digitalWrite(pin, LOW);
}

void dash() {
  digitalWrite(pin, HIGH);
  delay(unit * 3);
  digitalWrite(pin, LOW);
}

// Functions to flash a specific letter
void flashC() {
  // -.-.
  dash();
  delay(unit);
  dot();
  delay(unit);
  dash();
  delay(unit);
  dot();
}

void flashG() {
  // --.
  dash();
  delay(unit);
  dash();
  delay(unit);
  dot();
}

void flashK() {
  // -.-
  dash();
  delay(unit);
  dot();
  delay(unit);
  dash();
}

void flashO() {
  // ---
  dash();
  delay(unit);
  dash();
  delay(unit);
  dash();
}

void flashR() {
  // .-.
  dot();
  delay(unit);
  dash();
  delay(unit);
  dot();
}

void flashS() {
  // ...
  dot();
  delay(unit);
  dot();
  delay(unit);
  dot();
}

void flashW() {
  // .--
  dot();
  delay(unit);
  dash();
  delay(unit);
  dash();
}

void flashSpace() {
  // 7 units
  delay(unit * 7);
}

void flashPeriod() {
  // .-.-.-
  dot();
  delay(unit);
  dash();
  delay(unit);
  dot();
  delay(unit);
  dash();
  delay(unit);
  dot();
  delay(unit);
  dash();
}

