title BasicX Compile
@echo off
cls
color 0a

echo *******************************************************************************
echo                           X-Lab (Shanghai) Co., Ltd.
echo                  Copyright 2018-2018 X-Lab All Rights Reserved.
echo *******************************************************************************

echo.
echo Start BasicX Compile ...
echo.

D:\Python36\python.exe setup_all.py build_ext --inplace

echo.
echo Compile BasicX Finish.
echo.

pause

:: ����·�����ļ������ֲ���������
