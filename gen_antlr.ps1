param(
    [boolean]$ShowPath=$false
)

$path = ".\src\antlrlib"

if (Test-Path $path) {
    Remove-Item $path -Recurse
}

$folder = New-Item -Path $path -ItemType Directory

if (Test-Path $folder) {}

$python_path = Invoke-Expression "python3 .\utils\python_path.py"

if ($ShowPath) {
    Write-Output $python_path
}

$antlr_path = Join-Path -Path $python_path -ChildPath antlr4.exe

Start-Process -FilePath $antlr_path -NoNewWindow `
    -ArgumentList ".\grammar\StellarisLexer.g4 .\grammar\StellarisParser.g4 -Dlanguage=Python3 -o $path -visitor"
