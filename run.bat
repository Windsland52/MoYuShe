@echo off
setlocal

REM 获取当前目录
set "current_dir=%~dp0"

cd "%current_dir%"

REM 运行main.py文件
python "MoYuShe.py"

endlocal