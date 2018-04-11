#define S0 4
#define S1 5
#define S2 6
#define S3 7
#define sensorOut A1
int value = 0;
void setup() {
  pinMode(S0, OUTPUT);
  pinMode(S1, OUTPUT);
  pinMode(S2, OUTPUT);
  pinMode(S3, OUTPUT);
  pinMode(sensorOut, INPUT);
  
  // Setting frequency-scaling to 20%
  digitalWrite(S0,HIGH);
  digitalWrite(S1,LOW);
  
  Serial.begin(9600);
}

void loop()
{
  digitalWrite(S2, HIGH);
  digitalWrite(S3, LOW);
  value = pulseIn(sensorOut, LOW);
  delay(70);
  if(185<value && 210>value)
    Serial.println("Crna");
  else if(130<value && 150>value)
    Serial.println("Plavu");
  else if(151<value && 165>value)
    Serial.println("Zuta");
  else if(165<value && 180>value)
  {
    digitalWrite(S2,HIGH);
    digitalWrite(S3,HIGH);
    value = pulseIn(sensorOut, LOW);
    if(value<202)
      Serial.println("Zelena");
    else if(value>202)
      Serial.println("Narandzasta");
  }
  else
    Serial.println(value);
}
