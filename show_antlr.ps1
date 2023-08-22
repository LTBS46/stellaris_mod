param(
    [string]$File="tests\test1.stell",
    [string]$Mode="gui"
)

if ($Mode -notin ("gui", "trace", "tokens")) {
    Write-Error "Mode :'$Mode' is not known"
    exit
}

$python_path = Invoke-Expression "python3 .\utils\python_path.py"

$antlr_path = Join-Path -Path $python_path -ChildPath antlr4-parse.exe

Start-Process -FilePath $antlr_path -NoNewWindow -RedirectStandardInput $File `
    -ArgumentList ".\grammar\StellarisLexer.g4", ".\grammar\StellarisParser.g4", "mod", "-$Mode"
