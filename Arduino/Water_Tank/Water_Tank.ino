String State;

int x;
int y;
int z;

int upper = 62;
int lower = 70;

const int trigPin = 9;
const int echoPin = 10;
long duration;
int distance;

void setup() {
  // put your setup code here, to run once:
  pinMode(13, OUTPUT);
  pinMode(trigPin, OUTPUT); // Sets the trigPin as an Output
  pinMode(echoPin, INPUT); // Sets the echoPin as an Input
  Serial.begin(9600);

  x = 13;
  y = 31;
  z = 14;
}

void Time() {
  z = z + 1;
  delay(1000);
  if (z == 60) {
    z = 0;
    y = y + 1;
  }
  if (y == 60) {
    y = 0;
    x = x + 1;
  }
  if (x == 24) {
    x = 0;
  }

}

void loop() {
  // put your main code here, to run repeatedly:
  // Clears the trigPin
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  // Sets the trigPin on HIGH state for 10 micro seconds
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  // Reads the echoPin, returns the sound wave travel time in microseconds
  duration = pulseIn(echoPin, HIGH);
  // Calculating the distance
  distance = duration * 0.034 / 2;
  // Prints the distance on the Serial Monitor
  Serial.print("Distance: ");
  Serial.println(distance);
  Time();

  if ((distance > upper) && (distance < lower) ) {
    delay(2000);
    if ((distance > upper) && (distance < lower) ) {
      State = "on";
    }
  }

  if ((State == "on") && (10 < x) && (x < 20))
  {
    delay(1000);
    if ((State == "on") && (10 < x) && (x < 20))
    {
      digitalWrite(13, LOW);
    }

  }

  if (distance < upper) {
    digitalWrite(13, HIGH);
    State = "off";

  }
}
