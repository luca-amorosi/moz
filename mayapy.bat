:: Batch file used to launch package testing with a mayapy.exe environment.

@ECHO OFF

set MAYA_APP_DIR=%~dp0\tests\temp\maya
set PYTHONPATH=%~dp0\.venv\Lib\site-packages;

set MAYA_LOCATION=C:\Program Files\Autodesk\Maya2024
"%MAYA_LOCATION%\bin\mayapy.exe" %*