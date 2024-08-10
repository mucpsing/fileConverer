@REM @Author: CPS
@REM @email: 373704015@qq.com
@REM @Date: 
@REM Last Modified by: CPS
@REM Last Modified time: 2023-10-30 15:19:35.569025
@REM Modified time: 2023-10-30 15:19:35.569025
@REM @file_path "W:\CPS\MyProject\test"
@REM @Filename "00test.bat"
@REM 计算机\HKEY_CLASSES_ROOT\Directory\Background\shell\
@REM 计算机\HKEY_LOCAL_MACHINE\SOFTWARE\Classes\Directory\background\shell\ 目录右键

@echo off
@charset utf-8
chcp 65001 > nul

setlocal EnableDelayedExpansion

REM 定义变量
set "menuName=Test"
set "commandName=wordToPdf"
set "commandPath=\"W:\CPS\python\python310_64\python.exe\""

rem "%%W" 返回的是当前目录路径
set "srcriptPath=\"W:\CPS\MyProject\projsect_persional\python-file-scripts\src\word2pdf\word_to_pdf_by_word.py\" \"%%W\"" 
 
set "command=!commandPath! !srcriptPath!"

REM 添加任何目录的右键菜单中
reg add "HKCR\Directory\Background\shell\%menuName%" /ve /d "%menuName%" /f
reg add "HKCR\Directory\Background\shell\%menuName%\command" /ve /d "!command!" /f


rem reg add "HKLM\SOFTWARE\Classes\Directory\background\shell\" /ve /d "%menuName%" /f
rem reg add "HKLM\SOFTWARE\Classes\Directory\background\shell\%menuName%\command" /ve /d "!command!" /f

REM 创建注册表项，（添加在指定文件的右键菜单，只在文件右键时生效）
reg add "HKCR\*\shell\%menuName%" /ve /d "%menuName%" /f
reg add "HKCR\*\shell\%menuName%\command" /ve /d "!command!" /f

echo 添加右键菜单项完成！
pause
exit /b

