from email import message
import socket, os, keyboard

message_to_teacher = "done"

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((socket.gethostbyname(socket.gethostname()), 55000))
sock.listen(10) 

while True:
    conn, addr = sock.accept()
    print('connected:', addr)
    data = conn.recv(1024)
    print(str(data))
    com = str(data).replace("b\'", "").replace("\'", "")

    if "!" in com:
        file = open('text.txt', 'w')
        com = com.replace("!", "")
        text = com
        text = text.replace("/10 ", "и")
        text = text.replace("/11 ", "й")
        text = text.replace("/12 ", "к")
        text = text.replace("/13 ", "л")
        text = text.replace("/14 ", "м")
        text = text.replace("/15 ", "н")
        text = text.replace("/16 ", "о")
        text = text.replace("/17 ", "п")
        text = text.replace("/18 ", "р")
        text = text.replace("/19 ", "с")
        text = text.replace("/20 ", "т")
        text = text.replace("/21 ", "у")
        text = text.replace("/22 ", "ф")
        text = text.replace("/23 ", "х")
        text = text.replace("/24 ", "ц")
        text = text.replace("/25 ", "ч")
        text = text.replace("/26 ", "ш")
        text = text.replace("/27 ", "щ")
        text = text.replace("/28 ", "ъ")
        text = text.replace("/29 ", "ы")
        text = text.replace("/30 ", "ь")
        text = text.replace("/31 ", "э")
        text = text.replace("/32 ", "ю")
        text = text.replace("/33 ", "я")
        text = text.replace("/1 ", "а")
        text = text.replace("/2 ", "б")
        text = text.replace("/3 ", "в")
        text = text.replace("/4 ", "г")
        text = text.replace("/5 ", "д")
        text = text.replace("/6 ", "е")
        text = text.replace("/7 ", "ё")
        text = text.replace("/8 ", "ж")
        text = text.replace("/9 ", "з")
        file.write(text)
        file.close()
        os.startfile("message.exe")
    elif com == "off ":
        os.system("shutdown /s")
    elif com == "close ":
        keyboard.press_and_release('alt + f4')
    elif com == "app_on ":
        try:
            os.system("taskkill /IM kill_app.exe /f")
        except:
            message_to_teacher = "error 2"
    elif com == "sd ":
        print("s")
        os.startfile("sdu.exe")
    elif com == "csd ":
        os.system("taskkill /IM sdu.exe /f")

    elif "rpl " in com:
        com = com.replace("rpl", "")
        p1, p2 = com.split()
        try:
            os.replace(p1, p2)
        except:
            message_to_teacher = "error 1"
    elif "cmd " in com:
        com = com.replace("cmd ", "")
        try:
            os.system(com)
        except:
            message_to_teacher = "error 3"
    # elif "open " in com:
    #     com = com.replace("open ","")
    #     os.system(com)
    elif "app_off " in com:
        file = open('text.txt', 'w')
        com = com.replace("app_off ", "")
        file.write(com)
        file.close()
        os.startfile("kill_app.exe")
    elif "scr/;/;0 " in com:
        com = com.replace("scr/;/;0 ", "")
        if com == "srart":
            script_file = open('u_scr.bat', 'w')
            script_file.close()
        script_file = open("u_scr.bat", "a")
        script_file.write(com)
        if com == "stop/end__2qpw":
            script_file.close()
            os.system("u_scr.bat")
conn.close()
