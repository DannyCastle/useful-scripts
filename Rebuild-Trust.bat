reg add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Power" /t REG_DWORD /v HiberbootEnabled /d 0 /f
Powershell.exe -executionpolicy bypass -file %~dp0Trust.ps1
timeout 10
shutdown /r /t 0