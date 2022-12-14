import socket, os
import tkinter as tk
from tkinter import ttk
from tkinter.colorchooser import askcolor

conf = open("cfg.txt", "r")
fore_grount = conf.readline().replace("\n", "")
back_ground = conf.readline().replace("\n", "")
conf.close()
if fore_grount == "":
	fore_grount = "snow"
	back_ground = "gray10"
elif back_ground == "":
	back_ground = "gray10"

def fg_save():
	try:
		fg_color = askcolor()[1]
		conf = open("cfg.txt", "r")
		conf.readline()
		bg_color = conf.readline()
		conf.close()
		conf = open("cfg.txt", "w")
		conf.write(fg_color + "\n" + bg_color)
		conf.close()
	except:
		pass

def bg_save():
	bg_color = askcolor()[1]
	conf = open("cfg.txt", "r")
	fg_color = conf.readline()
	conf.close()
	conf = open("cfg.txt", "w")
	conf.write(fg_color + bg_color + "\n")
	conf.close()


def help_user():
	window = tk.Toplevel(root)
	window.geometry("854x480")
	window['bg'] = back_ground 

	help_label_1 = tk.Label(window, fg = fore_grount, bg = back_ground, font = "Calibri 15", text="1) Все сообщения, кроме команд, должны начинаться с \"!\"")
	help_label_2 = tk.Label(window, fg = fore_grount, bg = back_ground, font = "Calibri 15", text="2) Команды:")
	help_label_5 = tk.Label(window, fg = fore_grount, bg = back_ground, font = "Calibri 15", text="off - выключает компьютер")
	help_label_6 = tk.Label(window, fg = fore_grount, bg = back_ground, font = "Calibri 15", text="close - закрывает вкладку которая на данный момент открыта")
	help_label_7 = tk.Label(window, fg = fore_grount, bg = back_ground, font = "Calibri 15", text="app_off имя программы - запрещает доступ к данной программе")
	help_label_8 = tk.Label(window, fg = fore_grount, bg = back_ground, font = "Calibri 15", text="app_on имя программы - разрешает доступ к данной программе")
	help_label_9 = tk.Label(window, fg = fore_grount, bg = back_ground, font = "Calibri 15", text="rpl (файл) (папка) - перемещает файл в заданную папку.\n Например: E:/floader/text.txt C:/Users/User/floader")
	help_label_10 = tk.Label(window, fg = fore_grount, bg = back_ground, font = "Calibri 15", text="cmd команда - выполняет команду на компьютере ученика.\n Например cmd notepad.exe (открывает блокнот) ")
	help_label_11 = tk.Label(window, fg = fore_grount, bg = back_ground, font = "Calibri 15", text="sd команда - включает демонстрацию экрана учительского экрана ученику")
	help_label_12 = tk.Label(window, fg = fore_grount, bg = back_ground, font = "Calibri 15", text="сsd команда - выключает демонстрацию экрана учительского экрана ученику")

	help_label_1.place(x = 4, y = 4)
	help_label_2.place(x = 4, y = 34)
	help_label_5.place(x = 4, y = 64)
	help_label_6.place(x = 4, y = 94)
	help_label_7.place(x = 4, y = 124)
	help_label_8.place(x = 4, y = 154)
	help_label_9.place(x = 4, y = 184)
	help_label_10.place(x = 4, y = 234)
	help_label_11.place (x = 4, y = 294)
	help_label_12.place (x = 4, y = 324)

def settings():
	stg = tk.Toplevel(root)
	stg.geometry("854x480")
	stg['bg'] = back_ground

	fg_save_button = tk.Button(stg, fg = back_ground, bg = fore_grount, text = "Цвет текста", command = fg_save, font = "Calibri 15")
	bg_save_button = tk.Button(stg, fg = back_ground, bg = fore_grount, text = "Цвет фона", command = bg_save, font = "Calibri 15")

	fg_save_button.place(x = 4, y = 4, height=30, width=130)
	bg_save_button.place(x = 4, y = 38, height = 30, width = 130)

def get_text():
    text = entry.get()
    number = pick_number.get()
    cipter(text, number)



