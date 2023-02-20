Measure-Command { Invoke-WebRequest http://localhost:8000 -UseBasicParsing }

$jobs = 1..5 | ForEach-Object {
  Start-Job -ScriptBlock { Invoke-WebRequest http://localhost:8000/fib -UseBasicParsing }
}

Measure-Command { Invoke-WebRequest http://localhost:8000 -UseBasicParsing }

$jobs | Wait-Job | Get-Job | % { Receive-Job $_.Id; Remove-Job $_.Id } | out-null

Measure-Command { Invoke-WebRequest http://localhost:8000 -UseBasicParsing }
