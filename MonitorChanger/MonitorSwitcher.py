import subprocess
import pyautogui
import time
import psutil
import keyboard
import sys

class HPDisplayController:
    def __init__(self):
        self.app_path = r"C:\Program Files\WindowsApps\AD2F1837.HPDisplayCenter_2.2.8.0_x64__v10z8vjag6ke6\HPDisplayCenter.exe"
        self.app_name = "HPDisplayCenter.exe"
        self.app_window = None

    def get_primary_monitor_center(self):
        # Return the center coordinates of the primary monitor
        monitors = pyautogui.getAllMonitors()
        primary_monitor = [m for m in monitors if m.is_primary][0]
        return (
            primary_monitor.left + (primary_monitor.width // 2),
            primary_monitor.top + (primary_monitor.height // 2)
        )

    def move_window_to_center(self, hwnd):
        # Move the window to the center of the primary monitor
        try:
            # Get Primary monitor status
            monitor_info = win32api.GetMonitorInfo(win32api.MonitorFromPoint((0,0)))
            work_area = monitor_info["Work"]

            # Get Primary Monitor Size
            window_rect = win32gui.GetWindowRect(hwnd)
            window_width = window_rect[2] - window_rect[0]
            window_height = window_rect[3] - window_rect[1]

            # Calculate new position
            new_x = work_area[0] + (work_area[2] - work_area[0] - window_width) // 2
            new_y = work_area[1] + (work_area[3] - work_area[1] - window_height) // 2

            # Moving Windows to the center of primary monitor
            win32gui.MoveWindow(hwnd, new_x, new_y, window_width, window_height, True)
            return True
        except Exception as e:
            print(f"Error when Moving Windows to Center of Screen 1: {e}")
            return False

    def find_app_window(self, timeout=10):
       # this function is used to find the window of the HPDisplayCenter
        start_time = time.time()

        while time.time() - start_time < timeout:
            try:
                hwnd = win32gui.FindWindow(None, "HP Display Center")
                if hwnd:
                    self.app_window = hwnd
                    return True
            except:
                pass
            time.sleep(0.5)
        return False

    def is_app_running(self):
        # Checking is App Running or not?
        for process in psutil.process_iter(['name']):
            if process.info['name'] == self.app_name:
                return True
        return False

    def launch_app(self):
            # Launch the application in the Center of Primary Monitor
            try:
                # If App is Running then Activate app windows, else Launch the App
                if self.is_app_running():
                    print("HPDisplayCenter is already running => Activating...")
                    subprocess.Popen([self.app_path, '--activate'])
                else:
                    print("HPDisplayCenter is not running => Running...")
                    subprocess.Popen(self.app_path)

                # Waiting to open HPDisplayCenter Windows
                if not self.find_app_window():
                    print("HPDisplayCenter Windows is not found!")
                    return False

                # Moving HPDisplayCenter Windows to Center of Primary Monitor
                self.move_window_to_center(self.app_window)

                # Activate HPDisplayCenter Windows
                win32gui.SetForegroundWindow(self.app_window)

                print("HPDisplayCenter is Running in the Center of Primary Monitor Successfully!")
                return True

            except Exception as e:
                print(f"Error when Running HPDisplayCenter: {e}")
                return False

    def close_app(self):
        """Closing HPDisplayCenter"""
        try:
            for process in psutil.process_iter(['name', 'pid']):
                if process.info['name'] == self.app_name:
                    proc = psutil.Process(process.info['pid'])
                    proc.terminate()  # Using proc.kill() => For Force CLosing using
                    print("HPDisplayCenter Closed Successfully")
                    return True
            print("HPDisplayCenter is not Running!")
            return False
        except Exception as e:
            print(f"Error when Closing HPDisplayCenter: {e}")
            return False

    def hp_hdmi_switcher(self):
        try:
            self.launch_app()
            # # HP Display Center Exe file path
            # app_path = r"C:\Program Files\WindowsApps\AD2F1837.HPDisplayCenter_2.2.8.0_x64__v10z8vjag6ke6\HPDisplayCenter.exe"
            #
            # # Running HPDisplayCenter.exe
            # subprocess.Popen(app_path)
            # print("برنامه HPDisplayCenter با موفقیت اجرا شد.")

            # Wait to open App
            # time.sleep(5)

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
            print(f"Error when Switching to HDMI Port {e}")

        finally:
            self.close_app()
            print("HPDisplayCenter Closed Successfully")

    def hp_dp_switcher(self):
        try:
            self.launch_app()
            # # HP Display Center Exe file path
            # app_path = r"C:\Program Files\WindowsApps\AD2F1837.HPDisplayCenter_2.2.8.0_x64__v10z8vjag6ke6\HPDisplayCenter.exe"
            #
            # # Running HPDisplayCenter.exe
            # subprocess.Popen(app_path)
            # print("HPDisplayCenter Running Successfully.")

            # Wait to open App
            # time.sleep(5)

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
            print(f"Error when Switching to Display Port {e}")
        finally:
            self.close_app()
            print("HPDisplayCenter Closed Successfully")

# Function to set up hotkeys
def setup_hotkeys(controller):
    # Set Hotkeys
    keyboard.add_hotkey('ctrl+alt+f5', controller.hp_hdmi_switcher)
    keyboard.add_hotkey('ctrl+alt+f6', controller.hp_dp_switcher)
    keyboard.add_hotkey('ctrl+alt+q', lambda: sys.exit(0))

if __name__ == "__main__":
    # Requirements: pip install psutil pyautogui keyboard
    hpController = HPDisplayController()

    print("""
    ======================================
    HP Display Controller - Hotkey Mode
    ======================================
    Shortcuts:
    CTRL+ALT+F5  -> Switch to HDMI
    CTRL+ALT+F6  -> Switch to DisplayPort
    CTRL+ALT+Q   -> Exit Program
    ======================================
    Program is running in background...
    Press CTRL+ALT+Q to exit
    """)

    # Create & Configure Hotkeys
    setup_hotkeys(hpController)

    # Keep the program running
    try:
        keyboard.wait()  # Waiting for hotkeys to be pressed
    except KeyboardInterrupt:
        print("Goodbye Ninja.! 🥷🏼")
        pass
    finally:
        print("Program terminated.")


# if __name__ == "__main__":
#     hpController = HPDisplayController()
#     monitor = 0
#     while int(monitor) != 99:
#         monitor = input("Enter 1 for HDMI, 2 for Display Port, 99 for Exit: \n ::: ")
#         if int(monitor) == 1:
#             hpController.hp_hdmi_switcher()
#             hpController.close_app()
#         elif int(monitor) == 2:
#             hpController.hp_dp_switcher()
#             hpController.close_app()
#         elif int(monitor) == 99:
#             print("Goodbye Ninja.! 🥷🏼")
#         else:
#             print("Invalid Input !!!")
