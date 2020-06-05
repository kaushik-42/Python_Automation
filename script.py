import subprocess
for i in range(0, 5):
    subprocess.check_call(['python3', 'ex.py'])
#subprocess is a library that allows our python script to interact with the command line interface or shell.
""" where ex.py has 
print("hello world") and 
***the outut will be:***
hello world
hello world
hello world
hello world
hello world
"""
