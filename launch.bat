#!/bin/sh

python --version || (winget install -e --id Python.Python.3.12 --scope machine || pacman -Sy python || apt-get install python || dnf install python || yum install python)

(pip install -r ./requirements.txt || pip install -r .\requirements.txt) > nul 2>&1

cd ./App/GUI || cd .\App\GUI
./GUI.py || .\GUI.py
