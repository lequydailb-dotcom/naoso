@echo off
chcp 65001 >nul
title Khoi dong NAOTA
cd /d "%~dp0"

echo Bat NAOTA chay NEN - khong con cua so den (port 7777)...
REM Viec tat instance cu + chay server AN giao het cho start-naota.vbs (cua so an hoan toan).
REM Log ghi vao server\naota.log (mo file do neu can xem loi). Tat server: stop-naota.bat.
wscript //nologo start-naota.vbs

echo.
echo Da bat. Cho ~10 giay roi mo http://localhost:7777 va bam Ctrl+Shift+R.
echo (Tat server: chay stop-naota.bat. Xem loi: mo file server\naota.log)
timeout /t 4 >nul
