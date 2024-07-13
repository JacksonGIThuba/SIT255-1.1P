int ledPin = LED_BUILTIN;  // Use built-in LED pin
void setup() {
  pinMode(ledPin, OUTPUT);  // Set LED pin as output
  digitalWrite(ledPin, LOW);  // Ensure LED starts off
  Serial.begin(9600);  // Initialize serial communication
  //Randomise number recevied every time
  randomSeed(analogRead(A0));
}

void loop() {
  if (Serial.available() > 0) {
    int numBlinks = Serial.parseInt();  // Read the number of blinks from serial
    int sleep = random(5, 50); //generate random number
    Serial.println(sleep); //sleep for the generated number(this is the number python sees)
    // Blink the LED numBlinks times
    for (int i = 0; i < numBlinks; i++) {
      digitalWrite(ledPin, HIGH);  // Turn the LED on
      delay(500);  // Wait for 500 milliseconds
      digitalWrite(ledPin, LOW);  // Turn the LED off
      delay(500);  // Wait for 500 milliseconds
    }
  }
}