/**************************
  @Author Robert Powell
  @Class  SIE 558
***************************/

#include <Wire.h>
#include <Adafruit_Sensor.h>
#include "Adafruit_HTU21DF.h"
#include "Adafruit_TSL2591.h"

Adafruit_HTU21DF htu = Adafruit_HTU21DF();
Adafruit_TSL2591 tsl = Adafruit_TSL2591(2591);

String event_string = "";
boolean event = false;
float sensor_values[4];
int soilPower = 7;
int soilRead = 0;

/**************************************************************************/
/*
    Configures the gain and integration time for the TSL2591
*/
/**************************************************************************/
void configureSensor(void)
{
  tsl.setGain(TSL2591_GAIN_MED);      // 25x gain
  tsl.setTiming(TSL2591_INTEGRATIONTIME_100MS);  // shortest integration time (bright light)
  tsl2591Gain_t gain = tsl.getGain();
}

void setup() {

  pinMode(soilPower, OUTPUT); 
  Serial.begin(9600);

  if (!htu.begin()) {
    Serial.println("Couldn't find sensor!");
    while (1);
  }
  
  if (!tsl.begin()) 
  {
    Serial.println("No sensor found ... check your wiring?");
    while (1);
  }   
  configureSensor();
}

/**************************************************************************/
/*
    Performs a read using the Adafruit Unified Sensor API.
*/
/**************************************************************************/
float readLux(void)
{
  /* Get a new sensor event */ 
  sensors_event_t event;
  
  tsl.getEvent(&event);
  if ((event.light == 0) |
      (event.light > 4294966000.0) | 
      (event.light <-4294966000.0))
  {
    /* If event.light = 0 lux the sensor is probably saturated */
    /* and no reliable data could be generated! */
    /* if event.light is +/- 4294967040 there was a float over/underflow */
    return -1;
  }
  else
  {
    return event.light;
  }
}

int readSoil() {

  digitalWrite(soilPower, HIGH`);
  delay(50);
  int soil = analogRead(soilRead);
  digitalWrite(soilPower, LOW);
  return soil;
}

void SerialEvent() {
  while (Serial.available()) {

    char new_char = (char) Serial.read();

    if (new_char == '\n' & event_string.length() > 0) {
      event = true;
    }
    else if (new_char != '\n') {
      event_string += new_char;
    }


  }
}

void readSensors() {
  sensor_values[0] = htu.readTemperature();
  sensor_values[1] = htu.readHumidity();
  sensor_values[2] = readLux();
  sensor_values[3] = readSoil();
}

void loop() {
  SerialEvent();
  if (event) {
    if (event_string == "r") {
      readSensors();
      Serial.print(sensor_values[0]); Serial.print(",");
      Serial.print(sensor_values[1]); Serial.print(",");
      Serial.print(sensor_values[2]); Serial.print(",");
      Serial.print(sensor_values[3]); Serial.println();
    }
    event_string = "";
    event = false;
  }
}
