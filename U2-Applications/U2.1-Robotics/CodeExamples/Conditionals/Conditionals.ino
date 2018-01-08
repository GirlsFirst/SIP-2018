



int aNumber;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);       // use the serial port
  aNumber = 0;
}

void loop() {
  if(aNumber < 5) {
    Serial.println("a number is less than five");
  } else if(aNumber == 5) {
    Serial.println("a number is five");
  } else {
    Serial.println("a number more than five");
  }
  aNumber = aNumber + 1;
}
