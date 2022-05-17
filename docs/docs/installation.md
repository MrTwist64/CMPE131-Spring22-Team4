# Installation

## Requirements
The website requires the most recent version of [python](https://www.python.org/downloads/) as well as [pip](https://pip.pypa.io/en/stable/installing/).

After installing python and pip, run the commands listed under required libraries to install any necessary packages.

## Required Libraries
```angular2html
pip install flask 
pip install flask-wtf flask-sqlalchemy flask-login flask-session flask-bootstrap
pip install email_validator
pip install virtualenv
```

## Running the Website
The website should now work when the `run.py` file is executed. \
After running the file, click the URL printed by the console or by visit `127.0.0.1:5000` in a web browser.

## VirtualEnv

Included in the repository is a virtualenv environment which already includes all of the required packages.
- To start the environment, run the `Scripts/activate.bat` file.
- To end the environment, run the `Scripts/deactivate.bat` file.
