Remove-Item mod -Recurse

$folder = New-Item -Path .\mod -ItemType Directory

python3.10 mod_maker.py .\mod .\test1.stell