import qrcode
from tkinter import *


root = Tk()
root.title("生成二维码")
#root.geometry("400x200")

e = Entry(root, width=60, font=("微软雅黑",16))
e.pack()

def get2Code():
    img = qrcode.make(e.get())
    with open(r'e:/test.png', 'wb') as f:
    
        img.save(f)
    img.show()

btn = Button(root, text="生成二维码", font=("微软雅黑",16), width=30, command=get2Code)
btn.pack()
    
root.mainloop()