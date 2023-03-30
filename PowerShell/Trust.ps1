#make sure in admin mode
if (!([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole] "Administrator")) { Start-Process powershell.exe "-NoProfile -ExecutionPolicy Bypass -File `"$PSCommandPath`"" -Verb RunAs; exit }
#select current machine
$computer = Get-WmiObject Win32_ComputerSystem 
#unjoin current AD
$computer.UnjoinDomainOrWorkGroup("passhere", "username-here", 0) 
#rejoin AD
$computer.JoinDomainOrWorkGroup("domain-name", "passhere", "full-user", $null, 3) 
#Restart-Computer -Force
