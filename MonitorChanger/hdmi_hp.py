import subprocess
import pyautogui
import time

def run_hp_display_center():
    try:
        # مسیر فایل اجرایی HPDisplayCenter
        app_path = r"C:\Program Files\WindowsApps\AD2F1837.HPDisplayCenter_2.2.8.0_x64__v10z8vjag6ke6\HPDisplayCenter.exe"

        # اجرای برنامه
        subprocess.Popen(app_path)
        print("برنامه HPDisplayCenter با موفقیت اجرا شد.")

        # صبر کردن تا برنامه باز شود
        time.sleep(5)

        # انجام کلیک‌های مورد نظر
        # کلیک اول در موقعیت X:595 و Y:251
        pyautogui.moveTo(595, 251, duration=1)
        pyautogui.click()
        print("کلیک اول انجام شد.")

        # کلیک دوم در موقعیت X:436 و Y:333
        pyautogui.moveTo(436, 333, duration=1)
        pyautogui.click()
        print("کلیک دوم انجام شد.")

        # صبر کردن به مدت 3 ثانیه
        time.sleep(3)

        # کلیک سوم در موقعیت X:801 و Y:251
        pyautogui.moveTo(801, 251, duration=1)
        pyautogui.click()
        print("کلیک سوم انجام شد.")

        # کلیک چهارم در موقعیت X:612 و Y:378
        pyautogui.moveTo(612, 378, duration=1)
        pyautogui.click()
        print("کلیک چهارم انجام شد.")

        print("تمام عملیات با موفقیت انجام شد.")

    except Exception as e:
        print(f"خطا رخ داده است: {e}")

if __name__ == "__main__":
    run_hp_display_center()