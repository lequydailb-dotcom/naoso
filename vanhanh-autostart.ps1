# ============================================================
# VANHANH - tu khoi dong cung Windows (ban sao cua bin/vanhanh-autostart.sh ben Mac).
# Goi qua vanhanh-autostart.bat, dung goi truc tiep tru khi biet minh dang lam gi.
#
# Cach lam: ghi DUNG muc ma dashboard bat/tat (HKCU\...\Run, ten "Vanhanh",
# khong can quyen admin), tro vao `wscript start-vanhanh.vbs /open`: dang nhap may la server
# tu chay NEN roi tu mo dashboard trong cua so rieng. install.ps1 goi file nay mac dinh.
# File nay khong dat shortcut trong thu muc Startup vi dashboard da ghi Run key: hai
# muc cung bat thi luc dang nhap hai ban Vanhanh gianh nhau cong 7777. Gio chi con Run key,
# shortcut cu bi xoa khi install/uninstall.
# ============================================================
param([string]$Action = "status")

$Root = Split-Path -Parent $MyInvocation.MyCommand.Path
$Startup = [Environment]::GetFolderPath("Startup")
$Lnk = Join-Path $Startup "VANHANH.lnk"          # muc cu, chi de don
$RunKey = "HKCU:\Software\Microsoft\Windows\CurrentVersion\Run"
$Approved = "HKCU:\Software\Microsoft\Windows\CurrentVersion\Explorer\StartupApproved\Run"
$Name = "Vanhanh"                                  # khop _AUTOSTART_NAME trong server/main.py

switch ($Action.ToLower()) {
  "install" {
    $vbs = Join-Path $Root "start-vanhanh.vbs"
    if (-not (Test-Path $vbs)) {
      Write-Host "Khong thay start-vanhanh.vbs canh script nay - dat vanhanh-autostart.ps1 o goc thu muc Vanhanh."
      exit 1
    }
    # Cung chuoi voi _autostart_command() trong server/main.py, de dashboard bao "Bat" chu khong bao "duong dan cu".
    $cmd = "wscript.exe //nologo `"$vbs`" /open"
    if (-not (Test-Path $RunKey)) { New-Item -Path $RunKey -Force | Out-Null }
    Set-ItemProperty -Path $RunKey -Name $Name -Value $cmd
    # Task Manager tat muc nay bang mot co rieng; bat lai thi go co do (giong nut trong dashboard).
    try {
      $raw = (Get-ItemProperty -Path $Approved -Name $Name -ErrorAction Stop).$Name
      if ($raw -and ($raw[0] -band 1)) {
        Set-ItemProperty -Path $Approved -Name $Name -Value ([byte[]](2,0,0,0,0,0,0,0,0,0,0,0))
      }
    } catch { }
    if (Test-Path $Lnk) { Remove-Item $Lnk -Force }
    Write-Host "Da bat tu khoi dong cung Windows: dang nhap may la Vanhanh tu chay va tu mo dashboard."
    Write-Host "Tat: vanhanh-autostart.bat uninstall (hoac nut trong dashboard, trang Cai dat)."
  }
  "uninstall" {
    Remove-ItemProperty -Path $RunKey -Name $Name -ErrorAction SilentlyContinue
    if (Test-Path $Lnk) { Remove-Item $Lnk -Force }
    Write-Host "Da tat tu khoi dong cung Windows."
  }
  default {
    $val = (Get-ItemProperty -Path $RunKey -Name $Name -ErrorAction SilentlyContinue).$Name
    if ($val) {
      Write-Host "DANG bat tu khoi dong: $val"
    } elseif (Test-Path $Lnk) {
      Write-Host "DANG bat theo kieu cu (shortcut $Lnk). Chay vanhanh-autostart.bat install de len kieu moi."
    } else {
      Write-Host "CHUA bat tu khoi dong. Bat bang: vanhanh-autostart.bat install"
    }
  }
}
