param(
    [String]$mod="test1.stell"
)

$base = python .\base_name.py $mod

$path = Join-Path -Path .\mod -ChildPath $base

if (Test-Path $path) {
    Remove-Item $path -Recurse
}

$folder = New-Item -Path $path -ItemType Directory

python mod_maker.py $folder $mod