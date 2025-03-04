import os
import subprocess
import sys

# Get the current working directory (assumed to be the root of the repo)
project_dir = os.path.dirname(os.path.abspath(__file__))


requirements_file = os.path.join(project_dir, "Requirements.bat")
run_script = os.path.join(project_dir, "run.py")
main_script = os.path.join(project_dir, "client", "main.py")
client_dir = os.path.join(project_dir, "client")



# Run the batch file to install the requirements
try:
    subprocess.check_call([requirements_file], shell=True)
except subprocess.CalledProcessError as e:
    print(f"Failed to install requirements: {e}")
    print("Continuing to run the application...")

# Run the Flask application
subprocess.Popen([sys.executable, run_script])

# Run the main application
subprocess.Popen([sys.executable, main_script], cwd=client_dir)