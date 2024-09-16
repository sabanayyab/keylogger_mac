# macOS Keylogger with `pynput`

A simple Python keylogger for macOS using the `pynput` library. This script logs all keypresses and saves them into a text file.

## Features

- Logs alphanumeric keys.
- Logs special keys (e.g., Shift, Ctrl, Esc) with a readable format.
- Saves all keypresses in a log file named `mac_keylog.txt`.
- Stops logging when the "Esc" key is pressed.

## Requirements

To run this script, you'll need Python and the `pynput` library. You can install `pynput` using pip:

```bash
pip install pynput

