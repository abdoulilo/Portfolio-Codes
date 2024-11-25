from tts import speak

REMINDERS_FILE = "reminders.txt"

def handle_reminder_command(command):
    speak("What reminder should I set?")
    reminder = input("Enter reminder: ")  # Replace with speech recognition if needed
    save_reminder(reminder)
    speak(f"Reminder '{reminder}' has been set.")

def save_reminder(reminder):
    try:
        with open(REMINDERS_FILE, 'a') as file:
            file.write(reminder + "\n")
        print(f"Reminder saved: {reminder}")
    except Exception as e:
        print(f"Error saving reminder: {e}")
        speak("There was an error saving the reminder.")
