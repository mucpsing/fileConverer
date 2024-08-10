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
        self.master.title('ConfEditorForm')
        self.master.geometry('274x475')
        self.createWidgets()

    def createWidgets(self):
        self.top = self.winfo_toplevel()

        self.style = Style()

        self.style.configure('TFrame1.TLabelframe', font=('宋体',9))
        self.style.configure('TFrame1.TLabelframe.Label', font=('宋体',9))
        self.Frame1 = LabelFrame(self.top, text='配置编辑器', style='TFrame1.TLabelframe')
        self.Frame1.place(relx=0.029, rely=0.017, relwidth=0.938, relheight=0.962)

        self.confEditorBtn_cannelVar = StringVar(value='取  消')
        self.style.configure('TconfEditorBtn_cannel.TButton', font=('宋体',9))
        self.confEditorBtn_cannel = Button(self.Frame1, text='取  消', textvariable=self.confEditorBtn_cannelVar, command=self.confEditorBtn_cannel_Cmd, style='TconfEditorBtn_cannel.TButton')
        self.confEditorBtn_cannel.setText = lambda x: self.confEditorBtn_cannelVar.set(x)
        self.confEditorBtn_cannel.text = lambda : self.confEditorBtn_cannelVar.get()
        self.confEditorBtn_cannel.place(relx=0.498, rely=0.893, relwidth=0.471, relheight=0.09)

        self.confEditorBtn_saveVar = StringVar(value='保  存')
        self.style.configure('TconfEditorBtn_save.TButton', font=('宋体',9))
        self.confEditorBtn_save = Button(self.Frame1, text='保  存', textvariable=self.confEditorBtn_saveVar, command=self.confEditorBtn_save_Cmd, style='TconfEditorBtn_save.TButton')
        self.confEditorBtn_save.setText = lambda x: self.confEditorBtn_saveVar.set(x)
        self.confEditorBtn_save.text = lambda : self.confEditorBtn_saveVar.get()
        self.confEditorBtn_save.place(relx=0.031, rely=0.893, relwidth=0.44, relheight=0.09)


class Application(Application_ui):
    #这个类实现具体的事件处理回调函数。界面生成代码在Application_ui中。
    def __init__(self, master=None):
        super().__init__(master)

    def confEditorBtn_cannel_Cmd(self, event=None):
        #TODO, Please finish the function here!
        pass

    def confEditorBtn_save_Cmd(self, event=None):
        #TODO, Please finish the function here!
        pass

if __name__ == "__main__":
    top = Tk()
    Application(top).mainloop()



