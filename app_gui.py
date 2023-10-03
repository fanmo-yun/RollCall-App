import sys
import csv
import time
import random
import threading
import tkinter as tk
from app_topgui import *
from tkinter import messagebox, filedialog, font

class RollCall_App(tk.Tk):
    def __init__(self,
                appName: str,
                appWidth: int,
                appHeight: int,
                IsResizable: bool,
                screenName: str | None = None,
                baseName: str | None = None,
                className: str = "Tk",
                useTk: bool = True,
                sync: bool = False,
                use: str | None = None
            ) -> None:
        super().__init__(screenName, baseName, className, useTk, sync, use)

        posWidth = int((self.winfo_screenwidth() - appWidth) / 2)
        posHeight = int((self.winfo_screenheight() - appHeight) / 2)

        self.appName = appName
        self.title(self.appName)
        self.geometry(f"{appWidth}x{appHeight}+{posWidth}+{posHeight}")
        self.resizable(width=IsResizable, height=IsResizable)
        
        self.delay = 0.04
        self.isRandom = False
        self.rollval = tk.StringVar()
        self.appList = list()
    
    def freeze_win(self):
        self.attributes("-disabled", True)
    
    def release_win(self):
        self.attributes("-disabled", False)
    
    def set_delay(self, set_delay_num: float):
        self.delay = set_delay_num
    
    def set_bgcolor(self, color: str):
        self.showLabel.configure(background=color)
    
    def set_font(self, fontname: str, fontcolor: str):
        self.showLabel.configure(font=fontname, fg=fontcolor)
    
    def set_font2(self, fontname: str):
        self.showLabel.configure(font=fontname)
    
    def set_font3(self, fontcolor: str):
        self.showLabel.config(fg=fontcolor)
    
    def menu_layout(self):
        self.appMenu = tk.Menu(self)
        
        self.fileMenu = tk.Menu(self.appMenu, tearoff=0)
        self.fileMenu.add_command(label="导入txt", command=self.process_txt)
        self.fileMenu.add_command(label="导入csv", command=self.process_csv)
        self.fileMenu.add_separator()
        self.fileMenu.add_command(label="清空列表", command=self.empty_list)
        self.appMenu.add_cascade(label="文件", menu=self.fileMenu)

        self.settingmenu = tk.Menu(self.appMenu, tearoff=0)
        self.settingmenu.add_command(label="设置延迟", command=self.setting_delay)
        self.settingmenu.add_command(label="设置字体", command=self.setting_font)
        self.settingmenu.add_command(label="设置背景", command=self.setting_background)
        self.appMenu.add_cascade(label="设置", menu=self.settingmenu)
        
        self.config(menu=self.appMenu)

    def main_layout(self):
        self.appframe = tk.Frame(self)
        self.appframe.pack()

        self.showLabel = tk.Label(master=self.appframe, width=22, height=3, background="yellow", textvariable=self.rollval)
        self.showLabel.pack(side=tk.TOP)

        self.Btn1 = tk.Button(self, width=12, height=2, text="随机点名", command=self.random_one)
        self.Btn1.pack(side=tk.LEFT, padx=32, pady=10)

        self.Btn2 = tk.Button(self, width=12, height=2, text="动态点名", command=self.random_more)
        self.Btn2.pack(side=tk.LEFT, pady=10)
    
    def get_file(self, extension: str) -> str:
        return filedialog.askopenfilename(defaultextension=extension, filetypes=[("Text Files", "*" + extension)])

    def process_txt(self):
        try:
            filename = self.get_file(".txt")
            if (len(filename) != 0):
                with open(filename, "r", encoding="utf-8") as fp:
                    for name in fp.readlines():
                        if (len(name.strip()) != 0):
                            self.appList.append(name.strip())
                messagebox.showinfo(title=self.appName, message="添加成功")
        except:
            messagebox.showerror(title=self.appName, message="txt文件导入出现错误")

    def process_csv(self):
        try:
            filename = self.get_file(".csv")
            if (len(filename) != 0):
                with open(filename, "r", encoding="utf-8", newline="") as fp:
                    csv_content = csv.reader(fp, delimiter=',')
                    for names in csv_content:
                        for name in names:
                            if (len(name.strip()) != 0):
                                self.appList.append(name.strip())
                messagebox.showinfo(title=self.appName, message="添加成功")
        except:
            messagebox.showerror(title=self.appName, message="csv文件导入出现错误")

    def empty_list(self):
        if len(self.appList) != 0:
            self.appList.clear()
            self.rollval.set("")
            messagebox.showinfo(title=self.appName, message="已清除")
        else:
            messagebox.showinfo(title=self.appName, message="列表为空")
        
    def choice_more(self):
        while (self.isRandom):
            self.rollval.set(random.choice(self.appList))
            time.sleep(self.delay)
    
    def random_one(self):
        if (len(self.appList) != 0 and self.isRandom == False):
            self.rollval.set(random.choice(self.appList))
        elif (len(self.appList) != 0 and self.isRandom == True):
            pass
        else:
            messagebox.showwarning(title=self.appName, message="列表为空")
    
    def random_more(self):
        if (len(self.appList) != 0):
            if (self.isRandom == False):
                self.isRandom = True
                self.appThread1 = threading.Thread(target=self.choice_more)
                self.appThread1.start()
            else:
                self.isRandom = False
        else:
            messagebox.showwarning(title=self.appName, message="列表为空")

    def setting_font(self):
        if (self.isRandom == False):
            self.isRandom = True
        self.freeze_win()
        self.setting_font_win = setting_font_win(appName="设置字体", appWidth=350, appHeight=250, IsResizable=False, set_font=self.set_font, set_font2=self.set_font2, set_font3=self.set_font3, signal=self.release_win)
        self.setting_font_win.run()

    def setting_background(self):
        if (self.isRandom == False):
            self.isRandom = True
        self.freeze_win()
        self.setting_background_win = setting_background_win(appName="设置背景", appWidth=220, appHeight=70, IsResizable=False, set_color=self.set_bgcolor, signal=self.release_win)
        self.setting_background_win.run()

    def setting_delay(self):
        if (self.isRandom == False):
            self.isRandom = True
        self.freeze_win()
        self.setting_delay_win = setting_delay_win(appName="设置延迟", appWidth=220, appHeight=100, IsResizable=False, master_time=self.set_delay, signal=self.release_win)
        self.setting_delay_win.run()

    def destroy_self(self):
        self.isRandom = False
        sys.exit(0)
    
    def run(self):
        self.menu_layout()
        self.main_layout()
        self.protocol("WM_DELETE_WINDOW", self.destroy_self)
        self.mainloop()