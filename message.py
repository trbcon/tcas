import tkinter as tk

f = open('text.txt', 'r')
msg = f.read()
f.close

root = tk.Tk()
# root.geometry('600x400')
root['bg'] = 'white'
label = tk.Label(fg = "DeepSkyBlue2", bg = "white", width = 100, font = "Calibri 30", text=msg)
label.pack()
root.mainloop()