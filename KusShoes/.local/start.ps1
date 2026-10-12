$ErrorActionPreference = 'Stop'
$repoRoot = Split-Path -Parent $PSScriptRoot
$runtimeAlias = 'C:\Users\Asus\kusshoes-local-runtime'
$env:PYTHONUTF8 = '1'
$pythonPath = Join-Path $repoRoot 'BE\.venv\Scripts\python.exe'
$pgCtl = Join-Path $runtimeAlias 'tools\postgres\node_modules\@embedded-postgres\windows-x64\native\bin\pg_ctl.exe'
$logDir = Join-Path $PSScriptRoot 'logs'

function Test-LocalPort([int]$Port) {
    return [bool](Get-NetTCPConnection -State Listen -LocalPort $Port -ErrorAction SilentlyContinue)
}

function Start-LocalProcess($Name, $Executable, $Arguments, $Directory) {
    $process = Start-Process -FilePath $Executable -ArgumentList $Arguments -WorkingDirectory $Directory -WindowStyle Hidden -PassThru -RedirectStandardOutput (Join-Path $logDir "$Name.log") -RedirectStandardError (Join-Path $logDir "$Name.error.log")
    [pscustomobject]@{ Name = $Name; Id = $process.Id }
}

function Wait-LocalPort([int]$Port) {
    # Startup allowance for development processes; does not change app timeouts.
    for ($attempt = 0; $attempt -lt 30; $attempt++) {
        if (Test-LocalPort $Port) { return }
        Start-Sleep -Seconds 1
    }
    throw "Local service did not start on port $Port. Check .local/logs."
}

if (-not (Test-LocalPort 55432)) {
    & $pgCtl -D "$runtimeAlias\pgdata" -l "$runtimeAlias\logs\postgres.log" -o '-h 127.0.0.1 -p 55432' start
    if ($LASTEXITCODE -ne 0) { throw 'PostgreSQL startup failed.' }
}
if (-not (Test-LocalPort 56379)) {
    Start-LocalProcess 'redis' "$runtimeAlias\tools\redis\redis-server.exe" @('--bind','127.0.0.1','--port','56379','--dir',"$runtimeAlias\tools\redis") $repoRoot
}
if (-not (Test-LocalPort 9000)) {
    Start-LocalProcess 'storage' $pythonPath @('-m','moto.server','-H','127.0.0.1','-p','9000') "$repoRoot\BE"
    Wait-LocalPort 9000
    & $pythonPath "$PSScriptRoot\init-storage.py"
    if ($LASTEXITCODE -ne 0) { throw 'Local S3 bucket initialization failed.' }
}
if (-not (Test-LocalPort 8000)) {
    Start-LocalProcess 'api' $pythonPath @('-m','uvicorn','app.main:app','--host','127.0.0.1','--port','8000') "$repoRoot\BE"
}
if (-not (Test-LocalPort 5173)) {
    $viteEntry = '"' + (Join-Path $repoRoot 'FE\node_modules\vite\bin\vite.js') + '"'
    Start-LocalProcess 'vite' (Get-Command node.exe).Source @($viteEntry,'--config','../.local/vite-demo.config.ts') "$repoRoot\FE"
}
$worker = Get-CimInstance Win32_Process | Where-Object { $_.CommandLine -like "*$repoRoot*" -and $_.CommandLine -like '*app.workers.celery_app*worker*' }
if (-not $worker) {
    Start-LocalProcess 'worker' $pythonPath @('-m','celery','-A','app.workers.celery_app','worker','--pool=solo','--concurrency=1','--loglevel=info','-Q','high,normal,low') "$repoRoot\BE"
}
Wait-LocalPort 8000
Wait-LocalPort 5173
Invoke-RestMethod 'http://localhost:8000/health/ready' | ConvertTo-Json -Depth 4
Write-Host 'Website: http://localhost:5173 | API docs: http://localhost:8000/docs'