def cipter(text, number):
	if "!" in text:                      #шифрование текста для корректного вывода кирилицы
		text = text.replace("а", "1 ")
		text = text.replace("б", "2 ")
		text = text.replace("в", "3 ")
		text = text.replace("г", "4 ")
		text = text.replace("д", "5 ")
		text = text.replace("е", "6 ")
		text = text.replace("ё", "7 ")
		text = text.replace("ж", "8 ")
		text = text.replace("з", "9 ")
		text = text.replace("и", "10 ")
		text = text.replace("й", "11 ")
		text = text.replace("к", "12 ")
		text = text.replace("л", "13 ")
		text = text.replace("м", "14 ")
		text = text.replace("н", "15 ")
		text = text.replace("о", "16 ")
		text = text.replace("п", "17 ")
		text = text.replace("р", "18 ")
		text = text.replace("с", "19 ")
		text = text.replace("т", "20 ")
		text = text.replace("у", "21 ")
		text = text.replace("ф", "22 ")
		text = text.replace("х", "23 ")
		text = text.replace("ц", "24 ")
		text = text.replace("ч", "25 ")
		text = text.replace("ш", "26 ")
		text = text.replace("щ", "27 ")
		text = text.replace("ъ", "28 ")
		text = text.replace("ы", "29 ")
		text = text.replace("ь", "30 ")
		text = text.replace("э", "31 ")
		text = text.replace("ю", "32 ")
		text = text.replace("я", "33 ")

	print(text)
	
	if number != "all":							#отправка конкретному пользователю
		if text == "sd":						#включение демонстрации экрана если text равна sd
			sdft_file = open("sdft.txt", "w")
			sdft_file.write(number)
			sdft_file.close()
			os.startfile("sdft.exe")
		elif text == "csd":						#выключение демонстрации экрана если text равна csd
			os.system("taskkill /IM sdft.exe /f")
		send_one(text, number)
	else:                                        #отправка всем пользователям
		if text == "sd":
			for i in range(1,11):
				sdft_file = open("sdft.txt", "w")
				sdft_file.write(i)
				sdft_file.close()
				os.startfile("sdft.exe")
		send_all_user(text)

def send_one(text, number):						#отправка конкретному пользователю
	perem = 0

	file = open("ip.txt", "r")
	while perem != int(number):
		ip = file.readline()
		perem += 1
	ip = ip.replace("\n", "")
	file.close()

	connect_and_send(ip, text)

def send_all_user(text):						#отправка всем пользователям
	file = open("ip.txt", "r")

	for i in range(1, 11):
		ip = file.readline()
		ip = ip.replace("\n", "")
		connect_and_send(ip, text)

	file.close()

def connect_and_send(ip, text):					#подключение и отправка
	try:
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.connect((ip, 55000))
		sock.send(bytes(text, encoding = 'UTF-8'))
		data = sock.recv(1024)
		print(data)
		sock.close()
	except:
		print(ip)


# Графический интерфейс
root = tk.Tk()
root.geometry("854x480")
root['bg'] = back_ground

entry = tk.Entry(fg = fore_grount, bg = fore_grount, width = 50, font = "Calibri 20")

send_button = tk.Button(fg = back_ground, bg = fore_grount, text = "Отправить", command = get_text, font = "Calibri 15")
help_button = tk.Button(fg = back_ground, bg = fore_grount, text = "?", command = help_user, font = "Calibri 15")
settings_button = tk.Button(fg = back_ground, bg = fore_grount, text = "Настройки", command = settings, font = "Calibri 15")

num_label = tk.Label(fg = fore_grount, bg = back_ground, font = "Calibri 20", text="Номер компьютера")
commands_label = tk.Label(fg = fore_grount, bg = back_ground, font = "Calibri 20", text="Команды")

pick_number = ttk.Combobox(values = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "all"])

num_label.place(x = 40, y = 20)
commands_label.place(x = 40, y = 110)

pick_number.place(x = 40, y = 70, height=30, width=130)

entry.place(x = 40, y = 170, height=30, width=400)

send_button.place(x = 724, y = 450, height=30, width=130)
help_button.place(x = 821, y = 4, height=30, width=30)
settings_button.place(x = 700, y = 4, height=30, width=120)

root.mainloop()
