start "" "file:///C:/Users/Arshit/Google Drive/git/AI-Photo-Editor/frontend/index.html"
cls
python server.py
rem taskkill /F /IM chrome.exe
taskkill /FI "WINDOWTITLE eq AI Photo Editor*"