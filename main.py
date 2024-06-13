import os


def take_input_as_string(
    message: str = "Enter your input: ", error_message: str = "Invalid input"
):
    """
    Taking input as string, the string might not be empty
    """

    # Running a while loop
    while True:

        # Taking the user input
        userinput = input(message)

        # If the userinput is None (length of the userinput is zero)
        if userinput is None:

            # Prining the error message
            print(error_message)

        # If the userinput is not empty
        else:

            # Return the userinputs
            return userinput


# Getting the name of the project
project_name = take_input_as_string("Project Name: ")

# Getting the location of the project directory

# Running a while loop
while True:

    # Taking the user input for location
    location = input("Project Directory: ")

    # Checking if the path exists
    if not os.path.exists(location):

        # Printing the error message
        print("Directory does not exist")

    # Otherwise
    else:

        # Break the loop
        break

# Creating the project directory
os.mkdir(os.path.join(location, project_name))

# Creating the static directory
os.mkdir(os.path.join(location, project_name, "static"))

# Writing the JS file
with open(
    os.path.join(location, project_name, "static", "login.js"), "w"
) as login_file:
    login_file.writelines(
        """
var username = document.getElementById("username");
var password = document.getElementById("password");
var warning = document.getElementById("warning_text");
var registered_form = document.getElementById("form");
var submit_button = document.getElementById("submit");

// A function to hide the warning text
function hideWarning() {
    warning.style.display = "none";
}

// A function to show the warning text
function showWarning() {
    warning.style.display = "block";
}

// Checking the details in the form
function checkDetails() {

    // If the username is not empty
    if (username.value.toString().trim() === "") {

        // Updating the innerHTML
        warning.innerHTML = "Username cannot be empty";

        // Returning false
        return false;
    }

    // If the password is not empty
    else if (password.value.toString().trim() === "") {

        // Updating the innerHTML
        warning.innerText = "Password cannot be empty";

        // Returning false
        return false;
    }

    // Otherwise return true
    else {
        return true;
    }
}

// Adding an event listener to the document for the DOMContentLoaded to hide the warning
document.addEventListener("DOMContentLoaded", hideWarning)

// Adding an event listener to the submit button for checking all the fields and submitting the form
submit_button.addEventListener("click", function () {

    // Defining a bool to check the details
    var details_correct = checkDetails();

    // If the function returns false
    if (!details_correct) {

        // Hide the warning
        showWarning();
    }

    // Else
    else {

        // Hide the warning
        hideWarning();

        // Submitting the form
        registered_form.submit();
    }
})
        """
    )

# Writing the register.js file
with open(
    os.path.join(location, project_name, "static", "register.js"), "w"
) as register_file:
    register_file.writelines(
        """
// Getting the required elements
var username = document.getElementById("username");
var first_name = document.getElementById("first_name");
var last_name = document.getElementById("last_name");
var password = document.getElementById("password");
var submit_button = document.getElementById("submit");
var register_form = document.getElementById("register_form");
var warning = document.getElementById("warning_text");

// A function to hide the warning text
function hideWarning() {
    warning.style.display = "none";
}

// A function to show the warning text
function showWarning() {
    warning.style.display = "block";
}

// A function to check whether all the details in a form are entered correctly
function checkDetails() {
    if (username.value.toString().trim() === "") {
        warning.innerHTML = "Username cannot be empty";
        return false;
    } else if (first_name.value.toString().trim() === "") {
        warning.innerText = "First name cannot be empty";
        return false;
    } else if (last_name.value.toString().trim() === "") {
        warning.innerText = "Last name cannot be empty";
        return false;
    } else if (password.value.toString().trim() === "") {
        warning.innerText = "Password cannot be empty";
        return false;
    } else if (last_name.value.toString().trim() === first_name.value.toString().trim()) {
        warning.innerText = "First name cannot be same as last name";
        return false;
    } else if (password.value.toString().length < 8) {
        warning.innerText = "Password should be minimum 8 characters long";
        return false;
    } else {
        return true;
    }
}

// Adding an event listener to the document on DOM event loaded for hiding the warning element
document.addEventListener("DOMContentLoaded", hideWarning);

// Adding an event listener to the submit button on click event for checking all the fields and submitting the form
submit_button.addEventListener("click", function () {

    // Defining a bool to check the details
    var details_correct = checkDetails();


    // If the function returns false
    if (!details_correct) {

        // Shows the warning
        showWarning();
    }

    // If the function returned true
    else {

        // Hiding the warning element
        hideWarning();

        // Submitting the form
        register_form.submit();
    }
});
        """
    )

