#Renames user's Account name

import-module ActiveDirectory

$userCurrent = Read-Host "Enter user's current account name"
$userDesired = Read-Host "Enter user's desired account name"
$domain = "@k12.nd.us"

#get-aduser $userCurrent
$aduser = get-aduser $userCurrent
$userDesiredEmail = $userDesired + $domain
set-aduser $aduser -userprincipalname $userDesiredEmail
$newDN = $userDesired
Rename-ADObject -identity $aduser -newname $newDN