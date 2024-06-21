@echo off
setlocal

:: Check if venv_sdh exists
if not exist venv_sdh (
    echo Creating venv...
    python -m venv venv_sdh
)

:: Deactive venv
call venv_sdh\Scripts\deactivate.bat


:: Activate venv
echo Activating venv...
call venv_sdh\Scripts\activate

:: Pull from Git
echo Pulling from git...
git pull

:: Update requirements
echo Updating requirements...
pip install -r requirements.txt

:: Launch _Helper.ipynb with a specific kernel (e.g., "python3")
echo Launching .ipynb...
call jupyter notebook _Helper.ipynb --NotebookApp.kernel_name=python3

:: Deactivate venv
deactivate

:: Add a loading bar (optional)
for /l %%A in (1,1,10) do (
    <nul set /p ".=."
    ping -n 1 127.0.0.1 > nul
)
echo.

:: Pause to keep the window open
pause
