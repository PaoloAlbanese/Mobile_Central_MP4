@ECHO OFF

date /T >> ..\log\fixPrefs.log
time /T >> ..\log\fixPrefs.log
echo running CHMI preference conversion script version 2 >> ..\log\fixPrefs.log


REM Input/Output parameters validation
REM If less than 4 arguments then set defaults
IF "%4%"=="" GOTO defaultArgs
SET PREFERENCE_SRC=%1
SET PREFERENCE_DEST=%2
SET WORKSPACE_SRC=%3
SET WORKSPACE_DEST=%4
GOTO startConverter

:defaultArgs
ECHO WARNING: Using default Preference and Workspace file locations!
ECHO.
REM PUT default location of preferences file here
SET PREFERENCE_SRC="..\etc\preferences\chmi.preferences"
SET PREFERENCE_DEST="..\etc\preferences\chmi.preferences"
SET WORKSPACE_SRC="..\etc\preferences\chmi.workspaces"
SET WORKSPACE_DEST="..\etc\preferences\chmi.workspaces"


rem For AO

  SET PREFERENCE_SRC="c:\Program Files (x86)\Eurocontrol\NM Applications\15.5.4\etc\preferences\chmi.preferences"
  SET PREFERENCE_DEST="..\etc\preferences\chmi.preferences"
  SET WORKSPACE_SRC="c:\Program Files (x86)\Eurocontrol\NM Applications\15.5.4\etc\preferences\chmi.workspaces"
  SET WORKSPACE_DEST="..\etc\preferences\chmi.workspaces"





:startConverter
IF EXIST %PREFERENCE_DEST% (
	ECHO Backup destination preferences file
	copy %PREFERENCE_DEST% %PREFERENCE_DEST%.bak
)
IF EXIST %WORKSPACE_DEST% (
	ECHO Backup destination workspaces file
	copy %WORKSPACE_DEST% %WORKSPACE_DEST%.bak
)

ECHO Launching the converter application
rem ..\jre\bin\java -classpath ..\patch\CHMI.ATFCM.controllers.jar;..\patch\CHMI.FRAMEWORK.common.jar;..\patch\CHMI.COMMON.controllers.jar;..\patch\CHMI.CHMI_CONFIG.chmi.jar;..\jar\CHMI.ATFCM.controllers.jar;..\jar\CHMI.FRAMEWORK.common.jar;..\jar\CHMI.COMMON.controllers.jar;..\jar\CHMI.CHMI_CONFIG.chmi.jar eurocontrol.cfmu.chmi.WorkspaceAndPreferenceConverter %PREFERENCE_SRC% %PREFERENCE_DEST% %WORKSPACE_SRC% %WORKSPACE_DEST% %5 %6 %7 2> fixPrefs.log
rem ..\jre\bin\java -classpath ..\patch\CHMI.ATFCM.controllers.jar;..\patch\CHMI.FRAMEWORK.common.jar;..\patch\CHMI.FRAMEWORK.controllers.jar;..\patch\CHMI.COMMON.controllers.jar;..\patch\CHMI.CHMI_CONFIG.chmi.jar;..\jar\CHMI.ATFCM.controllers.jar;..\jar\CHMI.FRAMEWORK.common.jar;..\jar\CHMI.COMMON.controllers.jar;..\jar\CHMI.CHMI_CONFIG.chmi.jar eurocontrol.cfmu.chmi.WorkspaceAndPreferenceConverter %PREFERENCE_SRC% %PREFERENCE_DEST% %WORKSPACE_SRC% %WORKSPACE_DEST% %5 %6 %7 2>> fixPrefs.log
    ..\jre\bin\java -classpath ..\patch\CHMI.ATFCM.controllers.jar;..\patch\CHMI.FRAMEWORK.common.jar;..\patch\CHMI.FRAMEWORK.controllers.jar;..\patch\CHMI.COMMON.controllers.jar;..\patch\CHMI.CHMI_CONFIG.chmi.jar;..\jar\CHMI.ATFCM.controllers.jar;..\jar\CHMI.FRAMEWORK.common.jar;..\jar\CHMI.FRAMEWORK.controllers.jar;..\jar\CHMI.COMMON.controllers.jar;..\jar\CHMI.CHMI_CONFIG.chmi.jar eurocontrol.cfmu.chmi.WorkspaceAndPreferenceConverter %PREFERENCE_SRC% %PREFERENCE_DEST% %WORKSPACE_SRC% %WORKSPACE_DEST% %5 %6 %7 2> fixPrefs.log
date /T >> ..\log\fixPrefs.log
time /T >> ..\log\fixPrefs.log
echo stopping CHMI preference conversion script version 2 >> ..\log\fixPrefs.log
ECHO.
pause