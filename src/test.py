# -*- coding: utf-8 -*-
#
# @Author: CPS
# @email: 373704015@qq.com
# @Date:
# @Last Modified by: CPS
# @Last Modified time: 2024-06-14 16:05:44.492497
# @file_path "W:\CPS\MyProject\projsect_persional\python-tk-ui-learn\src"
# @Filename "test.py"
# @Description: 功能描述
#
import os, sys, tkinter

sys.path.append("..")

from os import path
from pathlib import Path
from pydantic import BaseModel


class SubWindowConfig(BaseModel):
    title: str
    width: int
    height: int


if __name__ == "__main__":
    config = SubWindowConfig(
        title="配置编辑器",
        width=300,
        height=500,
    )
    print("config: ", config)
