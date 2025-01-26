import speech_recognition as sr
import pyttsx3
import numpy as np
import sounddevice as sd
from noisereduce import reduce_noise
import time
import board
import busio
from adafruit_ssd1306 import SSD1306_I2C

# Initialize speech recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Initialize OLED display
i2c = busio.I2C(board.SCL, board.SDA)
disp = SSD1306_I2C(128, 32, i2c)
disp.fill(0)
disp.show()

# Function to reduce noise in audio
def noise_reduction(audio_data, sample_rate):
    print("Reducing background noise...")
    audio_array = np.frombuffer(audio_data.frame_data, dtype=np.int16)
    reduced_noise = reduce_noise(y=audio_array, sr=sample_rate)
    return reduced_noise

# Function for text-to-speech feedback
def speak_text(text):
    engine.say(text)
    engine.runAndWait()

# Function to display text on OLED
def display_text(text):
    disp.fill(0)  # Clear the display
    text_width, text_height = disp.text_width(text), disp.text_height(text)
    x = (disp.width - text_width) // 2
    y = (disp.height - text_height) // 2
    disp.text(text, x, y, 1)
    disp.show()

# Main function for voice detection
def advanced_voice_detection():
    print("Initializing advanced voice detection...")
    
    while True:
        try:
            print("\nCalibrating microphone for ambient noise...")
            with sr.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=2.0)
                print("Listening for your voice...")
                
                # Capture audio input
                audio = recognizer.listen(mic)
                print("Processing audio...")
                
                # Noise reduction
                reduced_audio = noise_reduction(audio, sample_rate=audio.sample_rate)
                
                # Recognize speech
                text = recognizer.recognize_google(audio)
                text = text.lower()
                
                print(f"Recognized: {text}")
                speak_text(f"You said: {text}")
                
                # Display text on OLED
                display_text(text) 
                time.sleep(2)  # Display text for 2 seconds

                # Exit condition (optional)
                if "exit" in text or "quit" in text:
                    print("Exiting voice detection. Goodbye!")
                    speak_text("Goodbye!")
                    break
        
        except sr.UnknownValueError:
            print("Sorry, I could not understand that. Please try again.")
            speak_text("I didn't catch that, could you please repeat?")
        
        except sr.RequestError as e:
            print(f"Google Speech Recognition service error: {e}")
            speak_text("There seems to be an issue with the speech recognition service.")
            break
        
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            speak_text("An unexpected error occurred. Please check the console for details.")
            break

# Run the advanced voice detection
if _name_ == "_main_":
    advanced_voice_detection()