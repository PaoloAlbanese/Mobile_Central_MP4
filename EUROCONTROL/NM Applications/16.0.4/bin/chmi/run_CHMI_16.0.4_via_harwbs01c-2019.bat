rem run_CHMI_16.0.4_via_harwbs01c-2019.bat

@ECHO OFF
rem define internet_proxy:port_number
rem SET CHMI_PROXYHOST_24_0=


SET CHMI_MAIN_ACCESSURL=/DOMAIN240/gateway/_facade
SET CHMI_SIMUL_ACCESSURL=/DOMAINSIM240/gateway/_facade
SET CHMI_PROXYHOST_SSLCERT_CHECK=no
SET CHMI_ACTIVATE_DOWNLOADER=no
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
_run.bat
