@echo off
title GEMA Test Package
where py >nul 2>&1
if %errorlevel%==0 (py "%~dp0gema_test.py" & goto :eof)
where python >nul 2>&1
if %errorlevel%==0 (python "%~dp0gema_test.py" & goto :eof)
echo Python 3 was not found.
echo Install Python 3 from https://www.python.org/downloads/
pause
