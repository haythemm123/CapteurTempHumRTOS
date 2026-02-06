#include <DHT.h>
#include <WiFi.h> 
#include <PubSubClient.h>

// ------------------- Pin definitions -------------------
#define DHTPIN 4
#define DHTTYPE DHT22

#define GREEN_LED 18
#define RED_LED   19
#define BUZZER    23

// ------------------- Thresholds -------------------
#define HUMIDITY_THRESHOLD 60.0   // %
#define TEMP_THRESHOLD     50.0   // Celsius

const char* ssid = "Wokwi-GUEST";
const char* password = "";
const char* mqtt_server = "test.mosquitto.org";

WiFiClient espClient;
PubSubClient client(espClient);
unsigned long lastMsg = 0;
unsigned long lastLCDUpdate = 0;

DHT dht(DHTPIN, DHTTYPE);

// Buzzer timing
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


  randomSeed(micros());


  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
  }

  void callback(char* topic, byte* payload, unsigned int length) {
  Serial.print("Message arrived [");
  Serial.print(topic);
  Serial.print("] ");
  for (int i = 0; i < length; i++) {
    Serial.print((char)payload[i]);
  }}

  void reconnect() {
  while (!client.connected()) {
    Serial.print("Attempting MQTT connection...");
    String clientId = "ESP32Client-";
    clientId += String(random(0xffff), HEX);
    if (client.connect(clientId.c_str())) {
      Serial.println("Connected");
      client.publish("/CapteurTempHum/Publish", "Welcome");
      client.subscribe("/CapteurTempHum/Subscribe");
    } else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 5 seconds");
      delay(5000);
    }}
  }
void setup() {
  Serial.begin(115200);

  pinMode(GREEN_LED, OUTPUT);
  pinMode(RED_LED, OUTPUT);
  pinMode(BUZZER, OUTPUT);

  digitalWrite(GREEN_LED, LOW);
  digitalWrite(RED_LED, LOW);
  digitalWrite(BUZZER, LOW);

  dht.begin();
  setup_wifi();
  client.setServer(mqtt_server, 1883);
  client.setCallback(callback);
  Serial.println("ESP32 + DHT22 Monitoring Started...");
}

void loop() {
  if (!client.connected()) {
    reconnect();
  }
  client.loop();  

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

  String t = String(temperature, 2);
  client.publish("/CapteurTempHum/temp", t.c_str()); 
  String h = String(humidity, 1);
  client.publish("/CapteurTempHum/hum", h.c_str()); 

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
