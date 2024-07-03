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

echo.

:: Launch _Helper.ipynb with a specific kernel (e.g., "python3")
echo %time% Launching GUI...
python gradio_GUI.py

:: start "" "_Helper.ipynb"

@echo off

:: test test