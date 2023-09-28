import random
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

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

        self.rollval = tk.StringVar()
        self.appList = list()
    
    def menu_layout(self):
        self.appMenu = tk.Menu(self)
        
        self.fileMenu = tk.Menu(self.appMenu, tearoff=0)
        self.fileMenu.add_command(label="导入txt", command=self.process_txt)
        self.fileMenu.add_command(label="导入xlsx", command=None)
        self.fileMenu.add_command(label="导入csv", command=None)
        self.fileMenu.add_separator()
        self.fileMenu.add_command(label="清空列表", command=self.empty_list)
        self.appMenu.add_cascade(label="文件", menu=self.fileMenu)

        self.settingMenu = tk.Menu(self.appMenu, tearoff=0)
        self.settingMenu.add_command(label="设置文字", command=None)
        self.settingMenu.add_command(label="设置颜色", command=None)
        self.settingMenu.add_command(label="设置延迟", command=None)
        self.appMenu.add_cascade(label="设置", menu=self.settingMenu)

        self.config(menu=self.appMenu)

    def main_layout(self):
        self.appframe = tk.Frame(self)
        self.appframe.pack()

        self.showLabel = tk.Label(master=self.appframe, width=22, height=3, font=20, background="yellow", textvariable=self.rollval)
        self.showLabel.pack(side=tk.TOP)

        self.Btn1 = tk.Button(self, width=10, height=2, text="随机点名", command=self.random_one)
        self.Btn1.pack(side=tk.LEFT, padx=40, pady=10)

        self.Btn2 = tk.Button(self, width=10, height=2, text="动态点名", command=None)
        self.Btn2.pack(side=tk.LEFT, pady=10)
    
    def get_file(self, extension: str) -> str:
        return filedialog.askopenfilename(defaultextension=extension, filetypes=[("Text Files", "*" + extension)])

    def process_txt(self):
        filename = self.get_file(".txt")
        if (len(filename) != 0):
            with open(filename, "r", encoding="utf-8") as fp:
                for name in fp.readlines():
                    if (len(name.strip()) != 0):
                        self.appList.append(name.strip())
        messagebox.showinfo(title=self.appName, message="添加成功")
    
    def process_xlsx(self):
        pass

    def process_csv(self):
        pass

    def empty_list(self):
        if len(self.appList) != 0:
            self.appList.clear()
            self.rollval.set("")
            messagebox.showinfo(title=self.appName, message="已清除")
        else:
            messagebox.showinfo(title=self.appName, message="列表为空")
    
    def random_one(self):
        if (len(self.appList) != 0):
            self.rollval.set(random.choice(self.appList))
        else:
            messagebox.showwarning(title=self.appName, message="列表为空")
    
    def random_more(self):
        pass
    
    def run(self):
        self.mainloop()

if __name__ == "__main__":
    app = RollCall_App(appName="RollCall", appWidth=280, appHeight=130, IsResizable=False)
    app.menu_layout()
    app.main_layout()
    app.run()