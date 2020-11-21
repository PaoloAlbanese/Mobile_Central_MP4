@ECHO OFF

SET BASELINE=CHMI.CHMI_CONFIG.24.0.0.16.0.4.1
SET CHMICLIENT_OPTIONS=
SET CHMILOADER_OPTIONS=


REM
REM Look at the environment to discover what options to start the client with.
REM

REM Variables CHMI_MAIN_ACCESSURL, CHMI_SIMUL_ACCESSURL and CHMI_WEBSERVER
IF NOT "%CHMI_MAIN_ACCESSURL%"=="" GOTO gotChmiMainAccessurl
IF "%4"=="" GOTO noWeb
SET CHMI_MAIN_ACCESSURL=%4
:gotChmiMainAccessurl
IF NOT "%CHMI_WEBSERVER%"=="" GOTO gotChmiWebserver
IF "%3"=="" GOTO noWeb
SET CHMI_WEBSERVER=%3
:gotChmiWebserver
IF "%CHMI_MAIN_ACCESSURL%"=="null" GOTO noWeb
IF "%CHMI_WEBSERVER%"=="null" GOTO noWeb
SET CHMICLIENT_OPTIONS=%CHMICLIENT_OPTIONS% -Dchmi.webserver="%CHMI_WEBSERVER%"
SET CHMICLIENT_OPTIONS=%CHMICLIENT_OPTIONS% -Dchmi.mainaccessurl="%CHMI_MAIN_ACCESSURL%"

IF "%CHMI_SIMUL_ACCESSURL%"=="" GOTO noWeb
IF "%CHMI_SIMUL_ACCESSURL%"=="null" GOTO noWeb
SET CHMICLIENT_OPTIONS=%CHMICLIENT_OPTIONS% -Dchmi.simulaccessurl="%CHMI_SIMUL_ACCESSURL%"

:noWeb

IF "%CHMI_OLDAUTH%"=="null" GOTO webseal
SET CHMICLIENT_OPTIONS=%CHMICLIENT_OPTIONS% -Dchmi.oldauth="%CHMI_OLDAUTH%"
:webseal

REM Variable CHMI_ACTIVATE_DOWNLOADER
IF NOT "%CHMI_ACTIVATE_DOWNLOADER%"=="yes" GOTO downloaderNotActivated
SET CHMICLIENT_OPTIONS=%CHMICLIENT_OPTIONS% -Ddownloader
SET CHMILOADER_OPTIONS=%CHMILOADER_OPTIONS% -Dchmiloader
SET CHMILOADER_OPTIONS=%CHMILOADER_OPTIONS% -Dchmi.baseline=%BASELINE%
:downloaderNotActivated

REM Variable CHMI_CACHE
IF NOT "%CHMI_CACHE%"=="" GOTO gotChmiCache
SET CHMI_CACHE=%2
IF "%CHMI_CACHE%"=="" GOTO noChmiCache
:gotChmiCache
SET CHMICLIENT_OPTIONS=%CHMICLIENT_OPTIONS% -Dserver.cache.path.prefix="%CHMI_CACHE%"
:noChmiCache

REM Variable CHMI_GROUP_HOME
IF "%CHMI_GROUP_HOME%"=="" SET CHMI_GROUP_HOME=..
SET CHMICLIENT_OPTIONS=%CHMICLIENT_OPTIONS% -Dchmi.group.home=%CHMI_GROUP_HOME%

REM Variable CHMI_JVM_MX
IF NOT "%CHMI_JVM_MX%"=="" GOTO gotChmiJvmMx
SET CHMI_JVM_MX=1024m
:gotChmiJvmMx

REM Variable CHMI_PROPERTIES
IF NOT "%CHMI_PROPERTIES%"=="" GOTO gotChmiProperties
SET CHMI_PROPERTIES=%1
IF "%CHMI_PROPERTIES%"=="" GOTO noChmiProperties
:gotChmiProperties
SET CHMICLIENT_OPTIONS=%CHMICLIENT_OPTIONS% -Dchmi.properties="%CHMI_PROPERTIES%"
:noChmiProperties

REM Variable CHMI_PROXYHOST_24_0
IF NOT "%CHMI_PROXYHOST_24_0%"=="" GOTO gotChmiProxyhost
IF "%6"=="" GOTO noChmiProxyhost
SET CHMI_PROXYHOST_24_0=%6
:gotChmiProxyhost
IF "%CHMI_PROXYHOST_24_0%"=="null" GOTO noChmiProxyhost
SET CHMICLIENT_OPTIONS=%CHMICLIENT_OPTIONS% -Dchmi.proxyhost="%CHMI_PROXYHOST_24_0%"
:noChmiProxyhost

REM Variable CHMI_USER_HOME
IF "%CHMI_USER_HOME%"=="" GOTO noChmiUserHome
SET CHMICLIENT_OPTIONS=%CHMICLIENT_OPTIONS% -Dchmi.user.home="%CHMI_USER_HOME%"
:noChmiUserHome

REM Variable SSLCERT_CHECK
IF NOT "%CHMI_PROXYHOST_SSLCERT_CHECK%"=="yes" GOTO SSLEND
SET CHMICLIENT_OPTIONS=%CHMICLIENT_OPTIONS% -Dchmi.proxysslcheck=yes
:SSLEND

REM
REM Always do this.
REM

SET CHMICLIENT_OPTIONS=%CHMICLIENT_OPTIONS% -Dlog4j.configuration=log4j.properties
SET CHMICLIENT_OPTIONS=%CHMICLIENT_OPTIONS% -Dchmi.baseline=%BASELINE%
REM SET CHMICLIENT_OPTIONS=%CHMICLIENT_OPTIONS% -DkeepAliveSession=true
SET CHMICLIENT_OPTIONS=%CHMICLIENT_OPTIONS% -mx%CHMI_JVM_MX%

SET CHMI
echo .
echo . ...................................................
echo .
echo .
echo . CHMI Baseline: %BASELINE%
echo .
echo . ...................................................

SET CHMILOADER_OPTIONS=%CHMILOADER_OPTIONS% -Dlog4j.configuration=chmiloader.log4j.properties

..\jre\bin\java %CHMILOADER_OPTIONS% -jar ..\jar\chmiloader.jar
IF ERRORLEVEL 2 GOTO installerFailed

..\jre\bin\java -Dsun.java2d.noddraw=true -Xbootclasspath/p:../patch/CHMI.COMMON.bootpatch.jar:CHMI.COMMON.bootpatch.jar %CHMICLIENT_OPTIONS% -jar ..\jar\chmi.jar
EXIT

:installerFailed
ECHO Installer failed, cannot start CHMI
PAUSE
EXIT
