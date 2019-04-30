



int sensor1 = 3;
int sensor2 = 4;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);       // use the serial port

  pinMode(sensor1, INPUT);
  pinMode(sensor2, INPUT);
}

void loop() {
  if(digitalRead(sensor1) == HIGH && digitalRead(sensor2) == HIGH) {
    Serial.println("Both sensors are being sensed!");
  }
  if(digitalRead(sensor1) == HIGH || digitalRead(sensor2) == HIGH) {
    Serial.println("At least one sensors is being sensed!");
  }
  if(!(digitalRead(sensor1) == HIGH)) {
    Serial.println("Sensor1 is not being sensed!");
  }
  
  delay(100);
}
