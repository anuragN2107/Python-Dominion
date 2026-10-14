# ===============================================================================================================================
#                                       PYTHON VIRTUAL ENVIRONMENTS MASTERCLASS
# ===============================================================================================================================


# ===============================================================================================================================
# PART 1: WHAT IS A VIRTUAL ENVIRONMENT?
# ===============================================================================================================================

# DEFINITION & OVERVIEW:
# - A Virtual Environment (`venv`) is an isolated, self-directory that houses a specific version of Python along with its own set of installed packages and libraries. 
# 
# WHY DO WE NEED IT?
# - Dependency Isolation: Project A might need Django version 3.2, while Project B needs Django version 4.2. Virtual environments keep them completely separate.
# - Global Pollution Prevention: Installing packages globally (`pip install`) can clutter your system Python, cause permission issues, and break system-level tools.
# - Reproducibility: It makes sharing your project and its exact dependencies with other developers seamless.


# ===============================================================================================================================
# PART 2: CREATING A VIRTUAL ENVIRONMENT
# ===============================================================================================================================

# INSTRUCTIONS & SYNTAX:
# - To create a virtual environment, open your terminal/command prompt, navigate to your project folder, and run the creation command.
# - Syntax: python -m venv <environment_name>
#   *(Note: Common names for the environment folder include `venv`, `.venv`, or `env`)*
# - Example: python -m venv venv
# - What happens behind the scenes? Python creates a folder named `venv` containing a copy of the Python interpreter, standard library, and a `site-packages` folder for future installations.


# ===============================================================================================================================
# PART 3: ACTIVATING THE VIRTUAL ENVIRONMENT
# ===============================================================================================================================

# ACTIVATION SYNTAX & EXAMPLES BY OPERATING SYSTEM:
# - Creating the environment isn't enough; you must activate it so your terminal directs all Python and `pip` commands into this isolated bubble.
# - Windows (Command Prompt / CMD): venv\Scripts\activate.bat
# - Windows (PowerShell): venv\Scripts\Activate.ps1
#   *(If you get a script execution policy error in PowerShell, run: `Set-ExecutionPolicy Unrestricted -Scope Process`)*
# - macOS / Linux (Bash / Zsh): source venv/bin/activate
# - How to know it worked? Once activated, your terminal prompt will typically change to show the environment name in parentheses, like this:
#   (venv) C:\Users\YourName\MyProject>


# ===============================================================================================================================
# PART 4: MANAGING PACKAGES (`pip`)
# ===============================================================================================================================

# MANAGING PACKAGES WITH PIP:
# - With your environment active, any package you install using `pip` goes exclusively into this folder.
# - Installing a package: pip install requests
# - Installing a specific version: pip install flask==2.2.1
# - Upgrading a package: pip install --upgrade requests
# - Uninstalling a package: pip uninstall requests


# ===============================================================================================================================
# PART 5: `pip freeze` AND REQUIREMENTS FILES
# ===============================================================================================================================

# DEPENDENCIES & REQUIREMENTS FILES:
# - When collaborating or deploying, you need to share a list of your project dependencies. `pip freeze` outputs all installed packages and their exact versions.
# - View all installed packages: pip freeze
# - 1. Saving dependencies into a file (Standard Root folder): pip freeze > requirements.txt
# - 2. Saving dependencies into a specific folder:
#   mkdir configs
#   pip freeze > configs/requirements.txt
# - Installing packages from a requirements file:
#   pip install -r requirements.txt
#   Or if it's inside a folder: pip install -r configs/requirements.txt


# ===============================================================================================================================
# PART 6: DEACTIVATING THE ENVIRONMENT
# ===============================================================================================================================

# DEACTIVATION:
# - When you are done working on your project and want to exit the isolated environment back to your system's global scope:
# - Syntax: deactivate


# ===============================================================================================================================
# PART 7: QUICK SUMMARY CHEATSHEET
# ===============================================================================================================================

# CHEATSHEET SUMMARY TABLE:
# Task                          | Command
# ------------------------------|---------------------------------------------
# Create venv                   | python -m venv venv
# Activate (Windows CMD)        | venv\Scripts\activate.bat
# Activate (Mac/Linux)          | source venv/bin/activate
# Install package               | pip install <package_name>
# Freeze dependencies (Root)    | pip freeze > requirements.txt
# Freeze dependencies (Folder)  | pip freeze > folder_name/requirements.txt
# Install from file             | pip install -r requirements.txt
# Deactivate                    | deactivate

