#include <Servo.h>
Servo myservo;
#include <SoftwareSerial.h>
SoftwareSerial ESPserial(2, 3); // RX | TX
//Variables
String wifi_rx1;
String val;
const int led = 13;
String servo_state = "unlocked";
String led_state = "off";

void setup() {
  // put your setup code here, to run once:

  Serial.begin(9600);
  // Start the software serial for communication with the ESP8266
  ESPserial.begin(9600);

  myservo.attach(9);   //Attaching Servo Signal Pin to 9

  pinMode(led, OUTPUT); //Pin-13, where LED is attached
  pinMode(10, OUTPUT);

  digitalWrite(10, HIGH); //Turning Servo on at the beginning

  // unlock the door at the beginning
  myservo.write(50);
  delay(7);
  servo_state = "unlocked";
  delay(1000);
  digitalWrite(10, LOW); //Turning Servo back off


  digitalWrite(led, HIGH); //Light off in the begining
}

void loop() {




  // put your main code here, to run repeatedly:
  // listen for communication from the ESP8266 and then write it to the serial monitor

  if ( ESPserial.available())
  {
    // Serial.write( ESPserial.read() );
    if (wifi_rx1 == "o")
    {
      val = "o";
    }
    else if (wifi_rx1 == "f")
    {
      val = "f";
    }
    else if (wifi_rx1 == "l")
    {
      val = "l";
    }
    else if (wifi_rx1 == "u")
    {
      val = "u";
    }
  }

  wifi_rx1 = char(ESPserial.read());
  Serial.print("ST:");
  Serial.println(val  );
  Serial.println(digitalRead(13));

  // listen for user input and send it to the ESP8266
  if ( Serial.available() )       {
    ESPserial.write( Serial.read() );
  }
  if (val == "u" && servo_state == "locked") //If unlock command recieved and the door is previously locked then,
  {
    digitalWrite(10, HIGH); //Servo On
    
    // unlock
    myservo.write(50);
    delay(7);
    servo_state = "unlocked";
    delay(1000);
    
    digitalWrite(10, LOW); //Servo off
  }
  else if (val == "l" && servo_state == "unlocked") //If lock command recieved and the door is previously unlocked then,
  {
    digitalWrite(10, HIGH); //Servo on
    
    // lock
    myservo.write(150);
    delay(7);
    servo_state = "locked";
    delay(1000);
    
    digitalWrite(10, LOW); //Servo off
  }
  else
  {

  }

  if (val == "o" && led_state == "off") //If light on command recieved then
  {
    // Light On
    Serial.println("ooooooooooooooooooooooooo");
    digitalWrite(led, LOW);
    led_state = "on";
  }
  else if (val == "f" && led_state == "on") //If light off command recieved then
  {
    // Light Off
    Serial.println("fffffffffffffffffffffffff");
    digitalWrite(led, HIGH);
    led_state = "off";
  }
  else {

  }
}
