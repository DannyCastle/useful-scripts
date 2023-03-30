#Gets all users from District Tech Admin hide group in each district OU and exports to CSV

import-module ActiveDirectory
Get-ADGroup -Filter {name -like "*DistrictTechAdmin_hide"} -properties description |
     ForEach-Object{
     
     $county = $_.description.substring(0,2)
     $district = $_.description.substring(2,3)
          $hash=@{GroupName=$_.Name;Member='';edutechID='';County=$county;District=$district}
          
          $_ | Get-ADGroupMember -ea 0 -recurs |
               ForEach-Object{
                    $hash.edutechID = (get-aduser -filter {samaccountname -eq $_.samaccountname} -properties edutechid).edutechID
                    $hash.Member=$_.samaccountName
                    New-Object psObject -Property $hash
               }
          } | 
     sort groupname,member,edutechID,County,District | 
     export-csv $PSScriptRoot\DistrictTechs.csv -NoTypeInformation