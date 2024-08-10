# -*- coding: utf-8 -*-
#
# @Author: CPS
# @email: 373704015@qq.com
# @Date: 2024-05-30 16:08:23.215384
# @Last Modified by: CPS
# @Last Modified time: 2024-05-30 16:08:23.215384
# @file_path "W:\CPS\MyProject\projsect_persional\python-tk-ui-learn\src"
# @Filename "tkinter_utils.py"
# @Description: 功能描述
#
import os, sys
from os import path

sys.path.append("..")
import tkinter
from tkinter.messagebox import showinfo
from tkinter import filedialog

from enum import Enum
from typing import Tuple, List, NewType

DIALOG_TYPES = NewType("Tuple[List[str]]", Tuple[List[str]])


class DialogTypeT(Enum):
    file = "file"
    dir = "dir"


def selectPath(
    dialog_type: DialogTypeT = DialogTypeT.file,
    root: str = os.getcwd(),
    filetypes: DIALOG_TYPES = None,
) -> str:
    """
    @Description 弹出一个选择框，可以选择文件和目录

    - param title                        :{str}          文件弹出框的标题
    - param dialog_type                  :{DialogTypeT}  文件类型
    - param root                         :{str}          工作目录
    - param filetypes=None               :{DIALOG_TYPES} 示例：(("txt","*.txt"),)

    @returns `{ str}` {description}

    """
    try:
        sel_path = ""
        if dialog_type == DialogTypeT.file.value:
            # 选择文件path_接收文件地址
            sel_path = filedialog.askopenfilename(
                title="选择文件",
                filetypes=(("*.py", "py"), ("*.txt", "txt")),
                initialdir=root,
            )

        elif dialog_type == DialogTypeT.dir.value:
            # 选择文件path_接收文件地址
            sel_path = filedialog.askdirectory(
                title="选择目录",
                initialdir=root,
            )

        return sel_path
    except Exception as e:
        print(e)
        return ""


def dragged_file(tk: tkinter.Tk):
    import windnd

    def dragged_files(files, encodeing="gbk"):
        msg = "\n".join((item.decode(encodeing) for item in files))

        showinfo("当前选择的文件: ", f"我拖放的文件: {msg}")

    windnd.hook_dropfiles(tk, func=dragged_files)
