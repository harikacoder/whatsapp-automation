import pyautogui
import time

def get_mouse_position():
    print("Move your mouse to the desired position within 5 seconds.")
    time.sleep(5)
    position = pyautogui.position()
    print(f"Mouse position: {position}")
    return position

if __name__ == "__main__":
    get_mouse_position()
