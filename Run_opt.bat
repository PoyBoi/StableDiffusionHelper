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

:: Pull from Git
:: echo %time% Pulling from git...
:: git pull

:: Update requirements
echo %time% Updating requirements...
pip install -r requirements.txt > nul 2>&1

for /l %%i in (1,1,10) do (
    <nul set /p "=."
    ping localhost -n 2 > nul
)
echo.

:: Launch _Helper.ipynb with a specific kernel (e.g., "python3")
echo %time% Launching .ipynb...
echo .ipynb launched at http://localhost:8888/notebooks/_Helper.ipynb
call jupyter notebook _Helper.ipynb --NotebookApp.kernel_name=python3 > nul 2>&1



:: Deactivate venv
echo %time% Deactivating venv...
deactivate

echo %time% Loading complete.

:: Pause to keep the window open
echo %time% Pausing execution...
pause