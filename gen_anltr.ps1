Remove-Item target_antlr -Recurse

$folder = New-Item -Path .\target_antlr -ItemType Directory

C:\Users\moi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\Scripts\antlr4.exe `
    ".\StellarisLexer.g4" ".\StellarisParser.g4" -Dlanguage=Python3 -o target_antlr #-listener #-atn

#C:\"Program Files"\Graphviz\bin\dot.exe `
#    .\target_antlr\StellarisParser.bool_expr_any_val.dot -Tsvg -o .\test.svg