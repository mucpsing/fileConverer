#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from abc import abstractmethod
import os, sys
from tkinter import *
from tkinter.font import Font
from tkinter.ttk import *

# Usage:showinfo/warning/error,askquestion/okcancel/yesno/retrycancel
from tkinter.messagebox import *

# from tkinter import filedialog  #.askopenfilename()
# from tkinter import simpledialog  #.askstring()


class Application_ui(Frame):
    # 这个类仅实现界面生成功能，具体事件处理代码在子类Application中。
    def __init__(self, master=None):
        super().__init__(master)
        self.master.title("Form1")
        self.master.geometry("585x331")
        self.createWidgets()

    def createWidgets(self):
        self.top = self.winfo_toplevel()

        self.style = Style()

        self.mainBtn_runVar = StringVar(value="运     行")
        self.style.configure("TmainBtn_run.TButton", font=("宋体", 9))
        self.mainBtn_run = Button(
            self.top,
            text="运     行",
            textvariable=self.mainBtn_runVar,
            command=self.mainBtn_run_Cmd,
            style="TmainBtn_run.TButton",
        )
        self.mainBtn_run.setText = lambda x: self.mainBtn_runVar.set(x)
        self.mainBtn_run.text = lambda: self.mainBtn_runVar.get()
        self.mainBtn_run.place(relx=0.014, rely=0.846, relwidth=0.726, relheight=0.124)

        self.mainBtn_open_config_editorVar = StringVar(value="配置编辑器")
        self.style.configure("TmainBtn_open_config_editor.TButton", font=("宋体", 9))
        self.mainBtn_open_config_editor = Button(
            self.top,
            text="配置编辑器",
            textvariable=self.mainBtn_open_config_editorVar,
            command=self.mainBtn_open_config_editor_Cmd,
            style="TmainBtn_open_config_editor.TButton",
        )
        self.mainBtn_open_config_editor.setText = lambda x: self.mainBtn_open_config_editorVar.set(x)
        self.mainBtn_open_config_editor.text = lambda: self.mainBtn_open_config_editorVar.get()
        self.mainBtn_open_config_editor.place(relx=0.752, rely=0.846, relwidth=0.221, relheight=0.124)

        self.style.configure("TFrame1.TLabelframe", font=("宋体", 9))
        self.style.configure("TFrame1.TLabelframe.Label", font=("宋体", 9))
        self.Frame1 = LabelFrame(self.top, text="配置文件路径", style="TFrame1.TLabelframe")
        self.Frame1.place(relx=0.014, rely=0.628, relwidth=0.959, relheight=0.196)

        self.mainBtn_sel_fileVar = StringVar(value="点击打开或者拖拽文件")
        self.style.configure("TmainBtn_sel_file.TButton", font=("宋体", 9))
        self.mainBtn_sel_file = Button(
            self.top,
            text="点击打开或者拖拽文件",
            textvariable=self.mainBtn_sel_fileVar,
            command=self.mainBtn_sel_file_Cmd,
            style="TmainBtn_sel_file.TButton",
        )
        self.mainBtn_sel_file.setText = lambda x: self.mainBtn_sel_fileVar.set(x)
        self.mainBtn_sel_file.text = lambda: self.mainBtn_sel_fileVar.get()
        self.mainBtn_sel_file.place(relx=0.014, rely=0.024, relwidth=0.973, relheight=0.583)

        self.Text1Var = StringVar(value="")
        self.Text1 = Entry(self.Frame1, textvariable=self.Text1Var, font=("宋体", 9))
        self.Text1.setText = lambda x: self.Text1Var.set(x)
        self.Text1.text = lambda: self.Text1Var.get()
        self.Text1.place(relx=0.014, rely=0.246, relwidth=0.971, relheight=0.631)


class Application(Application_ui):
    # 这个类实现具体的事件处理回调函数。界面生成代码在Application_ui中。
    def __init__(self, master=None):
        super().__init__(master)

    def mainBtn_run_Cmd(self, event=None):
        # TODO, Please finish the function here!
        pass

    def mainBtn_open_config_editor_Cmd(self, event=None):
        # TODO, Please finish the function here!
        pass

    def mainBtn_sel_file_Cmd(self, event=None):
        # TODO, Please finish the function here!
        pass


if __name__ == "__main__":
    top = Tk()
    Application(top).mainloop()
