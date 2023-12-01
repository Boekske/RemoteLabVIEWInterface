# how to wrap the code in to a python package

In order to make the scripted code easily distributable. We will wrap the code into a proper python package.
This way we can easily include the python code as part of the labVIEW application.

[poetry](https://python-poetry.org/) is used for dependency, package and build management

## pre-condition

Install Poetry. Should be fast, can be done as part of a CI task.

for windows:

```powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
```

## manual steps

- The current directory is the root of the repo. Let's call that directory *\<cdroot\>*.
- Prepare:
  
  deployment folder : *\<cdroot>*/bin
  - `cd <cdroot>`
  - `RMDIR /S /Q "bin" 2>nul`
  - `mkdir bin`

- Build, test, deploy the as a whl file:
  - `cd <cdroot>/src/Scripts/Python/`
  - `poetry install`
  - ~~`poetry run pytest`~~   can be discard as there are no unit test implemented.
  - `poetry build`
  - `copy .\dist\*.whl ..\..\..\bin` copy whl file to the deployment folder
  - `mkdir ..\..\..\bin\examples`  create examples folder
  - `copy .\example_*.py ..\..\..\bin\examples` copy whl file to the deployment folder

- build documentation:
  - `cd <cdroot>/src/Scripts/Python/doc`
  - update the API doc
    `sphinx-apidoc -o source\ ..\  "..\example_* -f`  (ensure the examples are filtered out, as they will hang the API doc generation)
  - `.\make html`
  - `mkdir ..\..\..\..\bin\doc` 
  - `copy .\build\html\* ..\..\..\..\bin\doc`

## automation

this process is automated via the build.bat file

1. create virtual env
2. create python package
   1. build package
   2. copy package to the artifacts folder
   3. copy examples scripts to artifacts folder
3. generate doc
   1. generate API doc
   2. build html
   3. copy to the artifacts folder

## usage

The Python "wheel" (whl) file should be used to install Python packages using tools like pip. The process generally involves these steps:

```cmd
pip install file_name.whl
```

After this the end-user van easily import end use the module.

```python
import module_name
```
