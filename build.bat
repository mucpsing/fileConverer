@REM @Author: CPS
@REM @email: 373704015@qq.com
@REM @Date: 2024-06-03 14:56:59.722341
@REM Last Modified by: CPS
@REM Last Modified time: 2024-06-03 14:56:59.722341
@REM Modified time: 2024-06-03 14:56:59.722341
@REM @file_path "W:\CPS\MyProject\projsect_persional\python-tk-ui-learn"
@REM @Filename "build.bat"

@echo off && setlocal enabledelayedexpansion
@chcp 65001


pdm run python -m nuitka --onefile --windows-disable-console --plugin-enable=tk-inter --standalone --show-memory --show-progress --nofollow-imports --follow-import-to=src --output-dir=dist main.py

pause
