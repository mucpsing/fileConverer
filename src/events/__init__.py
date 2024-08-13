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
from src.pdf_mamanger import merge_pdfs
from src.word2pdf.word_to_pdf_by_word import CpsWordConverter, CpsWordConverterConfig

from typing import List
from multiprocessing import Process


def file_list_handler(file_list: List[str], output_dir: str = None):
    # 查找word文件
    word_list = []
    # 查找pdf文件
    pdf_list = []

    res_list = []
    for each_file in file_list:
        if each_file.endswith(".docx"):
            word_list.append(each_file)
        elif each_file.endswith(".pdf"):
            pdf_list.append(each_file)

    if len(word_list) > 0:
        # 使用多线程来调用 CpsWordConverter
        for each_word_file in word_list:
            CpsWordConverter(CpsWordConverterConfig(overwrite=False, show_details=True)).convert(each_word_file)

    if len(pdf_list) > 0:
        merge_pdfs(pdf_list)


class UI_Var:
    Text1Var = "文件路径选择输入框，使用self.Text1Var.get()"


class UI_Events:
    def mainBtn_run_Cmd(self):
        """运行按钮"""
        if len(self.file_list) > 0:
            p = Process(target=file_list_handler, args=(self.file_list,))
            p.start()

    def mainBtn_outputSelect_Cmd(self):
        """输出路径选择按钮"""
        sel_path = selectPath("dir")
        if sel_path:
            if os.path.exists(sel_path):
                self.output_path = str(sel_path)
                self.mainText_outputPathVar.set(sel_path)

    def mianList_ListboxSelect(self, event):
        # 获取当前选中的项目（索引）列表
        widget = event.widget
        selection = widget.curselection()
        # 遍历所有选中的项目
        for index in selection:
            # 将选择的文件复制到输出框
            self.mainText_outputPathVar.set(widget.get(index))
            self.output_path = str(widget.get(index))
            break

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
