import-module ActiveDirectory
#Add-PSSnapin Quest.ActiveRoles.ADManagement
$district = 'Enderlin Area 24'
$path = "c:\users\aaron\desktop\Neva.csv"
$csv = Import-csv -path $path | foreach-object {
    $user = get-qaduser -DontUseDefaultIncludedProperties -ObjectAttributes @{studentID = $_.ID} -SearchRoot "ou=students,ou=$district,ou=districts,dc=k12,dc=nd,dc=us"
    $user | select @{n='User';e='samaccountname'}, studentID
   } | export-csv -NoTypeInformation "c:\users\aaron\desktop\Enderlin Aug 9.csv"