# Writing the style.css file
with open(
    os.path.join(location, project_name, "static", "style.css"), "w"
) as style_file:
    style_file.writelines(
        """
@import url('https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap');
* {
    font-family: "Poppins", -apple-system, BlinkMacSystemFont;
}

.center {
    text-align: center;
}

h2 {
    font-size: 27px;
}

header {
    padding-top: 10px;
    padding-bottom: 10px;
    background-color: whitesmoke;
}

h3.choose-title {
    font-size: 18px;
}

h4.choose-title{
    font-size: 16px;
    font-weight: normal;
}

.container {
    margin-top: 1.5%;
}
.custom p{
    font-family: "SF Mono", 'Courier New', Courier, monospace;
    font-size: 15px;
    padding: 0;
    margin: 0;
    
}
.custom{
    max-width: 80vw;
    max-height: 70vh;
    overflow-y: hidden;
    overflow-x: hidden;
    text-overflow: clip;
    word-break: keep-all;
    background-color: #eee; 
    padding: 10px;
    border-radius: 10px;
}
.custom:hover{
    overflow-y: scroll;
    overflow-x: scroll;
}
.custom p{
    white-space: nowrap;
}
span{
    margin-top: 10px;
    width: fit-content;
    height: fit-content;
    padding: 10px;
}
span:hover{
    cursor: pointer;
    background-color: #ccc;
    border-radius: 50%;
}
span.material-symbols-outlined#done{
    zoom: 2;
    align-items: center;
    justify-content: center;
    background-color: lightgreen;
    border-radius: 50%;
}
li{
    font-size: 20px;
}
li a{
    text-decoration: none;
    color: black;
}
li a:hover{
    text-decoration: underline;
    color: black;
}

#submit{
    font-size: 19px;
}
.choose-title.field::after{
    content: "*";
    color: red;
}
        """
    )

# Creating the template directory
os.mkdir(os.path.join(location, project_name, "templates"))

# Writing the login.html file
with open(
    os.path.join(location, project_name, "templates", "login.html"), "w"
) as layout_file:
    layout_file.writelines(
        """
{% extends "layout.html" %}
{% block title %}
<title>Login</title>
{% endblock %}
{% block body %}
<form class="container mb-3" style="width: 40%;" id="form" action="/login_be" method="POST">
    {% with messages = get_flashed_messages() %}
    {% if messages %}
        <ul class=flashes>
        {% for message in messages %}
            <div class="alert alert-primary center">{{ message }}</div>
        {% endfor %}
        </ul>
    {% endif %}
    {% endwith %}
    <h3 class="text-center">Login</h3>
    <div class="mb-3">
        <label for="username" class="form-label">
            <h3 class="choose-title field">Username</h3>
        </label>
        <input type="text" class="form-control" placeholder="Username"
        name="username" id="username" autofocus autocapitalize="off" autocomplete="off">
    </div>
    <div class="mb-3">
        <label for="password" class="form-label">
            <h3 class="choose-title field">Password</h3>
        </label>
        <input type="password" class="form-control" placeholder="Password"
        name="password" id="password" autofocus autocapitalize="off" autocomplete="off">
    </div>
    <div id="warning" class="mb-3 center">
        <h5 id="warning_text" class="alert alert-danger">Danger Text here</h5>
    </div>
</form>
<div class="mb-3 center">
    <button class="btn btn-primary" id="submit" name="submit_button">Login</button>
</div>
{% endblock %}
{% block script %}
<script src="/static/login.js"></script>
{% endblock %}
        """
    )

