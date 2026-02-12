import paho.mqtt.client as mqtt
import json
import time
from emailsender import send_alert as send_email
from telegram_sender import send_telegram_alert as send_telegram


BROKER_ADDRESS = "broker.hivemq.com" 
PORT = 1883
TOPIC = "pfe/sensor/data" 
TEMP_THRESHOLD = 30.0   
HUM_THRESHOLD = 100    
ALERT_COOLDOWN = 300    
last_alert_time = 0


def on_connect(client, userdata, flags, reason_code, properties):
    if reason_code == 0:
        print(" Connected to Broker!")
        client.subscribe(TOPIC)
        print(f" Listening on: {TOPIC}")
    else:
        print(f" Connection failed: {reason_code}")


def on_message(client, userdata, msg):
    global last_alert_time
    
    try:
        
        payload = msg.payload.decode()
        data = json.loads(payload)
        
       
        temp = float(data.get('temperature'))
        hum = float(data.get('humidity'))
        
        print(f" Data: T={temp}°C | H={hum}%")
        
        
        is_temp_bad = temp > TEMP_THRESHOLD
        is_hum_bad = hum > HUM_THRESHOLD
        
        if is_temp_bad or is_hum_bad:
            
            alert_reason = ""
            if is_temp_bad and is_hum_bad:
                alert_reason = "CRITICAL: Both Temp & Humidity High!"
            elif is_temp_bad:
                alert_reason = "WARNING: High Temperature!"
            elif is_hum_bad:
                alert_reason = "WARNING: High Humidity!"
            
            print(f" {alert_reason}")
            
            
            current_time = time.time()
            if (current_time - last_alert_time) > ALERT_COOLDOWN:
                print(" Sending Notifications...")
                
                
                send_email(temp, hum)
                
                
                send_telegram(temp, hum)
                
                print(" Alerts sent!")
                last_alert_time = current_time 
            else:
                print(" Alert active, but cooldown is running.")
                
    except Exception as e:
        print(f" Error: {e}")


client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_message = on_message

print(" System Starting...")
try:
    client.connect(BROKER_ADDRESS, PORT, 60)
    client.loop_forever()
except Exception as e:
    print(f"Connection Error: {e}")