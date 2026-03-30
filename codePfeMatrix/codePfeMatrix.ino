#include <DHT.h>
#include <WiFi.h> 
#include <PubSubClient.h>
#include <MD_Parola.h>
#include <MD_MAX72xx.h>
#include <SPI.h>

// -------- CONFIG --------
#define HARDWARE_TYPE MD_MAX72XX::FC16_HW
#define MAX_DEVICES 8   // 4 modules = 8x32 display

// ------------------- PIN DEFINITIONS -------------------
#define DHTPIN 4
#define DHTTYPE DHT22
#define GREEN_LED 18
#define RED_LED   22
#define BUZZER    23
#define DATA_PIN 13
#define CLK_PIN  14
#define CS_PIN   15

MD_Parola display = MD_Parola(HARDWARE_TYPE, DATA_PIN, CLK_PIN, CS_PIN, MAX_DEVICES);

// ------------------- WI-FI & MQTT -------------------
// ⚠️ REPLACE WITH YOUR REAL WIFI OR HOTSPOT ⚠️
const char* ssid = "Galaxy A501AFE";        
const char* password = "juyi7252"; 

// MUST match the Python script broker
const char* mqtt_server = "192.168.43.101"; 
const char* mqtt_topic = "pfe/sensor/data";

WiFiClient espClient;
PubSubClient client(espClient);
DHT dht(DHTPIN, DHTTYPE);

unsigned long previousMillis = 0;
const unsigned long beepInterval = 300; // ms
bool buzzerState = false;

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

  digitalWrite(GREEN_LED, LOW);
  digitalWrite(RED_LED, LOW);
  digitalWrite(BUZZER, HIGH);

  display.begin();
  display.setIntensity(5);   // Brightness (0-15)
  display.displayClear();

  // Show static text first
  display.displayText("HELLO", PA_CENTER, 0, 0, PA_PRINT, PA_NO_EFFECT);
  
  dht.begin();
  setup_wifi();
  client.setServer(mqtt_server, 1883);

  
  Serial.println("ESP32 + DHT22 Monitoring Started...");
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
    Serial.println("⚠️ WARNING: Threshold exceeded!!!");
    Serial.println(jsonPayload);
    digitalWrite(BUZZER, LOW);
    Serial.println("Buzzer: on");

    if (display.displayAnimate()) {
      display.displayText("WARNING: THRESHOLD EXCEEDED!!!", PA_CENTER, 0, 0, PA_PRINT, PA_NO_EFFECT);
    }
  } else {
    digitalWrite(RED_LED, LOW);
    digitalWrite(GREEN_LED, HIGH);
    Serial.println("✅ Status: Normal");
    Serial.println(jsonPayload);
    digitalWrite(BUZZER, HIGH);
    buzzerState = false;

    char msg[50];
    sprintf(msg, "T:%.1f H:%.1f%%", t, h);

    // Show static text
    if (display.displayAnimate()) {
      display.displayText(msg, PA_CENTER, 0, 0, PA_PRINT, PA_NO_EFFECT);
    }
  }

  Serial.println("----------------------------------");
  delay(2000); // Send data every 2 seconds
}