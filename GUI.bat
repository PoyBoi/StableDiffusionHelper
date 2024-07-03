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

echo %time% Launching GUI...
call ext_GUI.bat

@echo off

:: test test