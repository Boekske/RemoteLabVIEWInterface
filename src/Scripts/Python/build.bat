@ECHO OFF

pushd %~dp0

REM Command file for building en deplyment of the Python package

set OUTPUTDIR= ..\..\..\bin
set UPDATE_APIDOC= false

if "%1" == "help" goto help
if "%1" == "doc" goto doc

echo. clean up output folder = %OUTPUTDIR%
RMDIR /S /Q %OUTPUTDIR% 2>nul
mkdir %OUTPUTDIR%

rem	create package

echo. === start build process ===
poetry install
poetry build -f wheel

echo. copy build artifacts to the output folder
copy .\dist\*.whl %OUTPUTDIR% 
mkdir %OUTPUTDIR%\examples  
copy .\example_*.py %OUTPUTDIR%\examples

:doc

rem create documentation
echo. === generate documentation ===
if %UPDATE_APIDOC% == true (
	echo. update api doc 
	poetry run sphinx-apidoc -o doc\source\ ..\  "..\example_*" -f
	) 

poetry run doc\make.bat html
echo. copy documentation to the output folder
mkdir %OUTPUTDIR%\doc
xcopy doc\build\html\* %OUTPUTDIR%\doc /s /e

echo. === Done ===

goto end

:help
echo. help can be found in the readme file

:end
popd