@echo off
chcp 65001 >nul
cd /d "%~dp0"
echo === Menyiapkan lingkungan Python ===
where python >nul 2>nul
if errorlevel 1 goto tanpa_python
if not exist ".venv\Scripts\python.exe" (
    python -m venv .venv
)
call ".venv\Scripts\activate.bat"
python -m pip install --quiet --upgrade pip
python -m pip install --quiet -r requirements.txt
if errorlevel 1 goto gagal_pasang
echo === Membuka notebook di browser ===
cd Eksperimen
python -m notebook Tugas_MST_Lokal.ipynb
goto selesai
:tanpa_python
echo Python belum terpasang atau belum ada di PATH. Pasang dari python.org, centang "Add Python to PATH", lalu coba lagi.
goto selesai
:gagal_pasang
echo Gagal memasang pustaka. Periksa koneksi internet lalu coba lagi.
:selesai
pause
