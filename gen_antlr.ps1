param(
    [Boolean]$show_path=$false
)

$path = ".\target_antlr"

if (Test-Path $path) {
    Remove-Item $path -Recurse
}

$folder = New-Item -Path .\target_antlr -ItemType Directory

if (Test-Path $folder) {}

$python_path = Invoke-Expression "python .\utils\python_path.py"

if ($show_path) {
    Write-Output $python_path
}

$antlr_path = Join-Path -Path $python_path -ChildPath antlr4.exe

Start-Process -FilePath $antlr_path -NoNewWindow `
    -ArgumentList ".\StellarisLexer.g4 .\StellarisParser.g4 -Dlanguage=Python3 -o $path"