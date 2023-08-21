Remove-Item target_antlr -Recurse

$folder = New-Item -Path .\target_antlr -ItemType Directory

$python_path = python .\python_path.py

$antlr_path = Join-Path -Path $python_path -ChildPath antlr4.exe

$antlr_arg = ".\StellarisLexer.g4 .\StellarisParser.g4 -Dlanguage=Python3 -o target_antlr"

$antlr_cmd = Write-Output "$antlr_path $antlr_arg"

Invoke-Expression $antlr_cmd

#C:\"Program Files"\Graphviz\bin\dot.exe `
#    .\target_antlr\StellarisParser.bool_expr_any_val.dot -Tsvg -o .\test.svg