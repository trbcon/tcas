import socket
import tkinter as tk
from tkinter import ttk

def help_user():
	window = tk.Toplevel(root)
	window.geometry("854x480")
	window['bg'] = 'gray10'

def gettxt():
    text = entry.get()
    number = pick_number.get()
    cipter(text, number)

def cipter(text, number):
	if "!" in text:
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

	if number != "all":
		send_one(text, number)
	else:
		send_all(text)

def send_one(text, number):
	perem = 0

	file = open("ip.txt", "r")
	while perem != int(number):
		ip = file.readline()
		perem += 1
	ip = ip.replace("\n", "")
	file.close()

	connect_and_send(ip, text)

def connect_and_send(ip, text):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect((ip, 55000))
	sock.send(bytes(text, encoding = 'UTF-8'))
	data = sock.recv(1024)
	print(data)
	sock.close()

def send_all(text):
	file = open("ip.txt", "r")

	for i in range(1, 11):
		ip = file.readline()
		ip = ip.replace("\n", "")
		connect_and_send(ip, text)

	file.close()



root = tk.Tk()
root.geometry("854x480")
root['bg'] = 'gray10'

entry = tk.Entry(fg = "DarkOrange2", bg = "gray17", width = 50, font = "Calibri 20")

send_button = tk.Button(fg = "DarkOrange2", bg = "gray1", text = "Отправить", command = gettxt, font = "Calibri 15")
help_button = tk.Button(fg = "DarkOrange2", bg = "gray1", text = "?", command = help_user, font = "Calibri 15")

num_label = tk.Label(fg = "DarkOrange1", bg = "gray10", font = "Calibri 30", text="Номер компьютера")
commands_label = tk.Label(fg = "DarkOrange1", bg = "gray10", font = "Calibri 30", text="Команды")

pick_number = ttk.Combobox(values = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "all"])

num_label.place(x = 40, y = 20)
commands_label.place(x = 40, y = 130)

pick_number.place(x = 40, y = 90, height=30, width=130)

entry.place(x = 40, y = 200, height=30, width=400)

send_button.place(x = 724, y = 450, height=30, width=130)
help_button.place(x = 821, y = 4, height=30, width=30)


root.mainloop()


