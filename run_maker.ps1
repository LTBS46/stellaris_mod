param(
    [String]$mod=".\tests\test1.stell",
    [Boolean]$echo=$false
)

$base = Invoke-Expression "python .\utils\base_name.py $mod"


$path = Join-Path -Path .\mod -ChildPath $base

if ($echo) {
    Write-Output $base
    Write-Output $path    
}

if (Test-Path $path) {
    Remove-Item $path -Recurse
}

$folder = New-Item -Path $path -ItemType Directory

if (Test-Path $folder) {}

Invoke-Expression "python mod_maker.py $path $mod"