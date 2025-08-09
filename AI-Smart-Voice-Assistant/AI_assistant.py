import serial
import speech_recognition as sr
from google.generativeai import GenerativeModel
import google.generativeai as genai
import time
from gtts import gTTS
import os

genai.configure(api_key='YOUR_API_KEY')  
model = GenerativeModel('gemini-pro')

arduino = serial.Serial('COM3', 9600, timeout=1)  
time.sleep(2)  

def listen():
    """Listen to user's voice input and convert to text"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        
    try:
        text = r.recognize_google(audio)
        print(f"You said: {text}")
        return text
    except:
        print("Sorry, I didn't catch that")
        return ""

def speak(text):
    """Convert text to speech and play it"""
    print(f"AI: {text}")
    tts = gTTS(text=text, lang='en')
    tts.save("response.mp3")
    os.system("start response.mp3")  

def get_ai_response(prompt):
    """Get response from Gemini AI"""
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"Error with AI: {e}")
        return "I'm having trouble thinking right now. Can you repeat that?"

def check_person_detected():
    """Check if Arduino detects a person"""
    arduino.write(b'check\n')  
    time.sleep(0.1)
    if arduino.in_waiting:
        data = arduino.readline().decode('utf-8').strip()
        return data == "person_detected"
    return False

def main():
    speak("Hello! I'm your robot assistant. I'll activate when I detect someone nearby.")
    while True:
        if check_person_detected():
            speak("I see you there! How can I help you today?")
            while check_person_detected():  
                user_input = listen()
                if user_input.lower() in ["exit", "quit", "goodbye"]:
                    speak("Goodbye! Have a nice day!")
                    return
                if user_input:
                    if any(word in user_input.lower() for word in ["who are you", "your name"]):
                        response = "Hi! I'm Amy, a friendly robot assistant. How can I assist you?"
                    elif any(word in user_input.lower() for word in ["how are you", "how you doing"]):
                        response = "I'm functioning within normal parameters, thanks for asking!"
                    else:
                        prompt = f"Have a friendly, slightly informal conversation. Keep responses under concise and friendly. User said: {user_input}"
                        response = get_ai_response(prompt)
                    speak(response)
                else:
                    speak("I didn't hear anything. Are you still there?")
            speak("I don't see anyone. I'll go back to sleep now.")
        time.sleep(1)  
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        speak("Shutting down...")
        arduino.close()