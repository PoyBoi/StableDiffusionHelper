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

echo %time% Updating/Checking
for /l %%i in (1,1,10) do (
    <nul set /p "=."
    ping localhost -n 2 > nul
)
echo.

call Run_opt.bat

:: start "" "_Helper.ipynb"

@echo off

:: test test