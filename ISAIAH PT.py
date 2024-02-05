from tkinter import Tk, Entry, Button, Label, StringVar

window = Tk()
window.geometry("500x300")
window.title("Emoji converter")

entry_txt = Entry(window, width=20)
entry_txt.pack(pady = 20)

result = StringVar()

result_label = Label(window, textvariable=result)
result_label.pack(pady = 20) 
