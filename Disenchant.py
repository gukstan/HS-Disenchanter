import subprocess
import sys
import importlib.util

def install_and_import(package):
    if importlib.util.find_spec(package) is None:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# List of required packages
required_packages = ["pyautogui", "keyboard", "pygetwindow"]

# Install missing packages
for package in required_packages:
    install_and_import(package)

import pyautogui
import keyboard
import time
import pygetwindow as gw

# Bring the "Hearthstone" window to the front
window = gw.getWindowsWithTitle('Hearthstone')
if window:
    window[0].activate()
else:
    print("Hearthstone window not found.")
    exit()

time.sleep(3)  # Wait for the window to be activated

# Flag to indicate if the 'Insert' key has been pressed
stop_script = False

# Function to set the flag when 'Insert' key is pressed
def on_insert_key():
    global stop_script
    stop_script = True

# Register the 'Insert' key hotkey
keyboard.add_hotkey('insert', on_insert_key)


screenWidth, screenHeight = pyautogui.size()  # Get the size of the primary monitor
# Define the list of points (x, y coordinates)

if pyautogui.size() == (1920, 1080): # 1080p
    card = (400, 355)
    disenchant = (800, 915)
    confirm = (841, 673)
    nowhere = (118, 364)
else:
    print("Screen resolution not supported yet.")
    exit()

try:
    while not stop_script:
        pyautogui.click(card)
        time.sleep(1)  # check if the script has been interrupted
        if stop_script:
            break
        pyautogui.click(disenchant)
        time.sleep(1)
        if stop_script:
            break
        pyautogui.click(confirm)
        time.sleep(1)
        if stop_script:
            break
        pyautogui.click(nowhere)
        time.sleep(1)
        if stop_script:
            break
    print("Insert key pressed. Exiting...")
except KeyboardInterrupt:
    print("Program interrupted.")