import socket
import tkinter as tk
from tkinter import ttk

def gettxt():
    text_from_entry = entry.get()
    number = pick_number.get()
    send(text_from_entry, number)

def send(text, number):
	perem = 0

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

	file = open("ip.txt", "r")
	while perem != int(number):
		ip = file.readline()
		perem += 1
	ip = ip.replace("\n", "")
	file.close()

	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect((ip, 55000))
	sock.send(bytes(text, encoding = 'UTF-8'))
	data = sock.recv(1024)
	print(data)
	sock.close()



root = tk.Tk()
root.geometry("500x500")
root['bg'] = 'white'
entry = tk.Entry(fg = "DeepSkyBlue2", bg = "white", width = 50, font = "Calibri 30")
button = tk.Button(fg = "DeepSkyBlue2", bg = "white", text = "Отправить", command = gettxt, font = "Calibri 15")
label = tk.Label(fg = "DeepSkyBlue2", bg = "white", width = 50, font = "Calibri 30", text="Команды")
label1 = tk.Label(fg = "DeepSkyBlue2", bg = "white", width = 50, font = "Calibri 30", text="Номер компьютера")
pick_number = ttk.Combobox(values = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"])
label1.pack()
pick_number.pack()
label.pack()
entry.pack()
button.pack()
root.mainloop()


