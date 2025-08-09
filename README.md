# IEEE Robotics: Multimodal Human Interaction System

## System Overview
A modular robotics platform integrating:
1. **Robotics Vision Module**  
   - Real-time human presence detection using ultrasonic sensor arrays  
   - Servo-actuated directional response (pan-tilt mechanism)  
   - OpenCV-based object recognition pipeline  

2. **AI Assistant Module**  
   - Voice-activated Gemini API integration  
   - Context-aware dialogue management  
   - Sensor-triggered conversation initiation  

## Core Technical Specifications
🛠️ **Hardware Specifications**

*Component	Specification*

Microcontroller:	Arduino Uno R3

Sensors:	2x HC-SR04 Ultrasonic (20-400cm)

Actuators:	SG90 Servo (180° range)

Processing:	ESP32Cam (Optional)

Power:	5V 2A DC

<img width="1262" height="500" alt="deepseek_mermaid_20250809_afb6d3" src="https://github.com/user-attachments/assets/cae07a88-600c-45a8-8c2a-9173582b3567" />

### Robotics Vision Module
```c
// Key Arduino Functions
void trackHuman() {
  // Ultrasonic sensor polling (20-400cm range)
  // Servo control with dampened movement (PID control)
}
