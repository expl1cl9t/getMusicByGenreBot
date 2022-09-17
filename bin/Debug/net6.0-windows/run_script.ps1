$Trigger= New-ScheduledTaskTrigger -At 8:00pm -Daily
$User= "NT AUTHORITY\SYSTEM"
$Action= New-ScheduledTaskAction -Execute "PowerShell.exe" -Argument "python $PSScriptRoot main.py"
Register-ScheduledTask -TaskName "StartupScript_PS" -Trigger $Trigger -User $User -Action $Action -RunLevel Highest –Force