from flask import Flask, jsonify
import sqlite3
import os

app = Flask(__name__)

# Force the API to look in the folder where the script lives
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_NAME = os.path.join(BASE_DIR, "pfe_data.db")

def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row 
    return conn

@app.route('/history', methods=['GET'])
def get_history():
    try:
        # Debugging print to show exactly where the API is looking
        print(f"[DEBUG] Checking database at: {DB_NAME}")
        
        if not os.path.exists(DB_NAME):
            return jsonify({"error": f"Database not found at {DB_NAME}"}), 404

        conn = get_db_connection()
        cursor = conn.cursor()
        
        # Matches your table structure
        cursor.execute('SELECT timestamp, temperature, humidity FROM readings ORDER BY id DESC LIMIT 20')
        rows = cursor.fetchall()
        conn.close()

        history_list = []
        for row in rows:
            history_list.append({
                "time": row["timestamp"].split(" ")[1], # Extracting time part
                "temp": row["temperature"],
                "hum": row["humidity"]
            })
        
        return jsonify(history_list[::-1]) # Oldest to newest for chart

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)