@echo off
chcp 65001 >nul
title Tu khoi dong VANHANH
REM Tu khoi dong Vanhanh cung Windows. Dung: vanhanh-autostart.bat install | uninstall | status
REM Logic nam trong vanhanh-autostart.ps1 (ghi/xoa muc Vanhanh trong HKCU Run, khong can quyen
REM admin). Bat roi thi dang nhap may la server tu chay nen va tu mo dashboard.
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0vanhanh-autostart.ps1" %1
