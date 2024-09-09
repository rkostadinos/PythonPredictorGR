#!/bin/sh

python --version || echo "Python not found. Install Python first."

pip install -r ./requirements.txt >/dev/null 2>&1

cd ./App/GUI
./GUI.py

pause
