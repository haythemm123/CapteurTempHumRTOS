#include <DHT.h>

// ------------------- Pin definitions -------------------
#define DHTPIN 4
#define DHTTYPE DHT22

#define GREEN_LED 18
#define RED_LED   19
#define BUZZER    23

// ------------------- Thresholds -------------------
#define HUMIDITY_THRESHOLD 60.0   // %
#define TEMP_THRESHOLD     50.0   // Celsius

DHT dht(DHTPIN, DHTTYPE);

// Buzzer timing
unsigned long previousMillis = 0;
const unsigned long beepInterval = 300; // ms
bool buzzerState = false;

void setup() {
  Serial.begin(115200);

  pinMode(GREEN_LED, OUTPUT);
  pinMode(RED_LED, OUTPUT);
  pinMode(BUZZER, OUTPUT);

  digitalWrite(GREEN_LED, LOW);
  digitalWrite(RED_LED, LOW);
  digitalWrite(BUZZER, LOW);

  dht.begin();

  Serial.println("ESP32 + DHT22 Monitoring Started...");
}

void loop() {
  float humidity = dht.readHumidity();
  float temperature = dht.readTemperature();

  if (isnan(humidity) || isnan(temperature)) {
    Serial.println("Failed to read from DHT sensor!");
    return;
  }

  Serial.print("Humidity: ");
  Serial.print(humidity);
  Serial.print(" %  |  ");

  Serial.print("Temperature: ");
  Serial.print(temperature);
  Serial.println(" °C");

  bool alert = (humidity > HUMIDITY_THRESHOLD || temperature > TEMP_THRESHOLD);

  if (alert) {
    // ALERT MODE
    digitalWrite(RED_LED, HIGH);
    digitalWrite(GREEN_LED, LOW);

    // Non-blocking buzzer beep
    unsigned long currentMillis = millis();
    if (currentMillis - previousMillis >= beepInterval) {
      previousMillis = currentMillis;
      buzzerState = !buzzerState;
      digitalWrite(BUZZER, buzzerState);
    }

    Serial.println("⚠️ WARNING: Threshold exceeded!");
  } else {
    // NORMAL MODE
    digitalWrite(RED_LED, LOW);
    digitalWrite(GREEN_LED, HIGH);
    digitalWrite(BUZZER, LOW);
    buzzerState = false;

    Serial.println("✅ Status: Normal");
  }

  Serial.println("----------------------------------");
  delay(2000); // Sensor read interval
}
