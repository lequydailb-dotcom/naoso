@echo off
chcp 65001 >nul
title Khoi dong VANHANH
cd /d "%~dp0"

echo Bat VANHANH chay NEN - khong con cua so den (port 7777)...
REM Viec tat instance cu + chay server AN giao het cho start-vanhanh.vbs (cua so an hoan toan).
REM Log ghi vao server\vanhanh.log (mo file do neu can xem loi). Tat server: stop-vanhanh.bat.
wscript //nologo start-vanhanh.vbs

echo.
echo Da bat. Cho ~10 giay roi mo http://localhost:7777 va bam Ctrl+Shift+R.
echo (Tat server: chay stop-vanhanh.bat. Xem loi: mo file server\vanhanh.log)
timeout /t 4 >nul
