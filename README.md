# Velocity_pi_python_diagnosisScreen
Velocity Aircraft Pi powered diagnosis screen

## RaspberryPi Powered Diagnosis Screen
Built for the Velocity Aircraft, the Pi Diagnosis Screen reads data from the CAN bus of the aircraft and presents this information to the (touch) screen.

Information available includes: 
- Engine ECU Data
- Outside Air Temp (C)
- Cabin Air Temp (C)
- Lights
- Landing Gear position
- Pilot Door Lock
- CoPilot Door Lock
- System Alerts and Notices

## Architecture
This app is part of a wider project / suit of apps that are used by a single Pi to read and process data around the Velocity Aircraft.
Example software configuration:

1. CanBus Hi/Low Wires
2. RaspberryPi CanBus Reader
3. [PM2](https://pm2.keymetrics.io) Controlled script that reads CanBus data and passes via [SocketIO](https://socket.io).
4. NodeJS/SocketIO Server that hosts HTML and SocketIO config
5. [PM2](https://pm2.keymetrics.io) Python/Tkinter GUI that recieves data and presents it to the RPi Screen (This App)

