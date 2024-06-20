@echo off

git pull

start "" "_Helper.ipynb"

@echo off

@REM :: Install pip (if not already installed)
@REM set python_ver=36
@REM python ./get-pip.py
@REM cd \
@REM cd \python%python_ver%\Scripts\
@REM pip install xlrd
@REM pip install XlsxWriter
@REM :: Pause to keep the window open
@REM pause
@REM exit

@REM :: Create a requirements.txt file with the following content:
@REM :: xlrd
@REM :: XlsxWriter
@REM :: tkinter

@REM :: Install the modules from requirements.txt
@REM pip install -r requirements.txt