@echo off
setlocal
echo ===================================================
echo KPSS Portal Baslatiliyor...
echo.

:: IP adresini otomatik bulma
for /f "tokens=2 delims=:" %%a in ('ipconfig ^| findstr /c:"IPv4 Address" /c:"IPv4 Adresi"') do set IP=%%a
if defined IP set IP=%IP: =%

echo Bilgisayarinizdan erismek icin: http://localhost:8000
if defined IP (
    echo Telefon/Tabletten erismek icin ayni internet agina (Wi-Fi)
    echo baglanin ve su adresi girin: http://%IP%:8000
) else (
    echo Baska cihazdan erismek icin ipconfig yazarak IP adresinizi ogrenin (Orn: http://192.168.1.x:8000).
)

echo.
echo Lutfen bu pencereyi kapatmayin!
echo ===================================================
start http://localhost:8000
python -m http.server 8000 --bind 0.0.0.0
