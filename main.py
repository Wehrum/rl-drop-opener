import time
import psutil
from pynput.keyboard import Controller, Key, Listener
import pygetwindow as gw
import threading

keyboard = Controller()

# Function to check if Rocket League is running
def is_rocket_league_running():
    for process in psutil.process_iter(['name']):
        try:
            if 'RocketLeague' in process.info['name']:
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False

# Function to check if Rocket League is the active window
def is_window_in_focus(window_title="Rocket League"):
    active_window = gw.getActiveWindow()
    if active_window and window_title.lower() in active_window.title.lower():
        return True
    return False

def start_keyboard_bot():
    print("""
        +---------------------------------------------+
        |                                             |
        |   \x1B[32mRocket League drop opener\x1B[0m                 |
        |                                             |
        |   Please navigate to:                       |
        |     Main Menu > Garage > Manage Inventory > |
        |     Reward Items                            |
        |                                             |
        |   \x1B[31mWARNING: This bot will auto equip items\x1B[0m   |
        |                                             |
        +---------------------------------------------+
                """)
    input("\x1B[33mOnce you are there, press Enter to continue...\x1B[0m")
    while True:
        # Check if Rocket League is running
        if not is_rocket_league_running():
            print("Rocket League is not running. Waiting...")
            time.sleep(5)  # Wait for 5 seconds before checking again
            continue

        # Check if Rocket League is in focus
        if not is_window_in_focus():
            print("Rocket League is not the active window. Please focus on the game.")
            time.sleep(5)  # Wait for 5 seconds before checking again
            continue

        # Notify user to navigate to the correct menu

        # Countdown before starting the bot
        print("Starting bot in:")
        for i in range(5, 0, -1):
            print(f"{i}...")
            time.sleep(1)

        # Emulate keyboard inputs
        while True:
            time.sleep(0.1)
            keyboard.press('a')  # Press the 'A' key
            print("Pressing A")
            time.sleep(0.1)
            keyboard.release('a')
            time.sleep(0.1)

            keyboard.press(Key.left)  # Press the left arrow key
            print("Pressing Left")
            time.sleep(0.1)
            keyboard.release(Key.left)
            time.sleep(0.1)

            keyboard.press('a')  # Press the 'A' key again
            print("Pressing A")
            time.sleep(0.1)
            keyboard.release('a')
            time.sleep(0.1)

            keyboard.press(Key.esc)  # Press the 'ESC' key
            print("Pressing ESC")
            time.sleep(0.1)
            keyboard.release(Key.esc)
            time.sleep(0.1)

if __name__ == '__main__':
    start_keyboard_bot()
