import subprocess
import pyautogui
import time

def hp_hdmi_swithcer():
    try:
        # HP Display Center Exe file path
        app_path = r"C:\Program Files\WindowsApps\AD2F1837.HPDisplayCenter_2.2.8.0_x64__v10z8vjag6ke6\HPDisplayCenter.exe"

        # Running HPDisplayCenter.exe
        subprocess.Popen(app_path)
        print("برنامه HPDisplayCenter با موفقیت اجرا شد.")

        # Wait to open App
        time.sleep(5)

        # Clicking Codes
        # First Click: Open Monitor Selection PopUp => X:595 & Y:251
        pyautogui.moveTo(595, 251, duration=1)
        pyautogui.click()
        print("Monitor selection popup open.")

        # Second Click: Select HP Monitor => X:436 & Y:333
        pyautogui.moveTo(436, 333, duration=1)
        pyautogui.click()
        print("HP Monitor selected")

        # Waiting to select hp Monitor
        time.sleep(3)

        # Third Click: Goto input tab
        pyautogui.moveTo(801, 251, duration=1)
        pyautogui.click()
        print("Going to Input tab")

        # Fourth Click: Click on `HDMI` Button => X:612 & Y:378
        pyautogui.moveTo(612, 378, duration=1)
        pyautogui.click()
        print("HDMI port selected.")

        print("HP Monitor Changed to HDMI Port")

    #x:511  y: 38006
    except Exception as e:
        print(f"خطا رخ داده است: {e}")

    except Exception as e:
        print(f"خطا رخ داده است: {e}")

def hp_dp_swithcer():
    try:
        # HP Display Center Exe file path
        app_path = r"C:\Program Files\WindowsApps\AD2F1837.HPDisplayCenter_2.2.8.0_x64__v10z8vjag6ke6\HPDisplayCenter.exe"

        # Running HPDisplayCenter.exe
        subprocess.Popen(app_path)
        print("برنامه HPDisplayCenter با موفقیت اجرا شد.")

        # Wait to open App
        time.sleep(5)

        # Clicking Codes
        # First Click: Open Monitor Selection PopUp => X:595 & Y:251
        pyautogui.moveTo(595, 251, duration=1)
        pyautogui.click()
        print("Monitor selection popup open.")

        # Second Click: Select HP Monitor => X:436 & Y:333
        pyautogui.moveTo(436, 333, duration=1)
        pyautogui.click()
        print("HP Monitor selected")

        # Waiting to select hp Monitor
        time.sleep(3)

        # Third Click: Goto input tab
        pyautogui.moveTo(801, 251, duration=1)
        pyautogui.click()
        print("Going to Input tab")

        # Fourth Click: Click on `HDMI` Button => X:612 & Y:378
        pyautogui.moveTo(612, 378, duration=1)
        pyautogui.click()
        print("HDMI port selected.")

        # Five Click: Click on `DisplayPort` Button => X:511 & Y:38006
        pyautogui.moveTo(511, 38006, duration=1)
        pyautogui.click()
        print("HDMI port selected.")

        print("HP Monitor Changed to HDMI Port")

    #x:511  y: 38006
    except Exception as e:
        print(f"خطا رخ داده است: {e}")


if __name__ == "__main__":
    hp_dp_swithcer()