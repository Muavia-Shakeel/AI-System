import speech_recognition as sr
import pyttsx3
from datetime import datetime

# Initialize recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to speak a given text
def speak_text(text):
    engine.say(text)
    engine.runAndWait()

# Function to process recognized text
def process_command(command):
    command = command.lower()

    if "time" in command:
        current_time = datetime.now().strftime("%H:%M:%S")
        response = f"The current time is {current_time}."
        print(response)
        speak_text(response)

    elif "quit" in command:
        response = "Goodbye! Have a great day."
        print(response)
        speak_text(response)
        exit()

    else:
        response = "Sorry, I don't understand that command."
        print(response)
        speak_text(response)

# Main program loop
with sr.Microphone() as source:
    print("Listening for commands...")
    speak_text("I am ready to assist you. Please speak a command.")

    while True:
        try:
            recognizer.adjust_for_ambient_noise(source, duration=1)
            audio = recognizer.listen(source)
            print("Recognizing...")

            # Convert speech to text
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")

            # Process the recognized command
            process_command(text)

        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
            speak_text("Sorry, I could not understand that. Please try again.")

        except sr.RequestError as e:
            print(f"Request error from Google Speech Recognition: {e}")
            speak_text("There was a request error. Please try again.")
