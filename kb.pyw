import psutil, os
while True:
    for proc in psutil.process_iter():
        name = proc.name()
        # print(name)
        if name == "notepad.exe":
            os.system("taskkill /IM notepad.exe /f")