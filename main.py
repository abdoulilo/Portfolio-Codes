import commands_music as music
import commands_reminder as reminder

COMMANDS = {
    "play music": music.handle_music_command,
    "set reminder": reminder.handle_reminder_command,
}

def main():
    from tts import speak
    from recognizer import recognize_speech
    
    speak("Hello! I am your assistant. How can I help you?")
    while True:
        try:
            command = recognize_speech()
            if command:
                found = False
                for key, handler in COMMANDS.items():
                    if key in command:
                        handler(command)
                        found = True
                        break
                if not found:
                    speak("Sorry, I did not understand that command.")
        except KeyboardInterrupt:
            speak("Goodbye!")
            break

if __name__ == "__main__":
    main()
