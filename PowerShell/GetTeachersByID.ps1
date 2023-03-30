#Get all teacher license number of each teacher in CSV called TeacherList and export to CSV

import-module ActiveDirectory
#Add-PSSnapin Quest.ActiveRoles.ADManagement


$district = Read-Host "Enter district name exactly:"
$csv = Import-csv -path .\TeacherList.csv | foreach-object {
    $user = get-aduser -DontUseDefaultIncludedProperties -ObjectAttributes @{teacherLicenseID = $_.ID} -SearchRoot "ou=Staff,ou=$district,ou=districts,dc=k12,dc=nd,dc=us"
    $user | select samaccountname, teacherLicenseID
   } | export-csv $PSScriptRoot\TeachersListDone.csv -NoTypeInformation

