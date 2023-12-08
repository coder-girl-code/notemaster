# Python Flask Web App Template
This template is built using Flask Web App Framework. It contains a sample Sqlite Database enabled with a Login Feature and an admin panel.

## Instructions

### Install Python
As of Dec 2023, install Python Version 3.10.11

#### For Windows
https://www.python.org/downloads/windows/

#### For Mac
https://www.python.org/downloads/macos/

### Install MS Visual Studio Code
Microsoft's Visual Studio is a recommended IDE to use.

### Install Git
#### Git for Windows
https://git-scm.com/download/win

#### Git for Mac
You may require to install homebrew, if not already installed
https://brew.sh/

You may then proceed to install Git
https://git-scm.com/download/mac

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

### Activate the Virtual Environment
#### For Windows
`venv\bin\activate`

#### For Mac
`source venv/bin/activate`

Once activated, the terminal window will show the name of the virtual environment `venv` within round brackets.

### Clone the Repository
We can clone this repository to the local project directory using the below command
`git clone https://github.com/sunil-mnair/flask-login-admin-wtforms.git webapp`

Running the above command will create a new directory titled `webapp` which will contain all files from the repository.

### Install the required Python Packages

In the new `webapp' directory, the file `requirements.txt` contains all the packages we will need to get this web application running. In the active virtual environment, install the packages using the below command in the terminal.

`pip install -r requirements.txt'

### Configure the Flask Web App
The main file of your app is `app.py`. The Flask App needs to be configured to know this. Run below commands to get it done.

`cd webapp`

#### For Windows

`set FLASK_APP=app.py`

### For Mac

`export FLASK_APP=app.py`

### Run your App
In the active virtual environment, run the below command to run the app

`flask run --reload`
