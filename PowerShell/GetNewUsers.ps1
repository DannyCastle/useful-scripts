#Get AD User(s) created in X days

$When = ((Get-Date).AddDays(-5)).Date
Get-ADUser -Filter {whenCreated -ge $When} -Properties whenCreated |
Select-Object GivenName, Surname, Name, WhenCreated, UserPrincipalName, DistinguishedName |
export-csv $PSScriptRoot\NewUsers.csv -NoTypeInformation -Delimiter "|"