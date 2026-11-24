@echo off
cd /d "%~dp0"
call leafdoc\Scripts\activate.bat
streamlit run app.py
pause