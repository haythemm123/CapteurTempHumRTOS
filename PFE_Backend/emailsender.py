import smtplib
from email.message import EmailMessage
SENDER_EMAIL = "haythemm.marnaoui@gmail.com"
SENDER_PASSWORD = "mnfpduepogawhuog"  
RECEIVER_EMAIL = "haythemm.marnaoui@gmail.com"

def send_alert(temperature, humidity):
    """
    This function is called by your main script.
    It connects to the email server and sends the message.
    """
    msg = EmailMessage()
    msg.set_content(f" ALERT: High temperature detected!\n\n"
                    f"Temperature: {temperature}°C\n"
                    f"Humidity: {humidity}%\n\n"
                    f"Check the sensor immediately.")
    
    msg['Subject'] = " Temperature Alert!"
    msg['From'] = SENDER_EMAIL
    msg['To'] = RECEIVER_EMAIL

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()  
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.send_message(msg)
        return True
    except Exception as e:
        print(f"SMTP Error: {e}")
        return False