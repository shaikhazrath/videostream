import os
import subprocess

# Check if requirements.txt file exists
if os.path.exists("requirements.txt"):
    print("Installing dependencies...")
    subprocess.run(["pip", "install", "-r", "requirements.txt"])
else:
    print("Error: requirements.txt file not found.")
    exit(1)



print("Starting Django server...")
subprocess.run(["python", "manage.py", "runserver"])
