# Author: Burak Dogancay
from cx_Freeze import setup, Executable
import sys
application_title = "My Application" # Use your own application name
main_python_file = "my_script.py" # Your python script
def setupSettings():
    base = None
    if sys.platform == "win32":
        base = "Win32GUI"
    includes = ["atexit","re"]
    setup(
            name = application_title,
            version = "0.1",
            description = "Your Description",
            options = {"build_exe" : {"includes" : includes }},
        executables = [Executable(main_python_file, base = base)])
  
def main():
  setupSettings()

if __name__ == '__main__':
    main()