import paho.mqtt.client as mqtt
import json
import time
from email_manager import send_alert  
BROKER_ADDRESS = "broker.hivemq.com" 
PORT = 1883
TOPIC = "pfe/sensor/data"   #---


TEMP_THRESHOLD = 30.0  
EMAIL_COOLDOWN = 300        
last_email_time = 0         

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Successfully connected to local Mosquitto Broker!")
       
        client.subscribe(TOPIC)
        print(f" Listening for messages on topic: '{TOPIC}'")
    else:
        print(f" Connection failed with code {rc}")


def on_message(client, userdata, msg):
    global last_email_time
    
    try:
        payload = msg.payload.decode()
        print(f"New Data Received: {payload}")
        data = json.loads(payload)
        temp = float(data.get('temperature'))
        hum = float(data.get('humidity'))
        if temp > TEMP_THRESHOLD:
            print(f" High Temperature Detected: {temp}°C")
            current_time = time.time()
            if (current_time - last_email_time) > EMAIL_COOLDOWN:
                print("Sending Email Alert...")
                if send_alert(temp, hum):
                    print(" Email sent!")
                    last_email_time = current_time 
            else:
                print("Email skipped ")
                
    except json.JSONDecodeError:
        print(" Error: ESP32 sent bad data ")
    except Exception as e:
        print(f"Error: {e}")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
try:
    client.connect(BROKER_ADDRESS, PORT, 60)
except Exception as e:
    print(f" Could not connect to Mosquitto Error: {e}")
    exit()
client.loop_forever()