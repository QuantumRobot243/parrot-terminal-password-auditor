# utils.py
import sys
import time
import os
from termcolor import colored

def typewriter(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)
    print()

def red_prompt():
    os.system('color 4' if os.name == 'nt' else '')
    print(colored("[REDACTED]@root~# ", "red"), end="")
