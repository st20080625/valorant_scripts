import numpy as np
import cv2
import time
from mss import mss as mss_module
from random import uniform
import sys
import win32api
import win32con
def rgb_to_hsv(color):
    rgb = np.uint8([[color]])
    hsv = cv2.cvtColor(rgb, cv2.COLOR_RGB2HSV)
    return hsv[0][0]
#purple
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

sct = mss_module()
# keycode(16) 0xA2 = left ctrl
# keycode(16) 0x50 = p
# keycode(16) 0x4B = k
while True:
    if win32api.GetAsyncKeyState(0xA2) < 0:
        screenshot = sct.grab(monitor_target)
        rgb_array = np.array(screenshot)
        if rgb_array.shape[-1] == 4:
            rgb_array = rgb_array[:, :, :3]

        hsv_array = cv2.cvtColor(rgb_array, cv2.COLOR_RGB2HSV)
        mask = cv2.inRange(hsv_array, lower_bound, upper_bound)
        if np.any(mask):
            sleep_time = uniform(0.18, 0.24)
            win32api.keybd_event(0x4B, 0, 0, 0)
            #win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0)
            time.sleep(sleep_time)
            win32api.keybd_event(0x4B, 0, win32con.KEYEVENTF_KEYUP, 0)
            #win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0)
            time.sleep(0.01)
    if win32api.GetAsyncKeyState(0x50) < 0:
        sys.exit()
