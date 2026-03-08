import sqlite3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from datetime import datetime, timedelta
import io
import os


current_dir = os.path.dirname(os.path.abspath(__file__))
DB_NAME = os.path.join(current_dir, "..", "PFE_Backend", "pfe_data.db")
def train_and_predict():
    print("[AI] Loading data from database...")
    
    # 1. Connect to Database
    conn = sqlite3.connect(DB_NAME)
    query = "SELECT timestamp, temperature FROM readings"
    df = pd.read_sql_query(query, conn)
    conn.close()

    # Check if we have enough data (Need at least 10 points)
    if len(df) < 10:
        print("[AI ERROR] Not enough data to train! Let the system run for 10 minutes first.")
        return

    # 2. Preprocessing (Convert Time to Numbers)
    # The AI cannot read "2023-10-25". It needs numbers like "Hour: 14".
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    
    # We create "Features" (X)
    # We convert timestamp to "Minutes since start of day" to make it easy for the AI
    df['minutes_of_day'] = df['timestamp'].dt.hour * 60 + df['timestamp'].dt.minute
    
    X = df[['minutes_of_day']] # Input
    y = df['temperature']      # Output (Target)

    # 3. Train the Model (Random Forest)
    print(f"[AI] Training model on {len(df)} data points...")
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X, y)
    print("[AI] Training complete.")

    # 4. Predict the Future (Next 60 Minutes)
    last_time = df['timestamp'].iloc[-1]
    future_times = []
    future_minutes = []

    for i in range(1, 61, 5): # Predict every 5 minutes for the next hour
        next_time = last_time + timedelta(minutes=i)
        future_times.append(next_time)
        # Convert to minutes of day
        m_of_d = next_time.hour * 60 + next_time.minute
        future_minutes.append([m_of_d])

    # Ask the AI to guess
    predictions = model.predict(future_minutes)

    # 5. Visualize the Result
    plt.figure(figsize=(10, 6))
    
    # Plot Real History (Last 50 points only, to keep it readable)
    plt.plot(df['timestamp'].tail(50), df['temperature'].tail(50), label='Actual Data', color='blue', marker='o')
    
    # Plot AI Prediction
    plt.plot(future_times, predictions, label='AI Prediction (Next 1h)', color='red', linestyle='--', marker='x')

    plt.title("AI Temperature Forecast")
    plt.xlabel("Time")
    plt.ylabel("Temperature (C)")
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Save the graph to a file so you can see it
    filename = "ai_prediction_graph.png"
    plt.savefig(filename)
    print(f"[SUCCESS] Prediction Graph saved as '{filename}'")
    plt.show() # Opens the window on your screen

# --- RUN IT ---
if __name__ == "__main__":
    train_and_predict()