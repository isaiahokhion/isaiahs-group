from tkinter import Tk, Entry, Button, Label, StringVar

window = Tk()
window.geometry("500x300")
window.title("Emoji converter")

entry_txt = Entry(window, width=20)
entry_txt.pack(pady = 20)

result = StringVar()

result_label = Label(window, textvariable=result)
result_label.pack(pady = 20) 

emojis = {
    "happy": "😊",

    "sad": "😒",

    "excited": "😃",

    "tongue sticking out": "😛",

    "wink": "😉",

    "bored": "😐",

    "confused": "😕",

    "surprised": "😯",

    "cool": "😎",

    "angel": "😇",

    "love": "❤️",

    "angry": "😠",

    "in love": "😍",

    "shy": "😳",

    "laughing": "😂"

}

def newWindow():
    window2 = Tk()
    window2.geometry("400x250")
    window2.title("emoji Stuff")

    entry_txt = Entry(window2)
    
    entry_txt.pack()
    window2.mainloop()


