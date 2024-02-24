#include <LiquidCrystal.h>
LiquidCrystal lcd(8,9,10,11,12,13);
#include <SoftwareSerial.h>
SoftwareSerial mySerial(5,4); //rx, tx
//#include <TinyGPS++.h>
//int RXPin = 4;
//int TXPin = 5;
//int GPSBaud = 9600;
//TinyGPSPlus gps;
//SoftwareSerial gpsSerial(RXPin, TXPin);
int contrast=75;
char w;

// constants won't change
const int TRIG_PIN = 2; // Arduino pin connected to Ultrasonic Sensor's TRIG pin
const int ECHO_PIN = 3; // Arduino pin connected to Ultrasonic Sensor's ECHO pin
const int DISTANCE_THRESHOLD_1 = 10; // centimeters
const int DISTANCE_THRESHOLD_2 = 20; // centimeters
const int DISTANCE_THRESHOLD_3 = 30; // centimeters

// variables will change:
float duration_us, distance_cm;

void setup() {
  analogWrite(6,contrast);
//  gpsSerial.begin(GPSBaud);
  Serial.begin (9600);// initialize serial port
  pinMode(TRIG_PIN, OUTPUT); // set arduino pin to output mode
  pinMode(ECHO_PIN, INPUT);  // set arduino pin to input mode
  pinMode(A0, OUTPUT);  // set arduino pin to output mode
  pinMode(A1, OUTPUT);  // set arduino pin to output mode
  pinMode(A2, OUTPUT);  // set arduino pin to output mode
  lcd.begin(16, 2);
  lcd.clear();

  mySerial.begin(9600);
  delay(1000);
//  Serial.println("Initializing");
//  delay(1000);
//  mySerial.println("AT");
//  updateSerial();
//  mySerial.println("AT+CMGF=1");
//  updateSerial();
//  mySerial.println("AT+CMGS=\"+919591505592\"");
//  updateSerial();
//  mySerial.print("Smartbin status update"); //text content
//  updateSerial();
//  mySerial.write(26);
  
}

void loop() {
  // generate 10-microsecond pulse to TRIG pin
  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);

  // measure duration of pulse from ECHO pin
  duration_us = pulseIn(ECHO_PIN, HIGH);
  // calculate the distance
  distance_cm = 0.017 * duration_us;

  if(distance_cm < DISTANCE_THRESHOLD_1 && distance_cm>0){
    digitalWrite(A0, HIGH); // turn on LED
    digitalWrite(A1, HIGH);
    digitalWrite(A2, HIGH);
    lcd.setCursor(0, 0);
    lcd.print(" Bin is full");
    lcd.setCursor(0, 1);
    lcd.print("please empty bin");
    delay(1000);
    lcd.clear();

    if (mySerial.available()){ // for serial monitor
      w=mySerial.read();
      Serial.println(w); //pc
      delay(10);
    }

    if (Serial.available()){ // for device app
      w=Serial.read();
      mySerial.println(w); //phone
      delay(10);
    }

    mySerial.println("the smartbin is full");
    mySerial.println("Please empty the bin");
    mySerial.println();
    delay(2000);
  }
  
  if(distance_cm < DISTANCE_THRESHOLD_2 && distance_cm >= DISTANCE_THRESHOLD_1){
    digitalWrite(A0, HIGH); // turn on LED
    digitalWrite(A1, HIGH);
    digitalWrite(A2, LOW);
    lcd.setCursor(0, 0);
    lcd.print(" Bin is half");
    lcd.setCursor(0, 1);
    lcd.print("please empty bin");
    delay(1000);
    lcd.clear();
  }
  if(distance_cm < DISTANCE_THRESHOLD_3 && distance_cm >= DISTANCE_THRESHOLD_2){
    digitalWrite(A0, HIGH); // turn on LED
    digitalWrite(A1, LOW);
    digitalWrite(A2, LOW);
    lcd.setCursor(0, 0);
    lcd.print(" Bin is empty");
    delay(1000);
    lcd.clear();
  }
//  else{
//    digitalWrite(A0, LOW);  // turn off LED
//    digitalWrite(A1, LOW);
//    digitalWrite(A2, LOW);
//  }
  // print the value to Serial Monitor
  Serial.print("distance: ");
  Serial.print(distance_cm);
  Serial.println(" cm");

  delay(500);

//  // This sketch displays information every time a new sentence is correctly encoded.
//  while (gpsSerial.available() > 0)
//    if (gps.encode(gpsSerial.read())){
//      displayInfo();
//    }
//   // over the software serial port, show a "No GPS detected" error
//    if (millis() > 5000 && gps.charsProcessed() < 10)
//    {
//      Serial.println("No GPS detected");
//      while(true);
//    }
//}
}

//void updateSerial()
//{
//  delay(500);
//  while (Serial.available()) 
//  {
//    mySerial.write(Serial.read()); //Forward what Serial received to Software Serial Port
//  }
//  while(mySerial.available()) 
//  {
//    Serial.write(mySerial.read()); //Forward what Software Serial received to Serial Port
//  }
//}

//void displayInfo()
//{
//  if (gps.location.isValid())
//  {
//    Serial.print("Latitude: ");
//    Serial.println(gps.location.lat(), 6);
//    Serial.print("Longitude: ");
//    Serial.println(gps.location.lng(), 6);
//    Serial.print("Altitude: ");
//    Serial.println(gps.altitude.meters());
//  }
//  else
//  {
//    Serial.println("Location: Not Available");
//  }
//  
//  Serial.print("Date: ");
//  if (gps.date.isValid())
//  {
//    Serial.print(gps.date.month());
//    Serial.print("/");
//    Serial.print(gps.date.day());
//    Serial.print("/");
//    Serial.println(gps.date.year());
//  }
//  else
//  {
//    Serial.println("Not Available");
//  }
//
//  Serial.print("Time: ");
//  if (gps.time.isValid())
//  {
//    if (gps.time.hour() < 10) Serial.print(F("0"));
//    Serial.print(gps.time.hour());
//    Serial.print(":");
//    if (gps.time.minute() < 10) Serial.print(F("0"));
//    Serial.print(gps.time.minute());
//    Serial.print(":");
//    if (gps.time.second() < 10) Serial.print(F("0"));
//    Serial.print(gps.time.second());
//    Serial.print(".");
//    if (gps.time.centisecond() < 10) Serial.print(F("0"));
//    Serial.println(gps.time.centisecond());
//  }
//  else
//  {
//    Serial.println("Not Available");
//  }
//
//  Serial.println();
//  Serial.println();
//  delay(1000);
//}