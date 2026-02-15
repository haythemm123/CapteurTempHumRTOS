import requests
BOT_TOKEN = "7730543089:AAFTV086DOClnWit6L2wS-rRCKZfwXy8kws"
CHAT_ID = "8404717409"
def send_telegram_alert(temperature, humidity):

    try:
   
        message = (
            f"🚨 *CRITICAL ALERT* 🚨\n\n"
            f"🌡 *Temp:* {temperature}°C\n"
            f"💧 *Humidity:* {humidity}%\n\n"
            f"⚠️ _Check the sensor immediately!_"
        )
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        payload = {
            "chat_id": CHAT_ID,
            "text": message,
            "parse_mode": "Markdown" 
        }
       
        response = requests.post(url, json=payload)
        
        if response.status_code == 200:
            print(" Telegram Message Sent!")
            return True
        else:
            print(f" Telegram Error: {response.text}")
            return False

    except Exception as e:
        print(f" Connection Error: {e}")
        return False

if __name__ == "__main__":
    send_telegram_alert(45.5, 30.0)