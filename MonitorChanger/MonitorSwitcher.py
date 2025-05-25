import subprocess
import pyautogui
import time
import psutil

class HPDisplayController:
    def __init__(self):
        self.app_path = r"C:\Program Files\WindowsApps\AD2F1837.HPDisplayCenter_2.2.8.0_x64__v10z8vjag6ke6\HPDisplayCenter.exe"
        self.app_name = "HPDisplayCenter.exe"

    def is_app_running(self):
        # Checking is App Running or not?
        for process in psutil.process_iter(['name']):
            if process.info['name'] == self.app_name:
                return True
        return False

    def launch_app(self):
        # Launching HPDisplayCenter or open HPDisplayCenter
        if self.is_app_running():
            print("HPDisplayCenter is Running, Open Windows Now ")
            try:
                # activate HP Display Windows
                subprocess.Popen([self.app_path, '--activate'])
            except:
                print("Error when try to Open HPDisplayCenter Windows")
        else:
            print("HPDisplay Center is not Running!")
            try:
                subprocess.Popen(self.app_path)
                print("Now HP Display Center  Running Successfully")
            except Exception as e:
                print(f"Error when Running HPDisplayCenter: {e}")
                return False

        # صبر کردن تا برنامه باز شود
        time.sleep(5)
        return True

    def hp_hdmi_swithcer(self):
        try:
            self.launch_app()
            # # HP Display Center Exe file path
            # app_path = r"C:\Program Files\WindowsApps\AD2F1837.HPDisplayCenter_2.2.8.0_x64__v10z8vjag6ke6\HPDisplayCenter.exe"
            #
            # # Running HPDisplayCenter.exe
            # subprocess.Popen(app_path)
            # print("برنامه HPDisplayCenter با موفقیت اجرا شد.")

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

    def hp_dp_swithcer(self):
        try:
            self.launch_app()
            # # HP Display Center Exe file path
            # app_path = r"C:\Program Files\WindowsApps\AD2F1837.HPDisplayCenter_2.2.8.0_x64__v10z8vjag6ke6\HPDisplayCenter.exe"
            #
            # # Running HPDisplayCenter.exe
            # subprocess.Popen(app_path)
            # print("HPDisplayCenter Running Successfully.")

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
            pyautogui.moveTo(509, 380, duration=1)
            pyautogui.click()
            print("HDMI port selected.")

            print("HP Monitor Changed to HDMI Port")

        #x:511  y: 38006
        except Exception as e:
            print(f"خطا رخ داده است: {e}")


if __name__ == "__main__":
    hpController = HPDisplayController()
    monitor = 0
    while int(monitor) != 99:
        monitor = input("Enter 1 for HDMI, 2 for Display Port, 99 for Exit: \n ::: ")
        if int(monitor) == 1:
            hpController.hp_hdmi_swithcer()
        elif int(monitor) == 2:
            hpController.hp_dp_swithcer()
        else:
            print("Invalid Input !!!")
