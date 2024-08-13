#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import os, sys
from tkinter import *
from tkinter.font import Font
from tkinter.ttk import *
#Usage:showinfo/warning/error,askquestion/okcancel/yesno/retrycancel
from tkinter.messagebox import *
#from tkinter import filedialog  #.askopenfilename()
#from tkinter import simpledialog  #.askstring()

class Application_ui(Frame):
    #这个类仅实现界面生成功能，具体事件处理代码在子类Application中。
    def __init__(self, master=None):
        super().__init__(master)
        self.master.title('Form1')
        self.master.geometry('583x289+0-12')
        self.createWidgets()

    def createWidgets(self):
        self.top = self.winfo_toplevel()

        self.style = Style()

        self.mainBtn_runVar = StringVar(value='运     行')
        self.style.configure('TmainBtn_run.TButton', font=('宋体',9))
        self.mainBtn_run = Button(self.top, text='运     行', textvariable=self.mainBtn_runVar, command=self.mainBtn_run_Cmd, style='TmainBtn_run.TButton')
        self.mainBtn_run.setText = lambda x: self.mainBtn_runVar.set(x)
        self.mainBtn_run.text = lambda : self.mainBtn_runVar.get()
        self.mainBtn_run.place(relx=0.014, rely=0.803, relwidth=0.962, relheight=0.17)

        self.style.configure('TmainListTitle.TLabelframe', font=('宋体',9))
        self.style.configure('TmainListTitle.TLabelframe.Label', font=('宋体',9))
        self.mainListTitle = LabelFrame(self.top, text='文件列表', style='TmainListTitle.TLabelframe')
        self.mainListTitle.place(relx=0.014, rely=0.028, relwidth=0.962, relheight=0.751)

        self.mianListVar = StringVar(value='mianList')
        self.mianListFont = Font(font=('宋体',9))
        self.mianList = Listbox(self.mainListTitle, listvariable=self.mianListVar, font=self.mianListFont)
        self.mianList.place(relx=0.014, rely=0.074, relwidth=0.971, relheight=0.903)
        self.mianList.bind('<<ListboxSelect>>', self.mianList_ListboxSelect)


class Application(Application_ui):
    #这个类实现具体的事件处理回调函数。界面生成代码在Application_ui中。
    def __init__(self, master=None):
        super().__init__(master)

    def mainBtn_run_Cmd(self, event=None):
        #TODO, Please finish the function here!
        pass

    def mianList_ListboxSelect(self, event):
        #TODO, Please finish the function here!
        pass

if __name__ == "__main__":
    top = Tk()
    Application(top).mainloop()



