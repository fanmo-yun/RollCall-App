import tkinter as tk
import tkinter.ttk as ttk
from tkinter import font
from tkinter import messagebox
from tkinter.colorchooser import askcolor

def Is_Number(num):
    try:
        float(num)
        return True
    except ValueError:
        pass
 
    try:
        import unicodedata
        unicodedata.numeric(num)
        return True
    except (TypeError, ValueError):
        pass
 
    return False

class RollCall_TopLevel():
    def __init__(self, appName: str, appWidth: int, appHeight: int, IsResizable: bool) -> None:
        self.root = tk.Toplevel()

        posWidth = int((self.root.winfo_screenwidth() - appWidth) / 2)
        posHeight = int((self.root.winfo_screenheight() - appHeight) / 2)
        
        self.root.title(appName)
        self.root.geometry(f'{appWidth}x{appHeight}+{posWidth}+{posHeight}')
        self.root.resizable(width=IsResizable, height=IsResizable)
    
    def run(self):
        self.root.mainloop()

class setting_font_win(RollCall_TopLevel):
    def __init__(self, appName: str, appWidth: int, appHeight: int, IsResizable: bool, set_font, set_font2, set_font3, signal) -> None:
        super().__init__(appName, appWidth, appHeight, IsResizable)
        self.root.grid_rowconfigure(1,weight=1)
        self.root.grid_columnconfigure(0,weight=1)
        self.destroy_win_signal = signal
        self.set_font = set_font
        self.set_font2 = set_font2
        self.set_font3 = set_font3
        self.font_name = None
        self.colors = None
    
    def choose_color(self):
        self.root.grab_set()
        mycolor = askcolor()
        self.root.grab_release()
        self.colors =  mycolor
    
    def completed(self):
        try:
            self.font_name = self.fontlistbox.get(self.fontlistbox.curselection())
        except:
            pass
        if (self.colors != None and self.font_name != None):
            self.set_font(self.font_name, self.colors[1])
        elif (self.font_name != None):
            self.set_font2(self.font_name)
        elif (self.colors != None):
            self.set_font3(self.colors[1])
        self.destroy_self()
    
    def layout(self):
        self.fontlistbox = tk.Listbox(self.root, height=7)
        self.fontlistbox.pack(pady=10)
        for f in font.families():
            self.fontlistbox.insert(tk.END, f)

        self.dropdown_font_size = tk.Button(self.root, text="选择字体颜色", width=10, command=self.choose_color)
        self.dropdown_font_size.pack(pady=10)

        self.done_btn = tk.Button(self.root, width=10, text="设置字体", command=self.completed)
        self.done_btn.pack(pady=10)

    def destroy_self(self):
        self.destroy_win_signal()
        self.root.destroy()

    def run(self):
        self.layout()
        self.root.protocol("WM_DELETE_WINDOW", self.destroy_self)
        self.root.mainloop()

class setting_delay_win(RollCall_TopLevel):
    def __init__(self, appName: str, appWidth: int, appHeight: int, IsResizable: bool, master_time, signal) -> None:
        super().__init__(appName, appWidth, appHeight, IsResizable)
        self.set_delay_num = master_time
        self.destroy_win_signal = signal
    
    def layout(self):
        self.spinbox = tk.Spinbox(master=self.root, from_=0.01, to=5, format="%.2f", increment='0.01')
        self.spinbox.pack(pady=2)
        
        self.label = tk.Label(master=self.root, text="可以设置0.01 ~ 5.00之间")
        self.label.pack(pady=2)

        self.btn = tk.Button(master=self.root, width=10, height=1, text="完成", command=self.set_delay)
        self.btn.pack()
    
    def set_delay(self):
        if Is_Number(self.spinbox.get()):
            num = float(self.spinbox.get())
            if (num <= 0):
                self.show_num_error()
            elif (num >= 5):
                self.show_num_error()
            else:
                self.set_delay_num(num)
                self.destroy_self()
        else:
            self.show_num_error()
    
    def destroy_self(self):
        self.destroy_win_signal()
        self.root.destroy()
    
    def show_num_error(self):
        self.root.grab_set()
        messagebox.showerror(title="设置延迟", message="数字有误或异常")
        self.root.grab_release()

    def run(self):
        self.layout()
        self.root.protocol("WM_DELETE_WINDOW", self.destroy_self)
        self.root.mainloop()

class setting_background_win(RollCall_TopLevel):
    def __init__(self, appName: str, appWidth: int, appHeight: int, IsResizable: bool, set_color, signal) -> None:
        super().__init__(appName, appWidth, appHeight, IsResizable)
        self.color = set_color
        self.destroy_win_signal = signal
    
    def choose_color(self):
        self.root.grab_set()
        mycolor = askcolor()
        self.root.grab_release()
        if (mycolor[0] != None and mycolor[1] != None):
            self.color(mycolor[1])
            self.destroy_self()

    def layout(self):
        self.btn = tk.Button(self.root, text="选择颜色", command=self.choose_color, width=8)
        self.btn.pack(pady=14)

    def destroy_self(self):
        self.destroy_win_signal()
        self.root.destroy()

    def run(self):
        self.layout()
        self.root.protocol("WM_DELETE_WINDOW", self.destroy_self)
        self.root.mainloop()