from time import sleep
import tkinter as tk
from tkinter import messagebox
import os
import random
import threading

user_name = []
is_call = False

def show_xian():
    global is_call
    while is_call:
        val1.set(random.choice(user_name))
        sleep(0.04)

def show_person():
    global is_call
    if len(user_name) != 0:
        if is_call == False:
            is_call = True
            th1 = threading.Thread(target=show_xian)
            th1.start()
        else:
            is_call = False
    else:
        messagebox.showinfo(window,message="列表中没有任何东西")

def choose_person():
    val1.set('')
    def choose_file():
        is_or_not = messagebox.askyesno(message="are you sure")
        if is_or_not:
            try:
                user_name.clear()
                file_name = lb1.get(lb1.curselection())
                with open(file_name,'r',encoding='utf-8') as fp:
                    lines = fp.readlines()
                for i in lines:
                    user_name.append(i.split())
                messagebox.showinfo(message="添加成功")
                child_window.destroy()
            except:
                messagebox.showerror(message="添加失败")

    child_window = tk.Toplevel(window)
    child_window.title("选择文件")
    child_window.resizable(width=False,height=False)
    child_window.geometry("250x250")

    file_name = os.listdir('.')

    lb1 = tk.Listbox(child_window)
    lb1.pack()
    for item in file_name:
        lb1.insert("end",item)

    bu1 = tk.Button(child_window,width=10,height=3,text="选择此文件",command=choose_file)
    bu1.pack()

window = tk.Tk()
window.title('点名器')
window.resizable(width=False,height=False)
window.geometry('280x130')

val1 = tk.StringVar()
l1 = tk.Label(window,background='yellow',width=20,height=2,font=20,textvariable=val1)
l1.pack()

bu1 = tk.Button(width=10,height=2,text="点名",command=show_person)
bu2 = tk.Button(width=10,height=2,text="选择文件",command=choose_person)

bu1.place(x=40,y=60)
bu2.place(x=150,y=60)

if __name__ == '__main__':
    window.mainloop()
