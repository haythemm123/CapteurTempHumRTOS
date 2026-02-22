import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import io
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from datetime import datetime, timedelta
DB_NAME = "pfe_data.db"
SENDER_EMAIL = "haythemm.marnaoui@gmail.com"
SENDER_PASSWORD = "mnfpduepogawhuog"  
RECEIVER_EMAIL = "haythemm.marnaoui@gmail.com"

def generate_graph():
    """
    Reads DB, creates a graph image, returns the image data.
    """
    try:
     
        conn = sqlite3.connect(DB_NAME)
        
        
        query = "SELECT timestamp, temperature, humidity FROM readings"
        df = pd.read_sql_query(query, conn)
        conn.close()

        if df.empty:
            print("[REPORT] Database is empty. Cannot generate graph.")
            return None

        df['timestamp'] = pd.to_datetime(df['timestamp'])

        cutoff_time = datetime.now() - timedelta(hours=24)
        df = df[df['timestamp'] > cutoff_time]

        if df.empty:
            print("[REPORT] No data found in the last 24 hours.")
            return None

      
        plt.figure(figsize=(10, 5)) 
        
    
        plt.plot(df['timestamp'], df['temperature'], color='tab:red', label='Temp (C)')
        
        
        plt.plot(df['timestamp'], df['humidity'], color='tab:blue', label='Humidity (%)')

        plt.title(f"Daily Environment Report - {datetime.now().date()}")
        plt.xlabel("Time")
        plt.ylabel("Values")
        plt.legend() 
        plt.grid(True)
        plt.xticks(rotation=45)
        plt.tight_layout()
        img_buffer = io.BytesIO()
        plt.savefig(img_buffer, format='png')
        img_buffer.seek(0)
        plt.close() 
        
        print("[REPORT] Graph generated successfully.")
        return img_buffer

    except Exception as e:
        print(f"[ERROR] Graph generation failed: {e}")
        return None

def send_daily_email():
    """
    Generates the graph and sends it via email.
    """
    print("[REPORT] Starting daily report process...")
    
 
    graph_img = generate_graph()
    
    if graph_img is None:
        print("[REPORT] Aborting email (No graph).")
        return

    try:
     
        msg = MIMEMultipart()
        msg['Subject'] = f"Daily Report: {datetime.now().strftime('%Y-%m-%d')}"
        msg['From'] = SENDER_EMAIL
        msg['To'] = RECEIVER_EMAIL

     
        body_text = f"""
        <html>
            <body>
                <h2>Daily Environmental Log</h2>
                <p>Attached is the graph for the last 24 hours.</p>
                <p><b>System Status:</b> Online</p>
                <p><b>Generated at:</b> {datetime.now().strftime('%H:%M:%S')}</p>
            </body>
        </html>
        """
        msg.attach(MIMEText(body_text, 'html'))

      
        image = MIMEImage(graph_img.read())
        image.add_header('Content-Disposition', 'attachment', filename='daily_graph.png')
        msg.attach(image)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.send_message(msg)
        server.quit()
        
        print(f"[SUCCESS] Daily report sent to {RECEIVER_EMAIL}")

    except Exception as e:
        print(f"[ERROR] Email sending failed: {e}")


if __name__ == "__main__":
    send_daily_email()