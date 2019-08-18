import subprocess 
import re
import time

def banner():
	print("""
 _    _  ____   _____ _______ ___  _____ _____  
| |  | |/ __ \ / ____|__   __|__ \|_   _|  __ \ 
| |__| | |  | | (___    | |     ) | | | | |__) |
|  __  | |  | |\___ \   | |    / /  | | |  ___/ 
| |  | | |__| |____) |  | |   / /_ _| |_| |     
|_|  |_|\____/|_____/   |_|  |____|_____|_|     
     CODED BY @h4ck3r_dhanush

""")



banner()

victim = input("Enter Host or IP: ")

subprocess.call(["nslookup", victim])
