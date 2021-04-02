# template_python_project

This is a sample application for test deployment on pypi.
You can use it as reference but **i don't recommend its use**.

## Install

For install this app you need to have **setuptools** in your python environment.

```sh
# We assume that pip is install and is connected to python 3
pip install --editable .
# OR
pip install template-python-project

# For install the project with development tool
pip install --editable ".[development]"
```

## Use

For further information use *--help* option.

```sh
template-python-project --compute-type MUL --first 1 --second 2
```
## Linter

This application use the linter **pylint**.
**pylint** is installed with development tools.

```sh
# For execute tests we assume that the development dependencies are install
pylint template_python_project
```

## Test

This applciation use the test framework **pytest**.
**pytest** is installed with development tools.

```sh
# For execute tests we assume that the development dependencies are install
pytest ./test
```

## Deploy

You need to install **twine** for deploy on pypi.
You need to install **wheel** to have a valid binary for deployment.

```sh
# We assume that pip is install and is connected to python 3
pip install twine
pip install wheel
```

After the installation of the dependencies.
You need to use **setup.py** for build the project.
You need to use the **twine** command for the deployment.

```sh
# We assume that pip is install and is connected to python 3
# We assume that python is install and is a symbolic link to python 3
python setup.py bdist_wheel
twine upload dist/*
```
