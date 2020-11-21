@echo off
echo.
echo run_CHMI_16.0.4_via_www_testX_nm_eu_int.bat
echo.


SET CHMI_MAIN_ACCESSURL=/DOMAIN240/gateway/_facade
SET CHMI_SIMUL_ACCESSURL=/DOMAINSIM240/gateway/_facade
SET CHMI_ACTIVATE_DOWNLOADER=yes
SET CHMI_CACHE=chmi_appdata/MAPS/V11
SET CHMI_CORBA=
SET CHMI_GROUP_HOME=
SET CHMI_PROPERTIES=chmi.properties
SET CHMI_PROXYHOST_24_0=
SET CHMI_PROXYHOST_SSLCERT_CHECK=yes
SET CHMI_USER_HOME=..\..\etc\preferences
REM if not "%USERDOMAIN%"=="OPSCFMU" SET CHMI_USER_HOME=%USERPROFILE%
SET CHMI_OLDAUTH=false
SET CHMI_WEBSERVER=www.testx.nm.eurocontrol.int


cd ..

@REM CHECK FOR PATCH

@if NOT EXIST ..\new_patch goto run
@echo New patch found. Updating patch level ...

@if NOT EXIST ..\patch mkdir ..\patch 

@xcopy /E /V /R /K /Y  ..\new_patch\*.* ..\patch
@if errorlevel 5 goto XcopyWriteError
@if errorlevel 4 goto XcopyLowMemory
@if errorlevel 2 goto XcopyCtrlC
@if errorlevel 1 goto XcopyNoFiles
@if errorlevel 0 goto XcopySuccess

:XCopyWriteError
@echo Xcopy reported a disc write error.
@goto ErrorExit

:XCopyLowMemory
@echo Xcopy reported a low memory condition.
@goto ErrorExit

:XCopyCtrlC
@echo Xcopy aborted by user hitting Ctrl-C
@goto ErrorExit

:XcopyNoFiles
@echo Xcopy found no files to copy.
@goto XcopySuccess

:ErrorExit
@echo Xcopy returncode %errorlevel%
@pause
@exit 16

:XcopySuccess
@echo Patch successfully applied.
@echo Cleaning up ...
@rmdir /S /Q ..\new_patch

:run
_run.bat
