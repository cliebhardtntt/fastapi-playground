Write-Output "Req1 start: $(Get-Date)"
Invoke-WebRequest http://localhost:8000 -UseBasicParsing
Write-Output "Req1 end: $(Get-Date)"

$jobs = 1..1 | ForEach-Object {
  Start-Job -ScriptBlock { Invoke-WebRequest http://localhost:8000/largefib -UseBasicParsing }
}

Start-Sleep 1 # Make sure that the other requests have started

Write-Output "Req2 start: $(Get-Date)"
Invoke-WebRequest http://localhost:8000 -UseBasicParsing
Write-Output "Req2 end: $(Get-Date)"

$jobs | Wait-Job | Get-Job | % { Receive-Job $_.Id; Remove-Job $_.Id } | out-null

Write-Output "Req3 start: $(Get-Date)"
Invoke-WebRequest http://localhost:8000 -UseBasicParsing
Write-Output "Req3 end: $(Get-Date)"