@echo off
chcp 65001 >nul
title Tu khoi dong NAOTA
REM Tu khoi dong Naota cung Windows. Dung: naota-autostart.bat install | uninstall | status
REM Logic nam trong naota-autostart.ps1 (ghi/xoa muc Naota trong HKCU Run, khong can quyen
REM admin). Bat roi thi dang nhap may la server tu chay nen va tu mo dashboard.
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0naota-autostart.ps1" %1
