rem run_CHMI_16.0.4_via_PREOPS_c_harwbs01.bat

@ECHO OFF
rem define internet_proxy:port_number
rem SET CHMI_PROXYHOST_24_0=


SET CHMI_MAIN_ACCESSURL=/DOMAIN240_PREOPS/gateway/_facade
SET CHMI_SIMUL_ACCESSURL=/DOMAINSIM240/gateway/_facade
SET CHMI_PROXYHOST_SSLCERT_CHECK=no
SET CHMI_ACTIVATE_DOWNLOADER=no
SET CHMI_CACHE=chmi_appdata/MAPS/V11
SET CHMI_CORBA=
SET CHMI_GROUP_HOME=
SET CHMI_PROPERTIES=chmi.properties
SET CHMI_USER_HOME=
SET CHMI_OLDAUTH=false
IF EXIST sita_proxy.bat call sita_proxy.bat
SET CHMI_WEBSERVER=harwbs01.nm.eurocontrol.int

rem SET CHMI
cd ..

set TESTA1=Y
@echo ***************************************************************************
@Echo *     ATTENTION                                                           *
@Echo *     You have selected the PREOPS     shortcut,                          *
@Echo *     You should only use this shortcut if you want to verify PREOPS data *
@Echo *     If you want to continue, type "Y" and press ENTER-key               * 
@echo *             or type "N" and press ENTER-key to stop ...                 *
@Echo ***************************************************************************

set /p TESTA2="Type  Y or N and press the ENTER-key

if "%TESTA1%"=="%TESTA2%"   goto run

:stop
@echo ********************************************
@Echo *     You have choosen not continue....    *
@Echo ********************************************
pause
@exit 16

:run
@Echo *********************************************
@Echo *  starting       CHMI Please wait ........ *
@Echo *********************************************



_run.bat
