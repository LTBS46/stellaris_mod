param([Boolean]$show_path=$true)

$path = ".\target_antlr"

if (Test-Path $path) {
    Remove-Item $path -Recurse
}

$folder = New-Item -Path .\target_antlr -ItemType Directory

if (Test-Path $folder) {}

$python_path = python .\python_path.py

if ($show_path) {
    Write-Output $python_path
}

$antlr_path = Join-Path -Path $python_path -ChildPath antlr4.exe

$antlr_cmd = "$antlr_path .\StellarisLexer.g4 .\StellarisParser.g4 -Dlanguage=Python3 -o $path"

Invoke-Expression $antlr_cmd