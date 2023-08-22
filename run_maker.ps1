param(
    [string]$Mod=".\tests\test1.stell",
    [boolean]$Echo=$false
)

$base = Invoke-Expression "python3 .\utils\base_name.py $Mod"

$path = Join-Path -Path .\mod -ChildPath $base

if ($Echo) {
    Write-Output $base
    Write-Output $path    
}

if (Test-Path $path) {
    Remove-Item $path -Recurse
}

$folder = New-Item -Path $path -ItemType Directory

if (Test-Path $folder) {}

Invoke-Expression "python mod_maker.py $path $Mod"