# Writing the layout.html
with open(
    os.path.join(location, project_name, "templates", "layout.html"), "w"
) as login_template:
    login_template.writelines(
        """
<!DOCTYPE html>
<html lang="en" >
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="/static/style.css">
        <link
        href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css"
        rel="stylesheet"
        integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65"
        crossorigin="anonymous">
        <script
        src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-kenU1KFdBIe4zVF0s0G1M5b4hcpxyD9F7jL+jjXkk+Q2h455rYXK/7HAuoJl+0I4"
        crossorigin="anonymous"></script>
        <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200" />
        {% block head %}{% endblock %}
        {% block title %} {% endblock %}
    </head>
    <body id="html">
        <nav class="navbar bg-light">
            <div class="container-fluid">
                <a class="navbar-brand">Title here</a>
                {% if session.get("username") %}
                <ul class="nav justify-content-center">
                    <li class="nav-item">
                        <a class="nav-link" style="color: black; text-decoration: none;">Welcome, {{ session["username"] }}</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link active" aria-current="page" href="/login">Logout</a>
                    </li>
                </ul>
                {% else %}
                <div class="d-flex" role="search">
                    <a class="btn btn btn-outline-primary" href="/login">Login</a>
                    <a class="ms-3 btn btn btn-outline-primary" href="/register">Register</a>
                </div>
                {% endif %}
            </div>
        </nav>
        <section class="main">
            {% block body %} {% endblock %}
        </section>
    </body>
    {% block script %}
    {% endblock %}
</html>
        """
    )

# Writing the register.html file
with open(
    os.path.join(location, project_name, "templates", "register.html"), "w"
) as register_template:
    register_template.writelines(
        """
{% extends "layout.html" %}
{% block title %}
<title>Register</title>
{% endblock %}

{% block body %}
<form action="/register_be" method="POST" class="container mb-3" style="width: 40%;" id="register_form">
    <h3 class="text-center">Register</h3>
    <div class="mb-3">
        <label for="username" class="form-label">
            <h3 class="choose-title field">Username</h3>
        </label>
        <input type="text" class="form-control" placeholder="Username" name="username" id="username" autofocus autocapitalize="off" autocomplete="off">
    </div>
    <div class="mb-3">
        <label for="first_name" class="form-label">
            <h3 class="choose-title field">First Name</h3>
        </label>
        <input type="text" class="form-control" placeholder="First Name" name="first_name" id="first_name" autofocus autocapitalize="off" autocomplete="off">
    </div>
    <div class="mb-3">
        <label for="last_name" class="form-label">
            <h3 class="choose-title field">Last Name</h3>
        </label>
        <input type="text" class="form-control" placeholder="Last Name" name="last_name" id="last_name" autofocus autocapitalize="off" autocomplete="off">
    </div>
    <div class="mb-3">
        <label for="password" class="form-label">
            <h3 class="choose-title field">Password</h3>
        </label>
        <input type="password" class="form-control" placeholder="Password" name="password" id="password" autofocus autocapitalize="off" autocomplete="off">
    </div>
    <h5 id="warning_text" class="alert alert-danger center"></h5>
</form>
<div class="mb-3 center">
    <button class="btn btn-primary" id="submit" name="submit_button" type="button">Register</button>
</div>
{% endblock %}

{% block script %}
<script src="/static/register.js"></script>
{% endblock %}

        """
    )

# Writing the index.html file
with open(
    os.path.join(location, project_name, "templates", "index.html"), "w"
) as index_file:
    index_file.writelines(
        """
        """
    )

# Writing the apology.html file
with open(
    os.path.join(location, project_name, "templates", "apology.html"), "w"
) as apology_file:
    apology_file.writelines(
        """
{% extends "layout.html" %}
{% block title %}
    <title>Apology</title>
{% endblock %}

{% block body %}
        <div class="position-absolute top-50 start-50 translate-middle">
            <img alt="{{ top }}" class="border img-fluid" src="https://api.memegen.link/images/custom/{{ top | urlencode }}/{{ bottom | urlencode }}.jpg?background=https://i.imgur.com/CsCgN7Ll.png&width=400" title="{{ top }}">
        </div>
{% endblock %}
        """
    )


