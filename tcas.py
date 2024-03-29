from PyQt5 import QtWidgets, uic    
import socket, os
from tkinter.colorchooser import askcolor
from time import sleep

# ip.txt, cfs.txt, sdft.txt, scr.txt 

def get_var():
	bat_scrpit = 0
	number = ui.comNumb.currentText()
	command = ui.comL.currentText()
	if command == "message ":
		command = "!" + ui.line.text()
	elif command == "sd ":
		number_file = open("sdft.txt", "w")
		number_file.write(number)
		number_file.close()
		print("sw")
		os.startfile("sdft.exe")
	elif command == "csd":
		os.system("taskkill /IM sdft.exe /f")
	elif command == "cmd" or command == "rpl" or command == "app_off" or command == "app_on":
		command = command + " " + ui.line.text()
	elif command == "script":
		bat_scrpit = 1
		script_file = open("scr.txt", "w")
		script_file.close()
		os.system("scr.txt")
		tr_sc = 0
		while True:
			if tr_sc == 0:
				script_file = open("scr.txt", "r")
				data_script_file = script_file.readline()
				script_file.close()
				if data_script_file != "":
					tr_sc = 1
					script_file = open("scr.txt", "r")
			else:
				if number != "all":
					number = int(number)
				try:
					if tr_sc == 1:
						cipter("scr/;/;0 start", number)
						tr_sc += 1
					cipter(("scr/;/;0 " + script_file.readline()), number)
				except:
					cipter("scr/;/;0 stop/end__2qpw", number)
					break

	if number != "all":
		number = int(number)
	if bat_scrpit == 0:
		cipter(command, number)

"""conf = open("cfg.txt", "r")
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
	conf.close()"""

def cipter(text, number):
	if "!" in text:                      #шифрование текста для корректного вывода кирилицы
		text = text.replace("а", "/1 ")
		text = text.replace("б", "/2 ")
		text = text.replace("в", "/3 ")
		text = text.replace("г", "/4 ")
		text = text.replace("д", "/5 ")
		text = text.replace("е", "/6 ")
		text = text.replace("ё", "/7 ")
		text = text.replace("ж", "/8 ")
		text = text.replace("з", "/9 ")
		text = text.replace("и", "/10 ")
		text = text.replace("й", "/11 ")
		text = text.replace("к", "/12 ")
		text = text.replace("л", "/13 ")
		text = text.replace("м", "/14 ")
		text = text.replace("н", "/15 ")
		text = text.replace("о", "/16 ")
		text = text.replace("п", "/17 ")
		text = text.replace("р", "/18 ")
		text = text.replace("с", "/19 ")
		text = text.replace("т", "/20 ")
		text = text.replace("у", "/21 ")
		text = text.replace("ф", "/22 ")
		text = text.replace("х", "/23 ")
		text = text.replace("ц", "/24 ")
		text = text.replace("ч", "/25 ")
		text = text.replace("ш", "/26 ")
		text = text.replace("щ", "/27 ")
		text = text.replace("ъ", "/28 ")
		text = text.replace("ы", "/29 ")
		text = text.replace("ь", "/30 ")
		text = text.replace("э", "/31 ")
		text = text.replace("ю", "/32 ")
		text = text.replace("я", "/33 ")

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

def connect_and_send(ip, text):
    try:					#подключение и отправка
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((ip, 55000))
        sock.send(bytes(text, encoding = 'UTF-8'))
        # data = sock.recv(1024)
        # print(data)
        sock.close()
    except:
        pass

app = QtWidgets.QApplication([])
ui = uic.loadUi("tcas.ui")
ui.setWindowTitle("TCAS")

ui.okB.clicked.connect(get_var)

ui.show()
app.exec()