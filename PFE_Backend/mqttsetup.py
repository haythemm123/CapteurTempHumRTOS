import paho.mqtt.client as mqtt
import json
import time
import schedule
from emailsender import send_alert as send_email
from telegram_sender import send_telegram_alert as send_telegram
from db_manager import save_to_db 
from report_generator import send_daily_email
BROKER_ADDRESS = "broker.hivemq.com" 
PORT = 1883
TOPIC = "pfe/sensor/data" 

TEMP_THRESHOLD = 30.0   
HUM_THRESHOLD = 70.0    
ALERT_COOLDOWN = 300    
last_alert_time = 0


def on_connect(client, userdata, flags, reason_code, properties):
    if reason_code == 0:
        print("[SYSTEM] Connected to Broker!")
        client.subscribe(TOPIC)
    else:
        print(f"[ERROR] Connection failed: {reason_code}")

def on_message(client, userdata, msg):
    global last_alert_time
    try:
        payload = msg.payload.decode()
        data = json.loads(payload)
        temp = float(data.get('temperature'))
        hum = float(data.get('humidity'))
        
        print(f"[DATA] T={temp} C | H={hum} %")
        
        # 1. Save to Database
        save_to_db(temp, hum)
        
        # 2. Check Alerts
        is_temp_bad = temp > TEMP_THRESHOLD
        is_hum_bad = hum > HUM_THRESHOLD
        
        if is_temp_bad or is_hum_bad:
            alert_reason = "High Temp!" if is_temp_bad else "High Humidity!"
            print(f"[ALERT] {alert_reason}")
            
            current_time = time.time()
            if (current_time - last_alert_time) > ALERT_COOLDOWN:
                print("[NOTIFY] Sending Alerts...")
                send_email(temp, hum)
                send_telegram(temp, hum)
                last_alert_time = current_time 
                
    except Exception as e:
        print(f"[ERROR] {e}")

# --- SCHEDULER SETUP ---
def run_scheduler():
    print("[SCHEDULER] Daily Report scheduled.")
    
    # Run once every 24 hours at 23:59
    schedule.every().day.at("23:59").do(send_daily_email)
    
    # --- TEST MODE (Uncomment to test now) ---
    # schedule.every(1).minutes.do(send_daily_email)

# --- MAIN EXECUTION ---
if __name__ == "__main__":
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    client.on_connect = on_connect
    client.on_message = on_message
    
    print("[SYSTEM] Starting PFE Master System...")
    
    try:
        client.connect(BROKER_ADDRESS, PORT, 60)
        
        # Start MQTT in background
        client.loop_start() 
        
        # Start Scheduler
        run_scheduler()
        
        # Loop forever to keep script alive
        while True:
            schedule.run_pending()
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("[SYSTEM] Stopping...")
        client.loop_stop()
        client.disconnect()
    except Exception as e:
        print(f"[FATAL ERROR] {e}")