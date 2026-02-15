import sqlite3
import datetime

DB_NAME = "pfe_smart_system.db"

def init_db():
    """Creates the table if it doesn't exist."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS readings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp DATETIME,
            temperature REAL,
            humidity REAL
        )
    ''')
    conn.commit()
    conn.close()

def save_reading(temp, hum):
    """Saves a new reading."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute('INSERT INTO readings (timestamp, temperature, humidity) VALUES (?, ?, ?)', 
                   (now, temp, hum))
    conn.commit()
    conn.close()
    print(f"💾 Data Saved: {temp}°C | {hum}%")

def get_last_24h_data():
    """
    Fetches data from the last 24 hours for the Graph and AI.
    Returns a list of tuples: [(time, temp, hum), ...]
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # Calculate time 24 hours ago
    yesterday = datetime.datetime.now() - datetime.timedelta(hours=24)
    yesterday_str = yesterday.strftime("%Y-%m-%d %H:%M:%S")
    
    cursor.execute("SELECT timestamp, temperature, humidity FROM readings WHERE timestamp > ?", (yesterday_str,))
    data = cursor.fetchall()
    conn.close()
    return data

# Initialize on start
init_db()