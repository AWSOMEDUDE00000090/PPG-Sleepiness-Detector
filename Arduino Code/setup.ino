void setup()
{
    pinMode(LED_BUILTIN, OUTPUT);
    Serial.begin(9600);
}

void loop()
{
    digitalWrite(LED_BUILTIN, HIGH);
}