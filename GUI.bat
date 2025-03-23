@echo off
setlocal

:: Check if venv_sdh exists
if not exist venv_sdh (
    echo %time% Creating venv...
    python -m venv venv_sdh
)

:: Deactive venv
call venv_sdh\Scripts\deactivate.bat

:: Activate venv
echo %time% Activating venv...
call venv_sdh\Scripts\activate

echo %time% Updating Repository
git add *
git stash
git pull > nul 2>&1

echo %time% Updating requirements...
pip install -r requirements.txt > nul 2>&1

echo Do you want to re-install remBG with GPU support ? Only do this if you want GPU support and/or have CPU issues when running remBG ( 1 for yes, 0 for no):
set /p remRedo=

if "%remRedo%"=="1" (
    echo Updating RemBG with GPU support...
    echo y | pip uninstall rembg
    echo y | pip uninstall onnxruntime
    pip install rembg[gpu]==2.0.57 onnxruntime-gpu==1.18.0
) else if "%remRedo%"=="0" (
    echo.
) else (
    echo Invalid choice.
)

echo.

echo %time% Launching GUI...

python gradio_GUI.py

@echo off

:: test test