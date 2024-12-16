import time
import psutil
from pynput.keyboard import Controller, Key
import pygetwindow as gw

keyboard = Controller()

# Check if Rocket League is running
def is_rocket_league_running():
    for process in psutil.process_iter(['name']):
        try:
            if 'RocketLeague' in process.info['name']:
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False

# Check if Rocket League is the active window
def is_window_in_focus(window_title="Rocket League"):
    active_window = gw.getActiveWindow()
    if active_window and window_title.lower() in active_window.title.lower():
        return True
    return False

def start_keyboard_bot():
    print("""
        +---------------------------------------------+
        |                                             |
        |   Rocket League drop opener                 |
        |                                             |
        |   Please navigate to:                       |
        |     Main Menu > Garage > Manage Inventory > |
        |     Reward Items                            |
        |                                             |
        |   WARNING: This bot will auto equip items   |
        |                                             |
        +---------------------------------------------+
                """)
    input("Once you are there, press Enter to continue...")
    while True:
        # Check if Rocket League is running
        if not is_rocket_league_running():
            print("Rocket League is not running. Waiting...")
            time.sleep(5)  # Wait for 5 seconds before checking again
            continue

        # Countdown before starting the bot
        print("Starting bot in:")
        for i in range(5, 0, -1):
            print(f"{i}...")
            time.sleep(1)

        # Emulate keyboard inputs
        while True:
            if not is_window_in_focus():
                print("Rocket League is not the active window. Please focus on the game.")
                print("Or close the program if you are done with drops :)")
                time.sleep(5)  # Wait for 5 seconds before checking again
            else:
                time.sleep(0.1)
                keyboard.tap(Key.left)
                print("Pressing left")
                time.sleep(0.1)
                keyboard.tap(Key.left)
                print("Pressing left")
                time.sleep(0.1)
                keyboard.tap(Key.enter)
                print("Pressing enter")
                time.sleep(0.1)
                keyboard.tap(Key.left)
                print("Pressing left")
                time.sleep(0.1)
                keyboard.tap(Key.enter)
                print("Pressing enter")
                time.sleep(0.1)
                keyboard.tap(Key.esc)
                print("Pressing escape")
                time.sleep(0.1)
                keyboard.tap(Key.enter)
                print("Pressing enter")

if __name__ == '__main__':
    start_keyboard_bot()
