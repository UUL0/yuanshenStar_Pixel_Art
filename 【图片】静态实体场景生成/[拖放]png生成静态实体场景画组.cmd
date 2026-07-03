@echo off
setlocal enabledelayedexpansion

mkdir "静态画场景组" 2>nul

REM png图片 输出文件名

for %%f in (%*) do (
    echo 正在处理: %%f
    py [静态画]实体场景组生成.py %%f 静态画场景组\%%~nf_静态画073.proto
)

pause