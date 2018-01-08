
int piezo = A0;

int sensorReading = 0;
int threshold = 10;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  sensorReading = analogRead(piezo);

  Serial.println(sensorReading);

  if (sensorReading <= threshold) {
    Serial.println("Knock!");
    delay(1000);
  }
  
  delay(100);
}
