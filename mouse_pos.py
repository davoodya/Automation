from pynput.mouse import Controller
import time

mouse = Controller()

while True:
    x, y = mouse.position
    print(f"X: {x}, Y: {y}", end="\r")  # "\r" برای نمایش موقعیت به‌صورت به‌روز شده در همان خط
    time.sleep(0.1)  # برای جلوگیری از مصرف بیش از حد منابع سیستم