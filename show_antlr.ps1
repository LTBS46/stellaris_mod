param([String]$prog="test1.stell")
Get-Content $prog | `
 C:\Users\moi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\Scripts\antlr4-parse.exe `
 ".\StellarisLexer.g4" ".\StellarisParser.g4" mod -gui -tokens -trace
 