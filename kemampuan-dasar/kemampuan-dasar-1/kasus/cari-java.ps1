param(
#[string]$ComputerName
[Parameter(Mandatory=$true)][string]$Directory
)


Get-Childitem -Path $Directory -Include *.java -File -Recurse -ErrorAction SilentlyContinue