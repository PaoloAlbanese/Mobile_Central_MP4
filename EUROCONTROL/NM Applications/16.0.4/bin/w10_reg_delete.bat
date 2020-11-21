@echo off

set CURRENT_PATH=%~dp0
set JRE_PATH=%CURRENT_PATH%..\jre\bin
set JAVA_EXE_FILE=%JRE_PATH%\java.exe

CALL :RESOLVE %JAVA_EXE_FILE% REG_FILE

REG DELETE "HKCU\Software\Microsoft\Windows NT\CurrentVersion\AppCompatFlags\Layers" /V "%REG_FILE%" /F

GOTO :EOF
:RESOLVE
SET %2=%~f1
GOTO :EOF

