#Deletes a mailbox and restores it to another. Restore makes a copy, original mailbox left intact. Destination  mailbox must be active.

$deletedUser = Read-Host "Enter deleted user's account name"
$targetUser = Read-Host "Enter target user's full email"

    $context = Get-ConnectionInformation

    if (!$context)
    {
        $globalAdmin = Read-Host "Enter the username of your Global Admin account"
        #$globalAdmin = 'daniel.castillo1@k12.nd.us'
        $credentials = Get-Credential -Credential $globalAdmin
        Connect-ExchangeOnline -Credential $credentials
    }
    else
    {
        Write-Host "Already Signed in"
    }

$deletedMailbox = Get-Mailbox -SoftDeletedMailbox |  where alias -eq $deletedUser | select-object Alias,ExchangeGUID

Write-Host "Here are the DELETED (SOURCE) user details. Please verify
"
Write-Host "Source Account Name: $($deletedMailbox.Alias)"
Write-Host "Source Mailbox GUID: $($deletedMailbox.ExchangeGUID)"

$targetMailbox = Get-Mailbox -Identity $targetUser | Select-Object Alias,ExchangeGUID

Write-Host "

Here are the TARGET (DESTINATION) user details. Please verify:
" 
Write-Host "Destination Account name: $($targetMailbox.Alias)"
Write-Host "Destination mailbox GUID: $($targetMailbox.ExchangeGUID)"

write-host "

Continue? (Y/N) 

"
$response = read-host
if ( $response -ne "Y" ) { exit }

Write-Host "continuing"

New-MailboxRestoreRequest -SourceMailbox $deletedMailbox.ExchangeGUID -TargetMailbox $targetMailbox.ExchangeGUID -allowlegacydnmismatch -name $targetMailbox.Alias

Write-Host "
Mailbox transfer started. Please allow up to one hour depending on mailbox size.
Status updated every 20 seconds

"

$status = Get-MailboxRestoreRequestStatistics -identity "$($targetUser)\$($targetMailbox.Alias)"

While ($($status.StatusDetail).ToString() -ne "Completed")
{
    Start-Sleep -Seconds 20
    $status = Get-MailboxRestoreRequestStatistics -identity "$($targetUser)\$($targetMailbox.Alias)"
    Write-Host "
    Status: $($status.StatusDetail.ToString())
    Percent done: $($status.PercentComplete)
    "
}
Write-Host "
Completed!

Ignore this below, I don't know why it happens
"