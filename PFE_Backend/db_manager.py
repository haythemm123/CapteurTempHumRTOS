import sqlite3
import datetime

DB_NAME = "pfe_data.db"

def init_db():
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS readings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT,
                temperature REAL,
                humidity REAL
            )
        ''')
        conn.commit()
        conn.close()
        print("[INIT] Database initialized.")
    except Exception as e:
        print(f"[ERROR] Database Error: {e}")

def save_to_db(temp, hum):
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        cursor.execute('''
            INSERT INTO readings (timestamp, temperature, humidity)
            VALUES (?, ?, ?)
        ''', (now, temp, hum))
        
        conn.commit()
        conn.close()
        print(f"[SAVED] {now} | T={temp} | H={hum}")
        
    except Exception as e:
        print(f"[ERROR] Failed to save data: {e}")


init_db()