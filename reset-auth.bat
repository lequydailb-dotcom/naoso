echo   RESET DANG NHAP NAOSO
echo   (Xoa tai khoan/mat khau -> ve bo cai dat)
echo ==========================================
echo.
.venv\Scripts\python.exe -c "import json,os; p='server/settings.json'; d=(json.load(open(p,encoding='utf-8')) if os.path.exists(p) else {}); d['auth']={'username':'','password_hash':'','salt':''}; d['setup_done']=False; json.dump(d, open(p,'w',encoding='utf-8'), ensure_ascii=False, indent=2); print('OK - da xoa mat khau.')"
echo.
echo Da reset. Bay gio:
echo   1) Chay stop-naota.bat roi start-naota.vbs (hoac de nguyen cung duoc).
echo   2) Mo lai trang -> se ra bo cai dat de tao tai khoan moi.
echo.
pause
=======
@echo off
chcp 65001 >nul
title Xoa mat khau NAOSO
cd /d "%~dp0"
REM Xoa mat khau dang nhap NAOSO de dat lai tu dau (trang Tai khoan). Logic nam trong tools\reset_auth.py,
REM dung chung voi reset-auth.command cua macOS. Giu setup_done nen khong mo lai bo cai dat lan dau.
if not exist ".venv\Scripts\python.exe" (
  echo Khong thay .venv\Scripts\python.exe - hay cai NAOSO xong truoc.
  echo .venv\Scripts\python.exe not found - finish installing NAOSO first.
  pause
  exit /b 1
)
".venv\Scripts\python.exe" "tools\reset_auth.py"
echo.
pause
