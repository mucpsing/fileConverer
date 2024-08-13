# -*- coding: utf-8 -*-
#
# @Author: CPS
# @email: 373704015@qq.com
# @Date: 2024-08-13 14:54:02.231537
# @Last Modified by: CPS
# @Last Modified time: 2024-08-13 14:54:02.231537
# @file_path "W:\CPS\MyProject\projsect_persional\fileConverer\src"
# @Filename "main.py"
# @Description: 功能描述
#
import os, sys

sys.path.append("..")

from os import path
from pathlib import Path
from pydantic import BaseModel

from typing import List, Tuple

from src.pdf_mamanger import merge_pdfs
from src.word2pdf.word_to_pdf_by_word import CpsWordConverter, CpsWordConverterConfig


def file_list_handler(file_list: List[str], output_dir: str = None):
    # 查找word文件
    word_list = []
    # 查找pdf文件
    pdf_list = []
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


if __name__ == "__main__":
    pass
