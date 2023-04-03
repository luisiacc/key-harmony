## key-harmony

Play a sound every time you press a key, some people like it.

Right now it plays a default sound hardcoded but later will be selectable. The default sound is the mechanical cherry mx brown key stroke.

### Install dependencies

```bash
pip install -r requirements.txt
```

### How to run

On Linux/MacOS

```bash
nohup python key_sound.py &
```

On Windows

```cmd
pythonw key-harmony.py
```


### How to kill the process

Run the script with the `-k` flag like:

```bash
python key-harmony.py -k
```

This works for both Linux and Windows.

If you are on Linux you can also execute the `./kill.sh` file, remember to assign it execution permissions with `chmod`.

### TODO's

- [ ] Add more sounds, all mechanical cherry sounds
- [ ] Add `-file` arg to use a custom sound
- [ ] Add `-option` arg to select one of the default sounds
- [ ] User interface?

### Wanna contribute?

If you want to add some functionality or add an extra keystroke sound, feel free to open a PR.
