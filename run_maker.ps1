param(
    [String]$mod="test1.stell"
)

$base = Invoke-Expression "python .\base_name.py $mod"

$path = Join-Path -Path .\mod -ChildPath $base

if (Test-Path $path) {
    Remove-Item $path -Recurse
}

$folder = New-Item -Path $path -ItemType Directory

Invoke-Expression "python mod_maker.py $folder $mod"