# Writing the home.html file
with open(
    os.path.join(location, project_name, "templates", "home.html"), "w"
) as home_file:
    home_file.writelines(
        """
{% extends "layout.html" %}
{% block title %}
    <title>Home</title>
{% endblock %}

{% block body %}
{% endblock %}
"""
    )

# Writing the .gitignore file
with open(os.path.join(location, project_name, ".gitignore"), "w") as gitignore:
    gitignore.writelines(
        """
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# PyInstaller
#  Usually these files are written by a python script from a template
#  before PyInstaller builds the exe, so as to inject date/other infos into it.
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.py,cover
.hypothesis/
.pytest_cache/
cover/

# Translations
*.mo
*.pot

# Django stuff:
*.log
local_settings.py
db.sqlite3
db.sqlite3-journal

# Flask stuff:
instance/
.webassets-cache

# Scrapy stuff:
.scrapy

# Sphinx documentation
docs/_build/

# PyBuilder
.pybuilder/
target/

# Jupyter Notebook
.ipynb_checkpoints

# IPython
profile_default/
ipython_config.py

# pyenv
#   For a library or package, you might want to ignore these files since the code is
#   intended to run in multiple environments; otherwise, check them in:
# .python-version

# pipenv
#   According to pypa/pipenv#598, it is recommended to include Pipfile.lock in version control.
#   However, in case of collaboration, if having platform-specific dependencies or dependencies
#   having no cross-platform support, pipenv may install dependencies that don't work, or not
#   install all needed dependencies.
#Pipfile.lock

# poetry
#   Similar to Pipfile.lock, it is generally recommended to include poetry.lock in version control.
#   This is especially recommended for binary packages to ensure reproducibility, and is more
#   commonly ignored for libraries.
#   https://python-poetry.org/docs/basic-usage/#commit-your-poetrylock-file-to-version-control
#poetry.lock

# pdm
#   Similar to Pipfile.lock, it is generally recommended to include pdm.lock in version control.
#pdm.lock
#   pdm stores project-wide configurations in .pdm.toml, but it is recommended to not include it
#   in version control.
#   https://pdm.fming.dev/latest/usage/project/#working-with-version-control
.pdm.toml
.pdm-python
.pdm-build/

# PEP 582; used by e.g. github.com/David-OConnor/pyflow and github.com/pdm-project/pdm
__pypackages__/

# Celery stuff
celerybeat-schedule
celerybeat.pid

# SageMath parsed files
*.sage.py

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# Spyder project settings
.spyderproject
.spyproject

# Rope project settings
.ropeproject

# mkdocs documentation
/site

# mypy
.mypy_cache/
.dmypy.json
dmypy.json

# Pyre type checker
.pyre/

# pytype static type analyzer
.pytype/

# Cython debug symbols
cython_debug/

# PyCharm
#  JetBrains specific template is maintained in a separate JetBrains.gitignore that can
#  be found at https://github.com/github/gitignore/blob/main/Global/JetBrains.gitignore
#  and can be added to the global gitignore or merged into this file.  For a more nuclear
#  option (not recommended) you can uncomment the following to ignore the entire idea folder.
#.idea/
        """
    )

