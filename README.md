# Gesture-Based Alert System for Bedridden Patients 🤖🖐️📱

A real-time gesture recognition system designed to assist **bedridden patients, elderly individuals, and people with physical disabilities** by enabling them to communicate non-verbally through **hand gestures**. This system interprets hand signs and sends alerts to caregivers via a **mobile app**, significantly improving the quality of care and response time.

---

## 🧠 Project Overview

Many patients with limited mobility or speech struggle to convey their needs. This project uses **image processing**, **machine learning**, and **IoT** to detect hand gestures and transmit alerts using the **MQTT protocol** and a **Flutter-based mobile application**.

---

## 🔧 Features

- ✋ Real-time **hand gesture recognition** using MediaPipe & TensorFlow
- 📡 Communication through **MQTT protocol**
- 🛰️ IoT integration with **ESP8266 NodeMCU** and **Relay Module**
- 📲 **Cross-platform mobile app** using Flutter
- 🚨 Alerts caregivers for:
  - Emergency (Panic)
  - Request Water
  - Nature Call
  - Device Control (Fan/Light ON/OFF)
- 🔔 Instant **local notifications** on caregiver’s phone
- 🌐 **Cloud integrated** for remote monitoring

---

## 🧰 Tech Stack

| Component              | Technology Used                     |
|------------------------|-------------------------------------|
| Gesture Recognition    | Python, OpenCV, MediaPipe, TensorFlow |
| IoT Communication      | MQTT (HiveMQ), ESP8266 NodeMCU     |
| Mobile Application     | Flutter, Dart, MQTT Client, Local Notifications |
| Backend                | MQTT Broker (HiveMQ)                |

---

## 📲 How It Works

1. **Camera** captures hand gesture.
2. **Python script** detects and classifies gesture using TensorFlow.
3. **MQTT message** is published with gesture data.
4. **IoT device** acts based on gesture (like turning on a light).
5. **Flutter App** subscribed to MQTT receives alert & shows notification.

---

## 💡 Gestures Mapped

| Gesture | Meaning         | Action Triggered                |
|---------|------------------|--------------------------------|
| A       | Panic            | Sends emergency alert          |
| B       | Need Water       | Notifies caregiver             |
| C       | Nature Call      | Sends restroom request         |
| D       | All fingers down | Turn on appliance (e.g. light) |
| E       | Custom gesture   | Turn off appliance             |

---

## 🖼️ System Architecture

```text
[Camera] → [Python + MediaPipe] → [TensorFlow] 
          → [MQTT Publish] → [HiveMQ Broker]
              → [Flutter App Notification]
              → [NodeMCU IoT Device Control]


## 📦 Installation

```bash
# 1. Python Backend (Gesture Detection)
pip install opencv-python mediapipe tensorflow paho-mqtt
python gesture_mqtt_sender.py

# 2. IoT Hardware Setup
# - Flash ESP8266 NodeMCU with Arduino code
# - Connect relay module to control appliances
# - Subscribe to topic "handgesture1"

# 3. Flutter App
flutter pub get
flutter run
```

---

## 🧪 Testing

```text
Gesture | Action           | Result
--------|------------------|---------
A       | Emergency        | Passed ✅
B       | Give Water       | Passed ✅
C       | Nature Call      | Passed ✅
D       | Turn ON Device   | Passed ✅
E       | Turn OFF Device  | Passed ✅
```

---

## 📈 Future Enhancements

```diff
- Extend gesture vocabulary
- Personalize gesture mapping per patient
- Add voice fallback
- Support wearable-based gesture recognition
- Advanced ML models for high accuracy
```

---

## 👨‍💻 Authors

```csharp
Shridhar K Dhavaleshwar (4SU22AD402)
Mahantesh Sankanagoudra
Nitish Terdal
Shashank Sasalatti
Guided by: Mr. Padma Prasada, Assistant Professor, SDMIT
```

---

## 📜 License

```vbnet
This project is part of academic submission to Visvesvaraya Technological University (VTU) and may be reused for educational and research purposes.
```
