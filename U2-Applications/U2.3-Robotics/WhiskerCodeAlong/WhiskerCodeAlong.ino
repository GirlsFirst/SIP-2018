/* Whisker Code Along
 * Part 1: 
 * We will show students how to set up the whisker inputs.
 * We will show them how to print values from the input.
 * 
 * Part 2:
 * We will show students how to use conditionals with inputs.
*/

// PART 1
// We start by declaring where we've plugged in the whiskers.
// This can be different for different students, however,
// They should all be in digital pins!
int leftWhisker = 5;
int rightWhisker = 7;

void setup() {
  // PART 1
  // We always start opening up the serial port for writing.
  // If we don't do this, we can't see any values!
  Serial.begin(9600);

  // PART 1
  // We also need to declare these digital pins as INPUT
  // in order to read what values they are.
  pinMode(leftWhisker, INPUT);
  pinMode(rightWhisker, INPUT);
}

void loop() {
  // PART 1
  // We start by using our new information: digitalRead().
  // This less us see get information from the whisker sensor.
  int leftWhiskerValue = digitalRead(leftWhisker);
  int rightWhiskerValue = digitalRead(rightWhisker);

  // PART 1
  // Then we print out the information.
  // Note the use of print() vs println() in order 
  // to make the output very easy to read.
  Serial.print("Left :");
  Serial.print(leftWhiskerValue);
  Serial.print(" Right :");
  Serial.print(rightWhiskerValue);
  Serial.println("");

  // PART 2
  // Explain that just printing the values
  // isn't enough information. Let's try using
  // conditionals to print what information we
  // learn from the values.
  // Replace the prints above with:
  if(leftWhiskerValue == 0 && rightWhiskerValue == 0) {
    Serial.println("Left and Right pressed!");
  } else if(leftWhiskerValue == 0) {
    Serial.print("Left pressed!");
  } else if(rightWhiskerValue == 0) {
    Serial.print("Right pressed!");
  } else {
    Serial.print("No whiskers pressed!");
  }
  
  // PART 1
  // Avoid overwhelming the serial buffer.
  // Explain to students that this is like
  // lights on a highway entrance ramp --
  // preventing too many cars from going
  // on the highway at the same time to avoid
  // traffic jams.
  delay(100);
}
