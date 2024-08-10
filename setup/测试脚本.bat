@REM @Author: CPS
@REM @email: 373704015@qq.com
@REM @Date: 
@REM Last Modified by: CPS
@REM Last Modified time: 2024-08-09 17:59:33.825123
@REM Modified time: 2024-08-09 17:59:33.825123
@REM @file_path "W:\CPS\MyProject\projsect_persional\python-file-scripts\setup"
@REM @Filename "【任意文件】右键菜单.bat"

@echo off && setlocal enabledelayedexpansion
@chcp 65001



REM 定义变量
set "menu_name=CpsScripts Test"
set "command_path=\"W:\CPS\python\python310_64\python.exe\""
set "srcript_path=\"W:\CPS\MyProject\projsect_persional\python-file-scripts\src\test.py\" \"%%1\"" 

set "command=!command_path! !srcript_path!"

REM 添加任何目录的右键菜单中
reg add "HKCR\*\shell\%menu_name%" /ve /d "%menu_name%" /f
reg add "HKCR\*\shell\%menu_name%\command" /ve /d "!command!" /f

echo 添加右键菜单项完成！
pause
exit /b
