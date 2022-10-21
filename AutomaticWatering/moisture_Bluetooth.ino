
#define SensorPin A0
#define PumpPin 10
float sensorValue = 0; 

void setup() {
  // Setup serial for monitor
  Serial.begin(9600); 
  // Setup Serial1 for BlueTooth
  Serial1.begin(9600);
  pinMode(PumpPin, OUTPUT);
// Default communication rate of the Bluetooth module
}

void loop() {

 sensorValue = analogRead(SensorPin); 
 sensorValue = map(sensorValue,550,10,0,100); 
 Serial.println(sensorValue);
 Serial1.println(sensorValue);
 delay(1000);
  if(sensorValue > 80){
      digitalWrite(PumpPin, HIGH);
      Serial.println("PUMP ON");
  } else if(sensorValue < 80){
      digitalWrite(PumpPin, LOW);
      Serial.println("PUMP OFF");
}
 delay(1000); 
  if(Serial1.available() > 0){ // Checks whether data is coming from the serial port
    Serial.print(sensorValue);
    Serial1.println(sensorValue);    
    delay(1000);
        String str = Serial1.readString().substring(3);
   Serial.println(str);
   if(str.indexOf("START")!=-1){
      Serial.println("PUMP ON Manually");
      digitalWrite(PumpPin, HIGH);
      Serial.println("Manual Pump Operating");
      delay(4000);
       
 }
}
}
