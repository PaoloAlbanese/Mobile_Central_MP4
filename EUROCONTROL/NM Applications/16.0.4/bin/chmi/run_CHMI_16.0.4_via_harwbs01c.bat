rem run_CHMI_16.0.4_via_harwbs01c.bat

@ECHO OFF
rem define internet_proxy:port_number
rem SET CHMI_PROXYHOST_24_0=


SET CHMI_MAIN_ACCESSURL=/DOMAIN240/gateway/_facade
SET CHMI_SIMUL_ACCESSURL=/DOMAINSIM240/gateway/_facade
SET CHMI_PROXYHOST_SSLCERT_CHECK=no
SET CHMI_ACTIVATE_DOWNLOADER=yes
SET CHMI_CACHE=chmi_appdata/MAPS/V11
SET CHMI_CORBA=
SET CHMI_GROUP_HOME=
SET CHMI_PROPERTIES=chmi.properties
IF EXIST sita_proxy.bat call sita_proxy.bat
SET CHMI_USER_HOME=
SET CHMI_OLDAUTH=false
SET CHMI_WEBSERVER=harwbs01.nm.eurocontrol.int

rem SET CHMI
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