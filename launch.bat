@echo off

python --version || winget install -e --id Python.Python.3.12 --scope machine

pip install -r .\requirements.txt >nul 2>&1

cd .\App\GUI || cd App\GUI
.\GUI.py || GUI.py

pause
