@echo off
@charset utf-8
chcp 65001 > nul

setlocal EnableDelayedExpansion

REM 定义变量
set "menu_name=CpsScripts Word转pdf"
set "command_path=\"W:\CPS\python\python310_64\python.exe\""
set "srcript_path=\"W:\CPS\MyProject\projsect_persional\python-file-scripts\src\word2pdf\word_to_pdf_by_word.py\" \"%%V\"" 

set "command=!command_path! !srcript_path!"

REM 添加任何目录的右键菜单中
reg add "HKCR\Directory\Background\shell\%menu_name%" /ve /d "%menu_name%" /f
reg add "HKCR\Directory\Background\shell\%menu_name%\command" /ve /d "!command!" /f

echo 添加右键菜单项完成！
exit /b
