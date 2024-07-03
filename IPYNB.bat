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
:: Update requirements
echo %time% Updating requirements...
pip install -r requirements.txt > nul 2>&1

echo Do you want to re-install remBG with GPU support ? Only do this if you want GPU support and/or have CPU issues when running remBG ( 1 for yes, 0 for no):
set /p remRedo=

if "%remRedo%"=="1" (
    echo Updating RemBG with GPU support...
    echo y | pip uninstall rembg
    echo y | pip uninstall onnxruntime
    pip install rembg[gpu] onnxruntime-gpu
) else if "%remRedo%"=="0" (
    echo.
) else (
    echo Invalid choice.
)

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