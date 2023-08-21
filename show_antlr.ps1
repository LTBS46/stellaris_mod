param(
    [String]$prog="test1.stell",
    [String]$mode="gui"
)

$python_path = Invoke-Expression "python .\python_path.py"

$antlr_path = Join-Path -Path $python_path -ChildPath antlr4-parse.exe

Start-Process -FilePath $antlr_path -NoNewWindow -RedirectStandardInput $prog `
    -ArgumentList ".\StellarisLexer.g4", ".\StellarisParser.g4", "mod", "-$mode"