// Let There Be Light: Part 2

int pin = 10; // Make sure your circuit is using digital pin 10!

void setup() {
  // put your setup code here, to run once:
  pinMode(pin, OUTPUT);

}

void loop() {
  // put your main code here, to run repeatedly:

  digitalWrite(pin, HIGH);
  delay(500);
  digitalWrite(pin, LOW);
  delay(500);
}
