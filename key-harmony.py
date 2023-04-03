import argparse
import os
import platform
import sys
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


def kill_active_instances():
    current_pid = os.getpid()
    script_name = os.path.basename(sys.argv[0])

    if platform.system() == "Windows":
        for line in os.popen(
            "wmic process where \"name='python.exe' or name='pythonw.exe'\" get processid, commandline"
        ):
            if script_name in line and str(current_pid) not in line:
                pid = int(line.split()[-1])
                os.system(f"taskkill /F /PID {pid}")
    else:  # Linux
        os.system("killall $(ps aux | grep '%s' | awk '{print $2}')" % script_name)


def main():
    parser = argparse.ArgumentParser(description="Play a sound on every keystroke.")
    parser.add_argument("-k", "--kill", action="store_true", help="kill active instances of the script")
    args = parser.parse_args()

    if args.kill:
        kill_active_instances()
        sys.exit(0)

    # Attach the key event handlers to keyboard events
    with keyboard.Listener(on_press=on_key_press, on_release=on_key_release) as listener:
        listener.join()


if __name__ == "__main__":
    main()
