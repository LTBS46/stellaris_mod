param([String]$prog="test1.stell")

$python_path = python .\python_path.py

$antlr_path = Join-Path -Path $python_path -ChildPath antlr4-parse.exe

$antlr_arg = ".\StellarisLexer.g4 .\StellarisParser.g4 mod -gui -tokens -trace"

Get-Content $prog | Invoke-Expression "$antlr_path $antlr_arg"
 