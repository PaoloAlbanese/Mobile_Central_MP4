@ECHO OFF

ECHO Launching the converter application
..\jre\bin\java -cp ..\patch\CHMI.ATFCM.controllers.jar;..\patch\CHMI.FRAMEWORK.common.jar;..\patch\CHMI.FRAMEWORK.controllers.jar;..\patch\CHMI.COMMON.controllers.jar;..\patch\CHMI.CHMI_CONFIG.chmi.jar;..\jar\CHMI.ATFCM.controllers.jar;..\jar\CHMI.FRAMEWORK.common.jar;..\jar\CHMI.FRAMEWORK.controllers.jar;..\jar\CHMI.COMMON.controllers.jar;..\jar\CHMI.CHMI_CONFIG.chmi.jar eurocontrol.cfmu.chmi.WorkspaceAndPreferenceBatchConverter %1 %2 %3 %4 %5 %6 %7 %8 %9 2> fixPrefs.log
ECHO.
pause
