# Python Flask Web App Template
This template is built using Flask Web App Framework. It contains a sample Sqlite Database enabled with a Login Feature and an admin panel.

## Instructions

### Install Python
As of Dec 2023, install Python Version 3.10.11

Windows
https://www.python.org/downloads/windows/

Mac
https://www.python.org/downloads/macos/

### Install MS Visual Studio Code
Microsoft's Visual Studio is a recommended IDE to use.


### Designate a folder and get MS Visual Studio Code ready

Designate a folder on your computer that will contain the virtual environment and your project files.

Lets assume the folder name is project on your Desktop.

- Open the folder project from MS Visual Studio Code
- From the menu, click View and select Extensions and enable the Python Extension
- From the menu, click View and select Command Palette.
- From the command Palette, search for Python Interpreter. From the provided list, select the Python version you have installed.
- From the menu, click Terminal and select View Terminal.
- From the Terminal, check your python version using the below command

  ` python --version `

### Install virtualenv package
Virtualenv is a recommended third-party python package for creating and managing a virtual environment

For Windows, run a cmd terminal rather than a Powershell terminal.
For mac, either a bash or zsh is fine.

- From the Terminal, run the below command
` pip install virtualenv `

### Setup the Virtual Environment
From the Terminal, run the below command
` virtualenv venv --python=python3.10`

venv is the name assigned for the virtual environment. You are free to choose the name you like.
The `--python` argument is optional. It can be used if you have multiple Python versions installed on your computer.

Once completed, you will see a folder by the name venv within your project directory.

#### Key Libraries
* flask
* flask-sqlaclhemy
* flask-login
* flask-admin
* flask-wtforms
* wtforms
