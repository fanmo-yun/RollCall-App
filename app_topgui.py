import tkinter as tk
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
    def __init__(self, appName: str, appWidth: int, appHeight: int, IsResizable: bool, signal) -> None:
        super().__init__(appName, appWidth, appHeight, IsResizable)
        self.destroy_win_signal = signal
    
    def layout(self):
        pass

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

        self.btn = tk.Button(master=self.root, width=10, height=1, text="完成", command=lambda : self.set_delay(self.destroy_win_signal))
        self.btn.pack()
    
    def set_delay(self, singal):
        if Is_Number(self.spinbox.get()):
            num = float(self.spinbox.get())
            if (num <= 0):
                self.show_num_error()
            elif (num >= 5):
                self.show_num_error()
            else:
                self.set_delay_num(num)
                singal()
                self.root.destroy()
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
        mycolor = askcolor()
        print(type(mycolor), mycolor)
    
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