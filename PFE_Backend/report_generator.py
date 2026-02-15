import matplotlib.pyplot as plt
import pandas as pd
import sqlite3
import io
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib
import datetime

# Configuration
DB_NAME = "pfe_smart_system.db"
SENDER_EMAIL = "haythemm.marnaoui@gmail.com"
SENDER_PASSWORD = "haef fbtg nxmn bdf" # Your App Password
RECEIVER_EMAIL = "haythemm.marnaoui@gmail.com"

def generate_daily_graph():
    """
    Reads DB, creates a graph image, saves it to memory buffer.
    """
    conn = sqlite3.connect(DB_NAME)
    
    # Load data into Pandas DataFrame (Perfect for AI later too)
    df = pd.read_sql_query("SELECT timestamp, temperature FROM readings", conn)
    conn.close()

    if df.empty:
        return None

    # Convert string time to real datetime
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    
    # Filter only last 24 hours
    cutoff = datetime.datetime.now() - datetime.timedelta(hours=24)
    df = df[df['timestamp'] > cutoff]

    if df.empty:
        return None

    # Plotting
    plt.figure(figsize=(10, 5))
    plt.plot(df['timestamp'], df['temperature'], color='red', marker='o', linestyle='-')
    plt.title(f"Temperature Report ({datetime.date.today()})")
    plt.xlabel("Time")
    plt.ylabel("Temperature (°C)")
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Save graph to a Bytes Buffer (Virtual File)
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.close()
    
    return buf

def send_daily_report():
    """
    Generates graph and sends email with attachment.
    """
    print("📊 Generating Daily Report...")
    graph_img = generate_daily_graph()
    
    if graph_img is None:
        print("⚠️ No data to report.")
        return

    # Email Setup
    msg = MIMEMultipart()
    msg['Subject'] = f"📅 Daily Log Report - {datetime.date.today()}"
    msg['From'] = SENDER_EMAIL
    msg['To'] = RECEIVER_EMAIL

    body = MIMEText("<h3>Daily Environmental Report</h3><p>Attached is the temperature trend for the last 24 hours.</p>", 'html')
    msg.attach(body)

    # Attach Image
    img = MIMEImage(graph_img.read())
    img.add_header('Content-Disposition', 'attachment', filename='daily_graph.png')
    msg.attach(img)

    # Send
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.send_message(msg)
        print("✅ Daily Report Sent!")
    except Exception as e:
        print(f"❌ Report Failed: {e}")