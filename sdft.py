import socket, cv2, sys, pickle, struct, pyautogui
import numpy as np
from PIL import Image

number_file = open("sdft.txt", "r")
number_from_txt = number_file.readline()
number_from_txt = int(number_from_txt.replace("\n", ""))
number_file.close()

text_file = open("ip.txt", "r")
for i in range(1, number_from_txt + 1):
    ip = text_file.readline()
ip = ip.replace("\n", "")
text_file.close()
print(ip)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
while True:
    try:
        sock.connect((ip, 7777))
        break
    except:
        pass
 
def screen_demonstration():
    while True:
        image = pyautogui.screenshot()
        image = image.resize((1366, 768), Image.ANTIALIAS)
        image = np.array(image)
        img = Image.frombytes('RGB', (1366, 768), image)
        data = pickle.dumps(np.array(img))
        sock.sendall(struct.pack("L", len(data)) + data)


screen_demonstration()