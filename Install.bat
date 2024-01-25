@echo off

echo -----------------------------------------------------------
echo. 
echo *      Welcome to InstaSwap Standalone Installation       *
echo. 
echo -----------------------------------------------------------
echo. 
echo. 

echo Checking for Python 3.10...
echo -----------------------------------------------------------
echo. 

py -3.10 --version >nul 2>&1
if %errorlevel%==0 (
    echo Python 3.10 is already installed.
) else (
    echo Python 3.10 is not installed. Downloading installer...
    curl https://www.python.org/ftp/python/3.10.10/python-3.10.10-amd64.exe -o python-3.10.10-amd64.exe

    echo Installing Python 3.10...
    python-3.10.10-amd64.exe /quiet InstallAllUsers=1 PrependPath=1

    echo Cleaning up installer...
    del python-3.10.10-amd64.exe
)

echo Creating virtual environment...
echo -----------------------------------------------------------
py -3.10 -m venv venv
echo. 
echo. 

echo Updating pip and wheel...
echo -----------------------------------------------------------
venv\Scripts\python.exe -m pip install --upgrade pip wheel
venv\Scripts\python.exe -m pip install tqdm
venv\Scripts\python.exe -m pip install packaging
venv\Scripts\python.exe -m pip install safetensors
venv\Scripts\python.exe -m pip install gradio
echo. 
echo. 

echo Installing Torch...
echo -----------------------------------------------------------
nvidia-smi >nul 2>&1
if %errorlevel%==0 (
    echo Installing PyTorch with GPU support...
venv\Scripts\pip.exe install torch torchvision --index-url https://download.pytorch.org/whl/cu118
) else (
    echo Installing PyTorch without GPU support...
    venv\Scripts\pip.exe install torch
)

echo Install the packages...
echo -----------------------------------------------------------
venv\Scripts\python.exe install.py
echo. 
echo. 
echo Launching app...
echo -----------------------------------------------------------
venv\Scripts\python.exe app.py
@pause
