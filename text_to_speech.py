import pyttsx3

# Initializing the text-to-speech engine
engine = pyttsx3.init()

# Function to speak a given text
def speak_text(text):
    # Seeting the properties (optional)
    engine.setProperty('rate', 150) # Speed of speech
    engine.setProperty('volume', 0.9)
    
    # Speak the text
    engine.say(text)
    engine.runAndWait()
    
    
if __name__ == "__main__":
    text = "Hello, I am your AI assistant. How can I help you today?"
    print(f"Speaking: {text}")
    speak_text(text)