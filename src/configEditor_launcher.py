# -*- coding: utf-8 -*-
#
# @Author: CPS
# @email: 373704015@qq.com
# @Date: 2024-06-13 17:19:03.808006
# @Last Modified by: CPS
# @Last Modified time: 2024-06-13 17:19:03.808006
# @file_path "W:\CPS\MyProject\projsect_persional\python-tk-ui-learn\src"
# @Filename "configEditor_launcher.py"
# @Description: 子窗口的启动器，注册事件，重新配置窗体属性等
#
import os, sys
import tkinter

sys.path.append("..")

from src.ui.configEditor import Application
from src.events.configEditorEvents import Events

from pydantic import BaseModel
from tkinter.messagebox import showwarning


class SubWindowConfig(BaseModel):
    title: str
    width: int
    height: int
    left: int
    top: int


class UI(Events, Application):
    # 这个类实现具体的事件处理回调函数。界面生成代码在Application_ui中。
    def __init__(self, config: SubWindowConfig, parent):
        sub_tk = tkinter.Toplevel(parent.master)
        super().__init__(sub_tk)

        self.parent = parent
        self.master.title(config.title)
        self.master.geometry(f"{config.width}x{config.height}+{config.left}+{config.top}")
        self.master.protocol("WM_DELETE_WINDOW", self.on_close)

    def confEditorBtn_save_Cmd(self, event=None):
        showwarning("", "保存配置文件")

    def confEditorBtn_cannel_Cmd(self, event=None):
        self.on_close()

    def on_close(self):
        self.parent.configEditor = None
        self.master.destroy()


def create_window(config: SubWindowConfig):
    return UI


if __name__ == "__main__":
    config = SubWindowConfig()
    UI(config)
