# -*- coding: utf-8 -*-
#
# @Author: CPS
# @email: 373704015@qq.com
# @Date: 2024-08-11 11:28:07.718227
# @Last Modified by: CPS
# @Last Modified time: 2024-08-11 11:28:07.718227
# @file_path "D:\CPS\MyProject\Projects_Personal\fileConverer\src"
# @Filename "test.py"
# @Description: 功能描述
#
import os, sys
import winreg as reg

sys.path.append("..")

from os import path
from pathlib import Path
from pydantic import BaseModel, Field
from enum import Enum


class RegKey(Enum):
    HKCR = reg.HKEY_CLASSES_ROOT
    HKCU = reg.HKEY_CURRENT_USER
    HKLM = reg.HKEY_LOCAL_MACHINE
    HKU = reg.HKEY_USERS
    HKCC = reg.HKEY_CURRENT_CONFIG


class MenuConfig(BaseModel):
    pass


class MenuItem(BaseModel):
    name: str
    file_type: str = Field("*", description="要出发的文件格式，*默认未所有文件")


class RegMenuManager:
    def __init__(self):
        pass

    def addFileMenu(self, item: MenuItem, menu_config: MenuConfig):
        try:
            # 创建一级菜单
            reg.CreateKeyEx(
                RegKey.HKCR,
                f"{item.file_type}\\shell\\{item.name}",
                0,
                reg.KEY_WRITE,
                None,
            )
        except Exception as e:
            print(f"Failed to create context menu item: {e}")

        try:
            # 打开HKCR下对应文件类型的shell键
            shell_key = reg.CreateKeyEx(
                reg.HKEY_CLASSES_ROOT,
                f"{item.file_type}\\shell\\{item.command_name}",
                0,
                reg.KEY_WRITE,
                None,
            )

            # 在shell键下创建一个command键，并设置其默认值为命令路径
            command_key = reg.CreateKeyEx(shell_key, "command", 0, reg.KEY_WRITE, None)
            reg.SetValueEx(command_key, "", 0, reg.REG_SZ, item.command_path)

            # 关闭键
            reg.CloseKey(command_key)
            reg.CloseKey(shell_key)
            print(
                f"Context menu item '{item.command_name}' created successfully for '{item.file_type}' files."
            )
        except Exception as e:
            print(f"Failed to create context menu item: {e}")


if __name__ == "__main__":
    pass
