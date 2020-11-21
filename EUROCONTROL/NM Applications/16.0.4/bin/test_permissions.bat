echo oFF
rem 2014/10/22 version 1
rem This script allows to validate the CHMI installation and the automatic download procedure

cd ..
rem dir

if  not EXIST .\log2\HelpLink.txt goto FILENOTEXIST

:FILEEXIST

echo **********************************************************************
echo A test file exist, probably from a previous test, it will be removed.
echo **********************************************************************
dir .\log2
pause
del .\log2\HelpLink.txt
rd log2

echo **********************************
echo removing file  .\log2\HelpLink.txt
echo **********************************
 dir
echo *******************************************************
echo Do you see log2 folder, if not, then the test can start
echo *******************************************************
pause
 
if  EXIST .\log2\HelpLink.txt goto FILEEXIST
pause
goto TEST1
:FILENOTEXIST
echo No test file to remove 

:TEST1
dir 
echo **********************************************************************
echo you should see      bin, etc, jar, jre, log and optional patch folders
echo ready to start the test
echo **********************************************************************
echo .
echo .

echo **********************************************************************
echo start writing 1 test file (HelpLink.txt)
echo **********************************************************************
xcopy /s /q .\etc\HelpLink.txt .\log2\*.*

echo ********************************************
echo   Trying to copy 1 test file (HelpLink.txt) 
echo ********************************************

dir .\log2
pause
cd .\log2 


IF NOT EXIST "HelpLink.txt"  GOTO  FAILED



:SUCCESS
echo **************************************************************
echo TEST OK 
echo TEST OK 
echo TEST OK 
echo folder log2 and file HelpLink.txt exist, thus the test is OK, 
echo CHMI Folder permission looks good
echo TEST OK 
echo TEST OK 
echo TEST OK 
echo **************************************************************
pause

goto DONE
 
:FAILED

echo **************************************************************
echo TEST NOT OK 
echo TEST NOT OK 
echo TEST NOT OK 
echo TEST file is missing after "copy operation"
echo Please check CHMI Folder permission with your PC administrator
echo TEST NOT OK 
echo TEST NOT OK 
echo TEST NOT OK 
echo **************************************************************

pause

:DONE
echo start cleanup

cd ..
if  EXIST .\log2\HelpLink.txt del  .\log2\HelpLink.txt
rd .\log2


echo script finished


pause
rem :EXII


