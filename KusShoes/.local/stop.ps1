$ErrorActionPreference = 'Stop'
$repoRoot = Split-Path -Parent $PSScriptRoot
$runtimeAlias = 'C:\Users\Asus\kusshoes-local-runtime'
$initialVite = Get-Content (Join-Path $PSScriptRoot 'initial-vite-owner.json') -Raw | ConvertFrom-Json

# Only stop this demo's processes, checking command lines before using process IDs.
foreach ($port in @(5173, 8000, 9000)) {
    $listener = Get-NetTCPConnection -State Listen -LocalPort $port -ErrorAction SilentlyContinue
    foreach ($connection in $listener) {
        $processInfo = Get-CimInstance Win32_Process -Filter "ProcessId=$($connection.OwningProcess)"
        $isInitialVite = $port -eq 5173 -and $processInfo.ProcessId -eq $initialVite.Id -and $processInfo.CreationDate.ToString('o') -eq $initialVite.CreationDate -and $processInfo.CommandLine -eq $initialVite.CommandLine
        $isDemoRuntime = $processInfo.CommandLine -like "*$repoRoot*" -or $processInfo.CommandLine -like "*$runtimeAlias*"
        if (($isDemoRuntime -and $processInfo.CommandLine -match 'vite|uvicorn|moto.server') -or $isInitialVite) {
            Stop-Process -Id $processInfo.ProcessId
        }
    }
}
Get-CimInstance Win32_Process | Where-Object { $_.Name -like 'python*' -and ($_.CommandLine -like "*$repoRoot*" -or $_.CommandLine -like "*$runtimeAlias*") -and $_.CommandLine -like '*app.workers.celery_app*worker*' } | ForEach-Object { Stop-Process -Id $_.ProcessId -ErrorAction SilentlyContinue }
$redisListener = Get-NetTCPConnection -State Listen -LocalPort 56379 -ErrorAction SilentlyContinue
if ($redisListener) {
    $redisProcess = Get-CimInstance Win32_Process -Filter "ProcessId=$($redisListener.OwningProcess)"
    if ($redisProcess.CommandLine -like '*redis-server*' -and $redisProcess.CommandLine -like '*kusshoes*') {
        & "$runtimeAlias\tools\redis\redis-cli.exe" -p 56379 shutdown nosave
    }
}
& "$runtimeAlias\tools\postgres\node_modules\@embedded-postgres\windows-x64\native\bin\pg_ctl.exe" -D "$runtimeAlias\pgdata" stop -m fast
Write-Host 'Local demo stopped. PostgreSQL data is retained; Moto storage is temporary.'
