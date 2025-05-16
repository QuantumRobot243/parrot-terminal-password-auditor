# cli.py
import os
import time
from termcolor import colored
from utils import typewriter, red_prompt
from password_strength import evaluate_password

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    typewriter(colored("Initializing [REDACTED] Password Audit System...", "cyan"))
    time.sleep(1)
    typewriter(colored("Bypassing security protocols...", "magenta"))
    time.sleep(0.5)
    typewriter(colored("Accessing underground databases...\n", "red"))
    
    while True:
        try:
            red_prompt()
            password = input()
            if password.lower() in ['exit', 'quit']:
                break
                
            print(colored("\n[+] Scanning dark web archives...", "yellow"))
            time.sleep(1)
            print(colored("[+] Calculating cryptographic entropy...", "yellow"))
            time.sleep(0.7)
            print(colored("[+] Cross-referencing breach databases...\n", "yellow"))
            time.sleep(0.3)
            
            result = evaluate_password(password)
            print("\n" + "═" * 50)
            print(colored("‖ AUDIT RESULT ‖", "white", "on_red"))
            print(result)
            print("═" * 50 + "\n")
            
        except KeyboardInterrupt:
            print(colored("\n[!] Operation aborted by user", "red"))
            break

if __name__ == "__main__":
    main()
