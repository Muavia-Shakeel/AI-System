import speech_recognition as sr

# Initializing recognizer
recognizer = sr.Recognizer()

# # List microphone devices
# print("Available microphones:")
# print(sr.Microphone.list_microphone_names())

try:
    # Selecting a specific microphone if necessary
    mic = sr.Microphone(device_index=1)  # Replace 0 with your microphone index

    with mic as source:
        # Adjust for ambient noise
        print("Adjusting for ambient noise...")
        recognizer.energy_threshold = 100  # Fine-tune threshold as needed
        recognizer.adjust_for_ambient_noise(source, duration=2)

        # Start listening
        print("Listening... Say 'End the Program' to end.")
        while True:
            audio = recognizer.listen(source, timeout=15, phrase_time_limit=10)

            # Save audio for debugging
            with open("audio_debug.wav", "wb") as f:
                f.write(audio.get_wav_data())

            # Convert speech to text
            print("Recognizing...")
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")  # Debugging output
            if text.lower() == "End the program":
                print("Exiting...")
                break

except sr.UnknownValueError:
    print("Sorry, I could not understand the audio.")
except sr.RequestError as e:
    print(f"Request error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
