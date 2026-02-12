#include <DHT.h>
#include <WiFi.h> 
#include <PubSubClient.h>

// ------------------- PIN DEFINITIONS -------------------
#define DHTPIN 4
#define DHTTYPE DHT22
#define GREEN_LED 18
#define RED_LED   22
#define BUZZER    23

// ------------------- WI-FI & MQTT -------------------
// ⚠️ REPLACE WITH YOUR REAL WIFI OR HOTSPOT ⚠️
const char* ssid = "HONOR X6c";        
const char* password = "haythem1234"; 

// MUST match the Python script broker
const char* mqtt_server = "broker.hivemq.com";  
const char* mqtt_topic = "pfe/sensor/data";

WiFiClient espClient;
PubSubClient client(espClient);
DHT dht(DHTPIN, DHTTYPE);

void setup_wifi() {
  delay(10);
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\nWiFi connected");
}

void reconnect() {
  while (!client.connected()) {
    Serial.print("Attempting MQTT connection...");
    String clientId = "ESP32Client-";
    clientId += String(random(0xffff), HEX);
    if (client.connect(clientId.c_str())) {
      Serial.println("connected");
    } else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 5 seconds");
      delay(5000);
    }
  }
}

void setup() {
  Serial.begin(9600);
  pinMode(GREEN_LED, OUTPUT);
  pinMode(RED_LED, OUTPUT);
  pinMode(BUZZER, OUTPUT);
  
  dht.begin();
  setup_wifi();
  client.setServer(mqtt_server, 1883);
}

void loop() {
  if (!client.connected()) {
    reconnect();
  }
  client.loop();  

  // Read Sensor
  float h = dht.readHumidity();
  float t = dht.readTemperature();

  if (isnan(h) || isnan(t)) {
    Serial.println("Failed to read from DHT sensor!");
    return;
  }

  // --- CREATE JSON PAYLOAD ---
  // We manually build the string: {"temperature": 25.5, "humidity": 60.2}
  String jsonPayload = "{\"temperature\": " + String(t) + ", \"humidity\": " + String(h) + "}";
  
  Serial.print("Sending MQTT: ");
  Serial.println(jsonPayload);

  // Send to the topic Python is listening to
  client.publish(mqtt_topic, jsonPayload.c_str());

  // --- HARDWARE ALERTS (LEDs) ---
  if (t > 30.0) { // Local Alert Threshold
    digitalWrite(RED_LED, HIGH);
    digitalWrite(GREEN_LED, LOW);
  } else {
    digitalWrite(RED_LED, LOW);
    digitalWrite(GREEN_LED, HIGH);
  }

  delay(2000); // Send data every 2 seconds
}