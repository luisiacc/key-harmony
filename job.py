import os
import threading

import keyboard
from playsound import playsound


def play_sound():
    # Replace 'sound_file.wav' with the path to the sound file you want to play
    sound_file = "sound_file.wav"
    playsound(sound_file)


def on_key_event(event):
    # Play the sound in a separate thread to avoid blocking the main thread
    threading.Thread(target=play_sound, daemon=True).start()


def main():
    # Attach the key event handler to all keyboard events
    keyboard.on_press(on_key_event)

    # Keep the script running
    keyboard.wait()


if __name__ == "__main__":
    main()
