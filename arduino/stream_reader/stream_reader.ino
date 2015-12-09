
String event_string = "";
boolean event = false;

void setup() {

  Serial.begin(9600);
  Serial.println("Time to test some input/output for real!");
}

/* 
 *  For all intended purposes I think the SerialEvent() function of Arudino is broken
 *  This event fails to fire 
 */
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

void loop() {
  SerialEvent();
  if (event) {
    Serial.print("Just got new command: ");
    Serial.println(event_string);
    event_string = "";
    event = false;
  }
}
