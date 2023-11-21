<#
Use 
   Get-AudioDevice -List
to learn about available devices on your system.
Then set the two variables below with the start of their names.
#>
$device1 = "Razer Surround (7.1 Surround Sound)"
$programName1 = "rzappengine"
$programPath1 = "C:\Program Files\Razer\RzAppEngine\rzappengine.exe"

$device2 = "FxSound Speakers (FxSound Audio Enhancer)"
$programName2 = "FxSound"
$programPath2 = "C:\Program Files\FxSound LLC\FxSound\FxSound.exe"

$Audio = Get-AudioDevice -Playback
Write-Output "Audio device was $($Audio.Name)"

if ($Audio.Name -like "$device1") {
    (Get-AudioDevice -List | Where-Object Name -like "$device2" | Set-AudioDevice).Name
    Stop-Process -Name $programName1
    $workingDirectory = Split-Path -Path $programPath2 -Parent
    Start-Process -FilePath $programPath2 -WorkingDirectory $workingDirectory
    Write-Output "Audio device now set to $($(Get-AudioDevice -Playback).Name)"
} else {
    Stop-Process -Name $programName2
    $workingDirectory = Split-Path -Path $programPath1 -Parent
    Start-Process -FilePath $programPath1 -WorkingDirectory $workingDirectory
    (Get-AudioDevice -List | Where-Object Name -like "$device1" | Set-AudioDevice).Name
    Write-Output "Audio device now set to $($(Get-AudioDevice -Playback).Name)"
}
