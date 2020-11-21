@ECHO OFF


date /T >> fixPrefs.log
time /T >> fixPrefs.log
echo running CHMI preference conversion script version 2 >> fixPrefs.log

set  CHMI_SRC=c:\atfcm15.5.4.1
set CHMI_DEST=c:\atfcm16.0.4.1

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
SET PREFERENCE_SRC="%CHMI_SRC%\etc\preferences\chmi.preferences"
SET PREFERENCE_DEST="%CHMI_DEST%\etc\preferences\chmi.preferences"
SET WORKSPACE_SRC="%CHMI_SRC%\etc\preferences\chmi.workspaces"
SET WORKSPACE_DEST="%CHMI_DEST%\etc\preferences\chmi.workspaces"


echo %PREFERENCE_SRC%
echo %PREFERENCE_DEST%

echo %WORKSPACE_SRC%
echo %WORKSPACE_DEST%


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

rem %CHMI_DEST%\jre\bin\java -classpath %CHMI_DEST%\patch\CHMI.ATFCM.controllers.jar;%CHMI_DEST%\patch\CHMI.FRAMEWORK.common.jar;%CHMI_DEST%\patch\CHMI.COMMON.controllers.jar;%CHMI_DEST%\patch\CHMI.CHMI_CONFIG.chmi.jar;%CHMI_DEST%\jar\CHMI.ATFCM.controllers.jar;%CHMI_DEST%\jar\CHMI.FRAMEWORK.common.jar;%CHMI_DEST%\jar\CHMI.COMMON.controllers.jar;%CHMI_DEST%\jar\CHMI.CHMI_CONFIG.chmi.jar eurocontrol.cfmu.chmi.WorkspaceAndPreferenceConverter %PREFERENCE_SRC% %PREFERENCE_DEST% %WORKSPACE_SRC% %WORKSPACE_DEST% %5 %6 %7 2> convert_Prefs.log 
rem -25/08/2017
rem          ..\jre\bin\java -classpath          ..\patch\CHMI.ATFCM.controllers.jar;         ..\patch\CHMI.FRAMEWORK.common.jar;         ..\patch\CHMI.FRAMEWORK.controllers.jar;         ..\patch\CHMI.COMMON.controllers.jar;         ..\patch\CHMI.CHMI_CONFIG.chmi.jar;         ..\jar\CHMI.ATFCM.controllers.jar;         ..\jar\CHMI.FRAMEWORK.common.jar;         ..\jar\CHMI.FRAMEWORK.controllers.jar;         ..\jar\CHMI.COMMON.controllers.jar;         ..\jar\CHMI.CHMI_CONFIG.chmi.jar eurocontrol.cfmu.chmi.WorkspaceAndPreferenceConverter %PREFERENCE_SRC% %PREFERENCE_DEST% %WORKSPACE_SRC% %WORKSPACE_DEST% %5 %6 %7 2> fixPrefs.log
rem     %CHMI_DEST%\jre\bin\java -classpath %CHMI_DEST%\patch\CHMI.ATFCM.controllers.jar;%CHMI_DEST%\patch\CHMI.FRAMEWORK.common.jar;%CHMI_DEST%\patch\CHMI.FRAMEWORK.controllers.jar;%CHMI_DEST%\patch\CHMI.COMMON.controllers.jar;%CHMI_DEST%\patch\CHMI.CHMI_CONFIG.chmi.jar;%CHMI_DEST%\jar\CHMI.ATFCM.controllers.jar;%CHMI_DEST%\jar\CHMI.FRAMEWORK.common.jar;%CHMI_DEST%\jar\CHMI.FRAMEWORK.controllers.jar;%CHMI_DEST%\jar\CHMI.COMMON.controllers.jar;%CHMI_DEST%\jar\CHMI.CHMI_CONFIG.chmi.jar eurocontrol.cfmu.chmi.WorkspaceAndPreferenceConverter %PREFERENCE_SRC% %PREFERENCE_DEST% %WORKSPACE_SRC% %WORKSPACE_DEST% %5 %6 %7 2> convert_Prefs.log 
    %CHMI_DEST%\jre\bin\java -classpath %CHMI_DEST%\patch\CHMI.ATFCM.controllers.jar;%CHMI_DEST%\patch\CHMI.FRAMEWORK.common.jar;%CHMI_DEST%\patch\CHMI.FRAMEWORK.controllers.jar;%CHMI_DEST%\patch\CHMI.COMMON.controllers.jar;%CHMI_DEST%\patch\CHMI.CHMI_CONFIG.chmi.jar;%CHMI_DEST%\jar\CHMI.ATFCM.controllers.jar;%CHMI_DEST%\jar\CHMI.FRAMEWORK.common.jar;%CHMI_DEST%\jar\CHMI.FRAMEWORK.controllers.jar;%CHMI_DEST%\jar\CHMI.COMMON.controllers.jar;%CHMI_DEST%\jar\CHMI.CHMI_CONFIG.chmi.jar;%CHMI_DEST%\jar\CUA.CORE.iem.cua.jar;%CHMI_DEST%\jar\CUA.CORE.em-framework.jar;%CHMI_DEST%\jar\CUA.COMMON.shared.jar eurocontrol.cfmu.chmi.WorkspaceAndPreferenceConverter %PREFERENCE_SRC% %PREFERENCE_DEST% %WORKSPACE_SRC% %WORKSPACE_DEST% %5 %6 %7 2> convert_Prefs.log 


date /T >> fixPrefs.log
time /T >> fixPrefs.log
echo running CHMI preference conversion script version 2 >> fixPrefs.log

ECHO.


call c:\atfcm16.0.4.1\common\runUploadPrefs16_0_4.bat