# Writing the app.py file
with open(os.path.join(location, project_name, "app.py"), "w") as app_file:
    app_file.writelines(
        """
# Importing the required libraries and objects
from flask import Flask, render_template, request, redirect, session, flash
from flask_session import Session
import os
from helper import apology
from cs50 import SQL
from werkzeug.security import generate_password_hash, check_password_hash

# Setting up the flask application
app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


# Creating a SQL object for the database
db = SQL("sqlite:///database.db")


def create_and_init_db():
    \"""Creates and initializes the database.\"""

    # Checking if the database exists
    if not os.path.exists(os.path.join(os.getcwd(), "phonebook.db")):

        # Writing the database if it doesn't exist
        with open("phonebook.db", "w"):
            pass

    # Creating the SQL object
    db = SQL("sqlite:///database.db")

    # Executing SQL queries to create the tables
    db.execute(
        \"""
        CREATE TABLE IF NOT EXISTS "users" (
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
            username TEXT NOT NULL,
            hash TEXT NOT NULL,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL
        );
        \"""
    )


# Ensures that the cache is removeed
@app.after_request
def after_request(response):
    \"""Ensure responses aren't cached\"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# Defining a route for the main page
@app.route("/")

# Defining a function for the main
def main_route():

    # Returning the redirect to login page
    return redirect("/login")


# Setting up the routes
@app.route("/register")

# Defining the register route's function
def register_route():

    # Clearing the session
    session.clear()

    # Returning the `index.html` template
    return render_template("register.html")


# Setting up the login route
@app.route("/login")

# Defining the login function
def login_route():

    # Clearing the session
    session.clear()

    # Returning the `login.html` template
    return render_template("login.html")


# Defining a route for the backend for the registration
@app.route("/register_be", methods=["POST"])

# Defining a function for the backend for the registration
def register_be():

    # Clearing the session
    session.clear()

    # Getting the data from the form
    username = request.form.get("username")
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    password = request.form.get("password")

    # Checking the database if the user exists
    does_user_exist = db.execute(
        \"""
            SELECT * FROM users WHERE username = ?
        \""",
        username,
    )

    # If the length of the query returns 0
    if len(does_user_exist) != 0:

        # Returns an apology
        return apology("Username already exists")

    # If the length of the query is not zero, add the user to the database
    else:
        db.execute(
            \"""
                INSERT INTO users (username, hash, first_name, last_name)
                VALUES (?, ?, ?, ?)
            \""",
            username,
            generate_password_hash(password),
            first_name,
            last_name,
        )

        # Flashing the message
        flash("Registered Successfully! ")

        # Redirecting the user
        return redirect("/login")


# Defining a route for the backend for the login
@app.route("/login_be", methods=["POST"])

# Defining a function for the backend for the login
def login_be():

    # Clearing the session
    session.clear()

    # Getting the username and the password
    username = request.form.get("username")
    password = request.form.get("password")

    # Checking if the user exists
    does_user_exist = db.execute(
        \"""
            SELECT * FROM users WHERE username = ?
        \""",
        username,
    )

    # If the length of the query returns 0
    if len(does_user_exist) == 0:

        # Returns an apology
        return apology("Username doesn't exist")

    # If the length of the query is not zero
    else:

        # Checking if the password is correct
        if check_password_hash(does_user_exist[0]["hash"], password):

            # Setting the session
            session["user_id"] = does_user_exist[0]["id"]
            session["username"] = does_user_exist[0]["username"]
            session.modified = True

            # Redirecting the user
            return redirect("/home")

        # If the password is not correct
        else:

            # Returns an apology
            return apology("Incorrect Password")


# Defining a route for the home page
@app.route("/home")

# Defining the function for the home
def home_route():

    # Rendering the template
    return render_template(
        "home.html", user_id=session["user_id"], username=session["username"]
    )


# If the file is used as a main file
if __name__ == "__main__":

    # Creating an initializing database
    create_and_init_db()

    # Running the app in debug mode
    app.run(debug=True)

        """
    )

with open(os.path.join(location, project_name, "helper.py"), "w") as helper_file:
    helper_file.writelines(
        """
from flask import render_template
def apology(message, code=400):
    \"""Render message as an apology to user.\"""

    def escape(s):
        \"""
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        \"""
        for old, new in [
            ("-", "--"),
            (" ", "-"),
            ("_", "__"),
            ("?", "~q"),
            ("%", "~p"),
            ("#", "~h"),
            ("/", "~s"),
            ('"', "''"),
        ]:
            s = s.replace(old, new)
        return s

    return (
        render_template("apology.html", top=code, bottom=escape(message)),
        code,
    )

        """
    )


with open(os.path.join(location, project_name, "requirements.txt"), "w") as req_file:
    req_file.writelines(
        """
flask
flask_session
cs50
werkzeug
        """
    )
