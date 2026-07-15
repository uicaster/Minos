@echo off
cd /d "C:\Users\Administrator\Documents\Project\minos"
powershell -Command "Start-Process pythonw -ArgumentList 'main.py' -WorkingDirectory '%cd%' -WindowStyle Hidden -Verb RunAs"
