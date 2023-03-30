#######################################################
## My version of Waking up machines
## Daniel Castillo
## V2.5
##
##
#######################################################

<#
.SUM
Wake on LAN for multiple machines using wolcmd.exe

.PARAMETER Machines
csv with machine names to wake up

.PARAMETER Interface
The VLAN of machines to wake

.PARAMETER Subnet
The subnet mask of said machines

.EXAMPLE
WakeUp-Machines machines.csv 192.168.1.1 255.255.255.0

.EXAMPLE
WakeUp-Machines c:\utilities\machines.csv 192.168.1.1 255.255.255.0

.NOTES
wolcmd,exe must be avaialble on same location as this script

proper format of CSV file.

Name,MacAddress,IpAddress
pcname1,A0DEF169BE02,192.168.1.13
Host6,AC1708486CA2,192.168.1.17
pc2,FDDEF15D5401,192.168.1.19

#>


param(
    [Parameter(Mandatory=$true, HelpMessage="csv file path")]
    [string] $Machines, 
    [Parameter(Mandatory=$true, HelpMessage="VLAN IP address")]
    [string] $Interface,
    [Parameter(Mandatory=$true, HelpMessage="Subnet mask this time.")]
    [string] $Subnet
    )


## Constant variables
$WolCmd=".\wolcmd.exe"
$TimeOut = 30
$Replies = 10

clear;Write-Host

## check for wolcmd.exe
try
{
    Get-ChildItem $WolCmd | Out-Null
}
Catch
{
    Write-Host "$WolCmd file not here!";Write-Host
    exit
}

## Read CSV file with machine names
try
{
    $File=Import-Csv $Machines
}
Catch
{
    Write-Host "$Machines file not here!";Write-Host
    exit
}


$i=1
foreach($Machine in $File)
{
    $Name=$Machine.Name
    $MAC=$Machine.MacAddress
    $IP=$Machine.IpAddress

    ## Send magic packet to each
    Write-Progress -ID 1 -Activity "Waking up machine $Name" -PercentComplete ($i*100/$file.Count)
    Invoke-Expression "$WolCmd $MAC $Interface $Subnet" | Out-Null

    $j=1
    ## Go into loop until machine replies to echo function
    $Ping = New-Object System.Net.NetworkInformation.Ping
    do
    {
        $Echo = $Ping.Send($IP)
        Write-Progress -ID 2 -ParentID 1 -Activity "Waiting for $Name to respond" -PercentComplete ($j*100/$TimeOut)
        sleep 1
        
        if ($j -eq $TimeOut)
        {
            Write-Host "Time out, aborting.";Write-Host
            exit
        }
        $j++
    }
    while ($Echo.Status.ToString() -ne "Success" )

    ## Machine is alive, keep sending for $Replies
    for ($k = 1; $k -le $Replies; $k++) 
    { 
       Write-Progress -ID 2 -ParentID 1 -Activity "Waiting for $Name to respond to echo" -PercentComplete (100) 
       Write-Progress -Id 3 -ParentId 2 -Activity "Receiving echo reply"  -PercentComplete ($k*100/$Replies)
       sleep 1
    }
    $i++
    Write-Progress -Id 3 -Completed $true
    $Ping=$null
}


