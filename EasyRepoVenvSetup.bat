@echo off
@REM NOTE: for creating a virtual environment, you need to have python installed and added to PATH
@REM NOTE: for working with github repositories you just need to provide link at ##LINK## and ##REPO_NAME## and uncomment the line
@REM NOTE: Only uncomment the line about requirements if you have a requirements.txt file

set "repo=##LINK##"
set "repo_dir=##REPO_NAME##"

@REM git clone %repo% %repo_dir%
@REM cd %repo_dir%
python.exe -m pip install -- upgrade pip
pip install virtualenv
python -m venv venv
call venv/Scripts/activate.bat
set "filename=isvenv.py"
echo ^>^>^> Creating Python file: %filename%
echo import os >> %filename%
echo running_in_virtualenv = "VIRTUAL_ENV" in os.environ >> %filename%
echo print(f'venv working: {running_in_virtualenv}') >> %filename%

echo ^>^>^> Python file created: %filename%
python isvenv.py > temp.txt
set /p venv_working=<temp.txt
del temp.txt
del isvenv.py

echo %venv_working%

if "%venv_working%"=="venv working: True" (
    @REM NOTE: only uncomment the line below if you have a requirements.txt file
    echo venv is working properly. Installing requirements...
    @REM pip install -r requirements.txt
) else (
    echo venv is not working properly. Not installing requirements.
)

pause