import os
import threading
from pathlib import Path

from playsound import playsound
from pynput import keyboard


def play_sound():
    # Replace 'sound_file.wav' with the path to the sound file you want to play
    sound_file = Path("./sounds/cherry-mx-brown-short.wav")
    playsound(sound_file.absolute())


pressed_keys = set()


def on_key_press(key):
    if key not in pressed_keys:
        pressed_keys.add(key)
        # Play the sound in a separate thread to avoid blocking the main thread
        threading.Thread(target=play_sound, daemon=True).start()


def on_key_release(key):
    pressed_keys.discard(key)


def main():
    # Attach the key event handlers to keyboard events
    with keyboard.Listener(on_press=on_key_press, on_release=on_key_release) as listener:
        listener.join()


if __name__ == "__main__":
    main()
