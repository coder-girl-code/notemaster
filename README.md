# Flask-Based Web Application Template

This template leverages the Flask Web Application Framework, incorporating an example Sqlite Database with an integrated Login Feature and an admin panel.


## 1. Python Installation
Currently, as of December 2023, Python Version 3.10.11 is recommended.

### For Windows: 
Access the download link [here](https://www.python.org/downloads/windows/)

### For Mac: 
Access the download link [here](https://www.python.org/downloads/macos/)

## 2. Microsoft Visual Studio Code Installation
Microsoft's Visual Studio is the suggested Integrated Development Environment (IDE) for this project.

## 3. Git Installation
### Git for Windows: 
Download it from [here](https://git-scm.com/download/win)

### Git for Mac: 
You may need to install homebrew first, if it isn't already installed, which can be found [here](https://brew.sh/). Then, proceed with Git installation from [here](https://git-scm.com/download/mac)

## Setting Up Microsoft Visual Studio Code
- Create a specific folder on your local machine that will host the virtual environment and your project files. For this guide, let's assume the folder is named "project" located on your Desktop.
- Open this "project" folder in MS Visual Studio Code.
- Navigate to View in the menu, select Extensions and enable the Python Extension.
- Then, go to View in the menu and select Command Palette.
- In the Command Palette, search for Python Interpreter and select the Python version you have installed from the list provided.
- Navigate to Terminal in the menu and select View Terminal.
- In the Terminal, validate your installed Python version using the command: `python --version`

## 5. Installation of virtualenv Package
Virtualenv is a third-party Python package suggested for creating and managing virtual environments.

For Windows users, utilize a `cmd` terminal instead of a `powershell` terminal. For Mac users, either a `bash` or `zsh` terminal is acceptable.

In the Terminal, install `virtualenv` using the command: `pip install virtualenv`

## 6. Virtual Environment Setup
In the Terminal, create a virtual environment using the command: `virtualenv venv --python=python3.10`

The name `venv` has been assigned to the virtual environment, but feel free to choose a name that suits you. The `--python` argument is optional and can be used if you have multiple Python versions installed on your system.

Upon completion, a folder named `venv` should be present within your project directory.

## 7. Activation of the Virtual Environment
### For Windows: 
`venv\bin\activate`

### For Mac: 
`source venv/bin/activate`

Once activated, the terminal should display the virtual environment name `venv` within parentheses.

### 8. Repository Cloning
Clone the repository to your local project directory using the command: 
`git clone https://github.com/sunil-mnair/flask-login-admin-wtforms.git webapp`

Executing this command will create a new directory named `webapp` that will house all the repository files.

### 9. Python Packages Installation
In the newly created `webapp` directory, there is a file named `requirements.txt` that lists all the necessary packages for running this web application. In the active virtual environment, install these packages using the following command: `pip install -r requirements.txt`

### 10. Flask Web App Configuration
The primary file of your app is 'app.py'. The Flask App needs to be configured accordingly with the following commands.


### Configure the Flask Web App
To ensure Flask recognizes app.py as your primary application file, follow these steps:

Open your terminal or command prompt.

Navigate to your webapp directory using the following command:
`cd webapp`

Depending on your operating system, use the appropriate commands to set up Flask:

#### For Windows Users:
Enter the following commands to set your FLASK_APP environment variable to app.py and to set your FLASK_ENV environment variable to development:

`set FLASK_APP=app.py
set FLASK_ENV=development`

#### For Mac Users:
Use the following commands instead:

`export FLASK_APP=app.py
export FLASK_ENV=development`

After setting up Flask, you can launch your application.

## 11. Launching Your Application:

Ensure you are within the active virtual environment. Then, execute the following command to start your Flask application with reloading enabled:

`flask run --reload`

This command starts your application and the --reload option enables hot-reloading, meaning Flask will automatically detect changes in your files and restart the server when needed.

After running the above command, your application will launch in your web browser as localhost. You can access it by entering http://localhost:5000 in your browser's address bar.
