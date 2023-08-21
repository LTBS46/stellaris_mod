param(
    [String]$mod="test1.stell"
)

$path = Join-Path -Path .\mod -ChildPath $mod.BaseName

Remove-Item $path -Recurse

$folder = New-Item -Path $path -ItemType Directory

python mod_maker.py $folder $mod