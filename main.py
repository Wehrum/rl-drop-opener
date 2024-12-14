import time
import psutil
from pynput.keyboard import Controller, Key
import pygetwindow as gw

keyboard = Controller()

def is_rocket_league_running():
    """ Function checks that the Rocket League process
    is on. If it's not on, notify the user and wait 5 seconds.

    Returns:
        bool: True if Rocket League process is detected, false if not.
    """
    for process in psutil.process_iter(['name']):
        try:
            if 'RocketLeague' in process.info['name']:
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False

def is_window_in_focus(window_title="Rocket League"):
    active_window = gw.getActiveWindow()
    if active_window and window_title.lower() in active_window.title.lower():
        return True
    return False

if __name__ == '__main__':
    print("Welcome to the RL Drop Opener bot, before continuing please setup the game as instructed.")
    print("Go to: Main Menu > Garage > Manage Inventory > Reward Items.")
    input("Once you are there, press Enter to continue...")
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

        # Countdown before starting the bot
        print("Starting bot in:")
        for i in range(5, 0, -1):
            print(f"{i}...")
            time.sleep(1)

        while True:
            time.sleep(0.1)
            keyboard.tap(Key.left)  # Press the left arrow key
            print("Pressing left")
            time.sleep(0.1)
            keyboard.tap(Key.left)  # Press the left arrow key
            print("Pressing left")
            time.sleep(0.1)
            keyboard.tap(Key.enter)
            print("Pressing enter")
            time.sleep(0.1)
            keyboard.tap(Key.left)  # Press the left arrow key
            print("Pressing left")
            time.sleep(0.1)
            keyboard.tap(Key.enter)  # Press the 'A' key again
            print("Pressing enter")
            time.sleep(0.1)
            keyboard.tap(Key.esc)  # Press the 'B' key
            print("pressing escape")
            time.sleep(0.1)
            keyboard.tap(Key.enter)
            print("Pressing enter")
