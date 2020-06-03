const int flexPin = A1; //Define analog input pin to measure
                        //flex sensor position. 


void setup() 
{ 

  Serial.begin(9600); //Set serial baud rate to 9600 bps


} 


void loop() 
{ 
  int flexPosition;    // Input value from the analog pin.
  int servoPosition;   // Output value to the servo.

  // Read the position of the flex sensor (0 to 1023):

  flexPosition = analogRead(flexPin);

  // Now we'll command the servo to move to that position:




  Serial.print("sensor: ");
  Serial.print(flexPosition);
  


  delay(500);  // wait 20ms between servo updates
} 
