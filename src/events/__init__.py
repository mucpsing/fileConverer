# -*- coding: utf-8 -*-
#
# @Author: CPS
# @email: 373704015@qq.com
# @Date: 2024-05-30 16:35:13.961047
# @Last Modified by: CPS
# @Last Modified time: 2024-05-30 16:35:13.961047
# @file_path "W:\CPS\MyProject\projsect_persional\python-tk-ui-learn\src"
# @Filename "events.py"
# @Description: 这是一个类似事件中心的组件，对应ui.py的Application类中所有回调方法
#
import os, sys

sys.path.append("..")

from src.utils.tk_utils import selectPath
from src.configEditor_launcher import UI as configEditor_show


class UI_Var:
    Text1Var = "文件路径选择输入框，使用self.Text1Var.get()"


class UI_Events:
    def mainBtn_sel_file_Cmd(self, event=None):
        """选择文件的按钮"""

        # 点击按钮打开文件的调用
        sel_path = selectPath("file")
        if sel_path:
            if os.path.exists(sel_path):
                self.Text1Var.set(sel_path)

    # def mainBtn_open_config_editor_Cmd(self, subFormConfig):
    #     """打开一个子窗口"""
    #     configEditor_show()
