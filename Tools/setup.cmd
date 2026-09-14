@echo off
rem Double click this file on Windows to set the computer up. It runs Tools\setup.ps1.
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0setup.ps1" %*
echo.
pause
