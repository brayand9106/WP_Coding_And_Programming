import os
import subprocess
import sys

'''Shortcut file to run entire application'''

# Get the current working directory (assumed to be the root of the repo)
project_dir = os.path.dirname(os.path.abspath(__file__))


#requirements_file = os.path.join(project_dir, "Requirements.bat")
run_script = os.path.join(project_dir, "run.py")
main_script = os.path.join(project_dir, "client", "main.py")
client_dir = os.path.join(project_dir, "client")


# Run the Flask application
subprocess.Popen([sys.executable, run_script])

# Run the main application
subprocess.Popen([sys.executable, main_script], cwd=client_dir)