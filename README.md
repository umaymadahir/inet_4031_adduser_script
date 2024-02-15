## inet_4031_adduser_script

## description

This repository contains a Python script called `create-users.py` that helps automate the process of creating user accounts on a system. With this script, system administrators can quickly set up new user accounts with just a few steps.

## operation

Using the `create-users.py` script is quite simple! Just follow these 2 steps:

1. User List: Create a file named `create-users.input` and list your users along with their details. Each line represents one user, with fields separated by tabs. 

2. Run the Script: Make sure you have Python 3 installed on your system. Or just make few edits to the python file depending on what version of python your computer is running. Then, run the script using one of these two methods:
   - If you prefer using the command line, run `sudo ./create-users.py < create-users.input`.
   - Or, you can use a pipe to send input from the file by running `cat create-users.input | sudo ./create-users.py`.
