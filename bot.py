import numpy as np
import keyboard
import cv2
import time
import mss
import random
import threading
from queue import Queue
import win32api
import win32con

def screenshot(monitor_target, lower_bound, upper_bound, queue):
    with mss.mss() as sct:
        while True:
            if keyboard.is_pressed('left ctrl'):
                screenshot = sct.grab(monitor_target)
                rgb_array = np.array(screenshot)
                if rgb_array.shape[-1] == 4:
                    rgb_array = rgb_array[:, :, :3]
                hsv_array = cv2.cvtColor(rgb_array, cv2.COLOR_RGB2HSV)
                mask = cv2.inRange(hsv_array, lower_bound, upper_bound)
                queue.put(mask)

def shot(queue):
    while True:
        if keyboard.is_pressed('left ctrl'):
            if not queue.empty():
                mask = queue.get()
                if np.any(mask):
                    keyboard.press_and_release('k')
                    #win32api.keybd_event(win32con.MOUSEEVENTF_LEFTDOWN, 0,0,0)
                    #win32api.keybd_event(win32con.MOUSEEVENTF_LEFTUP, 0,0,0)

def rgb_to_hsv(color):
    rgb = np.uint8([[color]])
    hsv = cv2.cvtColor(rgb, cv2.COLOR_RGB2HSV)
    return hsv[0][0]

# 設定
target_color_rgb = (128, 0, 128)
target_color_hsv = rgb_to_hsv(target_color_rgb)
monitor_target = {
    'top': 535,
    'left': 955,
    'width': 10,
    'height': 10
}
hue_range = 10
lower_bound = np.array([max(target_color_hsv[0] - hue_range, 0), 50, 50])
upper_bound = np.array([min(target_color_hsv[0] + hue_range, 179), 255, 255])

queue = Queue()

screenshot_thread = threading.Thread(target=screenshot, daemon=True, args=(monitor_target, lower_bound, upper_bound, queue))
shot_thread = threading.Thread(target=shot, daemon=True, args=(queue,))

screenshot_thread.start()
shot_thread.start()

while True:
    if keyboard.is_pressed('p'):
        break
