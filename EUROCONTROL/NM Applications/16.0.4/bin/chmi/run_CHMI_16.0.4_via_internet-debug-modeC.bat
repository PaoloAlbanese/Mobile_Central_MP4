rem run_CHMI_16.0.4_via_internet-debug-modeC.bat
@echo my Computer Name is ** %computername% **
@ECHO OFF


rem version 3: added debug option

rem version 2:  added - deleteCFMU.Ciam folder if present
rem define internet_proxy:port_number
rem SET CHMI_PROXYHOST_24_0=


echo *************************************************************************
echo starting CHMI in debug mode (creation of extended debug logfiles)
echo CHMI log files are located in                   ..\16.0.4\log\
echo *************************************************************************

pause

dir "..\.."  /S >> ..\..\log\dir.log

if EXIST ..\..\patch\debug.txt goto LABEL2
rem if EXIST ..\..\patch\debug-activated.txt goto LABEL2

copy ..\..\etc\log4j-debug.properties ..\..\etc\log4j.properties
dir >> ..\..\patch\debug-activated.txt




:LABEL2
rem start section: deleteCFMU.Ciam folder
if not exist ..\..\etc\data\CFMU.Ciam\  goto LABEL1
if not exist ..\..\patch\donotdeleteCFMU.Ciam.txt  del ..\..\etc\data\CFMU.Ciam\*.* /q /s 
echo note to Ciam/FUA users to increase performance, CFMU.Ciam map cache files are deleted at each startup.
rem end section: deleteCFMU.Ciam folder
rem 


:LABEL1
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
SET CHMI_WEBSERVER=www.nm.eurocontrol.int


rem SET CHMI
cd ..
_run.bat
