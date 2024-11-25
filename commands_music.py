import os
import random
from tts import speak

MUSIC_FOLDER_PATH = "./music"  # Adjust to your folder with music files

def handle_music_command(command):
    speak("Playing music.")
    play_random_music()

def play_random_music():
    try:
        files = [f for f in os.listdir(MUSIC_FOLDER_PATH) if f.endswith(('.mp3', '.wav'))]
        if files:
            random_song = random.choice(files)
            print(f"Playing: {random_song}")
            os.system(f"start {os.path.join(MUSIC_FOLDER_PATH, random_song)}")
        else:
            speak("No music files found in the folder.")
    except Exception as e:
        print(f"Error playing music: {e}")
        speak("There was an error playing the music.")
