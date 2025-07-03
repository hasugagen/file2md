@echo off

echo Creating virtual environment...
python -m venv .venv

echo Activating virtual environment...
call .venv\Scripts\activate

echo Installing dependencies...
pip install -r requirements.txt

echo Building the executable...
rem pyinstaller --onefile --name file2md --distpath .\dist --workpath .\build src\main.py
pyinstaller file2md.spec

echo Deactivating virtual environment...
deactivate

echo.
echo Build complete! The executable is located in the 'dist' folder.

pause
