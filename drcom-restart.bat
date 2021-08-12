@echo off

set "user=2111******"
set "pwd=********"
rem set pwd=%pwd:)=^^)%


for /f "tokens=4" %%a in ('route print^|findstr 0.0.0.0.*0.0.0.0') do (
 set IP=%%a
)

call:detect

:detect
ping -n 1 -w 1 zhihu.com > nul
if %errorlevel% leq 0 (
   echo network ok.
   choice /t 4 /d y /n > nul
   exit
) else (
   echo network bad.
   echo curl -G -d c=Portal -d a=login -d login_method=1 --data-urlencode user_account=,0,%user% --data-urlencode user_password=%pwd% -d wlan_user_ip=%IP% http://192.168.6.1:801/eportal/ 
   curl -G -d c=Portal -d a=login -d login_method=1 --data-urlencode user_account=,0,%user% --data-urlencode user_password=%pwd% -d wlan_user_ip=%IP% http://192.168.6.1:801/eportal/   
   rem taskkill /f /t /im DrMain.exe
   choice /t 1 /d y /n > nul
   rem taskkill /f /t /im DrClient.exe
   rem choice /t 5 /d y /n > nul
   rem start C:\Drcom\DrUpdateClient\DrMain.exe
   rem choice /t 300 /d y /n > nul
)
goto detect 