#Program to automate update and upgrade of linux system.

import os
from colorama import Back, Fore
import time

print(Fore.BLUE + "Updating packages...")
time.sleep(2)
os.system("sudo apt-get update")
print(Fore.BLUE + "Upgrading...")
time.sleep(2)
os.system("sudo apt-get full-upgrade -y")

rmv_packages = str(input(Fore.YELLOW + "Sometimes some packages are automatically installed and not really required. Do you want to remove them? (y/n): "))

if(rmv_packages == "y"):
    print("Removing not required packages...")
    time.sleep(1)
    os.system("sudo apt-get autoremove")

print(Fore.RED + "Cleaning up terminal...")
time.sleep(2)
os.system("clear")

