kill $(ps aux | grep 'sound-on-keystroke' | awk '{print $2}')
