# CapteurTempHumRTOS

A real-time temperature and humidity monitoring system built around an Arduino sensor node running on an RTOS (Real-Time Operating System), with a backend, a web dashboard, and an AI component for data analysis. This project appears to be a PFE (*Projet de Fin d'Études* / final-year engineering project).

> **Note:** This README was generated from the repository's folder structure. Please review and adjust the sections below (hardware, tech stack, setup steps) to match the actual implementation details of each sub-project.

## Project Structure

```
CapteurTempHumRTOS/
├── AI/                 # AI / data analysis component
├── PFE_Backend/         # Backend server (API, data handling)
├── code2/codeArduino2/  # Second Arduino firmware variant
├── codeArduino/         # Arduino firmware (sensor + RTOS tasks)
├── codePfeMatrix/       # Matrix / display related code
├── dashboard/           # Web dashboard for visualizing sensor data
├── pfe_data.db          # Project database (SQLite)
└── README.md
```

## Overview

The system reads temperature and humidity data from a sensor connected to an Arduino board. The firmware uses an RTOS to manage concurrent tasks (e.g., sensor sampling, data transmission, display updates) in real time. Collected data is sent to a backend service, stored in a database, and visualized through a web dashboard. An AI module is included for further data processing or predictive analysis.

## Features

- Real-time sensor sampling (temperature & humidity) using RTOS task scheduling on Arduino
- Backend API for receiving, storing, and serving sensor data
- Web dashboard for live/historical data visualization
- AI component for data analysis or predictions
- Local data persistence via SQLite (`pfe_data.db`)

## Tech Stack

- **Firmware:** Arduino (C/C++) with an RTOS (e.g., FreeRTOS)
- **Backend:** `PFE_Backend` (server/API — update with actual framework, e.g. Python/Flask, Node.js, etc.)
- **Dashboard:** `dashboard` (web frontend — update with actual framework)
- **AI:** `AI` folder (update with model/library used)
- **Database:** SQLite (`pfe_data.db`)

## Hardware Requirements

- Arduino board (e.g., Uno, Mega, ESP32 — update with the actual board used)
- Temperature & humidity sensor (e.g., DHT11/DHT22 — update with the actual sensor used)
- USB cable / power supply
- (Optional) Display module, if used by `codePfeMatrix`

## Getting Started

### 1. Firmware (Arduino)

1. Open the `codeArduino` (or `code2/codeArduino2`) project in the Arduino IDE or PlatformIO.
2. Install any required libraries (RTOS library, sensor library, etc.).
3. Select your board and port, then upload the sketch.

### 2. Backend

```bash
cd PFE_Backend
# install dependencies (update command based on the actual stack)
# e.g. pip install -r requirements.txt   OR   npm install

# run the server
# e.g. python app.py   OR   npm start
```

### 3. Dashboard

```bash
cd dashboard
# install dependencies
# npm install

# start the dashboard
# npm start
```

### 4. AI Module

```bash
cd AI
# install dependencies and run according to the module's own instructions
```

## Database

Sensor readings and related data are stored in `pfe_data.db` (SQLite). You can inspect it using any SQLite client:

```bash
sqlite3 pfe_data.db
```

## Author

- [haythemm123](https://github.com/haythemm123)

## License

No license specified yet. Consider adding one (e.g., MIT) if you intend to share or open-source this project.
