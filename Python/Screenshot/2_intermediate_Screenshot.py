from PIL import Image
import pyautogui as pag
import time
import keyboard

time.sleep(3)

filepath = 'C:\\Users\\visio\\OneDrive\\Desktop\\Python\\Screenshot\\images'

def screenshot():
    curr_time = time.strftime("_%Y%m%d_%H%M%S")
    pag.screenshot(f"{filepath}/image{curr_time}.png")

while True:
    if keyboard.is_pressed("ctrl"):
        screenshot()
    elif keyboard.is_pressed("esc"):
        break