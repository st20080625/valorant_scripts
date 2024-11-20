import numpy as np
import keyboard
import cv2
import time
import mss

target_color_rgb = (128, 0, 128)

def rgb_to_hsv(color):
    rgb = np.uint8([[color]])
    hsv = cv2.cvtColor(rgb, cv2.COLOR_RGB2HSV)
    return hsv[0][0]
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
while True:
    while keyboard.is_pressed('left ctrl'):
        with mss.mss() as sct:
            screenshot = sct.grab(monitor_target)
            rgb_array = np.array(screenshot)
        if rgb_array.shape[-1] == 4:
            rgb_array = rgb_array[:, :, :3]

        hsv_array = cv2.cvtColor(rgb_array, cv2.COLOR_RGB2HSV)

        mask = cv2.inRange(hsv_array, lower_bound, upper_bound)
        if np.any(mask):
            time.sleep(0.05)
            keyboard.press('k')
            time.sleep(0.2)
            keyboard.release('k')
        if keyboard.is_pressed('p'):
            exit()