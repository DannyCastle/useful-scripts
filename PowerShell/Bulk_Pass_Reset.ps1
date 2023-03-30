#Resets password for all users in a CSV called "bulk_pass_reset.csv"

Import-Module ActiveDirectory

Import-Csv -path .\bulk_pass_reset.csv | ForEach-Object {
$samAccountName = $_."user"
 
#Un-comment the below line if your CSV file includes password for all users. Recommended.
$newPassword = ConvertTo-SecureString -AsPlainText $_."password"  -Force
 
# Reset user password.
Set-ADAccountPassword -Identity $samAccountName -NewPassword $newPassword -Reset
 
# Force user to reset password at next logon.
# Remove this line if not needed for you
Set-AdUser -Identity $samAccountName -ChangePasswordAtLogon $true
Write-Host " AD Password has been reset for: "$samAccountName
}