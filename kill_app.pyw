import psutil, os

f = open('text.txt', 'r')
app_name = f.read()
f.close

while True:
    for proc in psutil.process_iter():
        name = proc.name()
        # print(name)
        if name == app_name:
            os.system("taskkill /IM " + app_name + " /f")