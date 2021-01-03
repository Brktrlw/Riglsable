#!/usr/bin/env python
import os
import time
x=0
while x<3:
	print("\033[1;32mPlease wait,loading.")
	print("\033[0;33mContinue the questions by pressing the letter \033[0;34mY.\033[0;37m")
	time.sleep(0.5)
	os.system("clear")
	print("\033[1;32mPlease wait,loading..")
	print("\033[0;33mContinue the questions by pressing the letter \033[0;34mY.\033[0;37m")
	time.sleep(0.5)
	os.system("clear")
	print("\033[1;32mPlease wait,loading...\033[0;33m")
	print("\033[0;33mContinue the questions by pressing the letter \033[0;34mY.\033[0;37m")
	time.sleep(0.5)
	os.system("clear")
	x+=1
os.system("apt-get update")
os.system("apt install python3-pip")
os.system("apt-get install python3")
os.system("apt install python")
os.system("pip install pyqt5")
os.system("pip install pyqt5-tools")
os.system("pip install wafw00f==0.9.4")
os.system("apt-get install nmap")
print("""
    \033[1;32mInstallation completed successfully.
""")
time.sleep(2)
