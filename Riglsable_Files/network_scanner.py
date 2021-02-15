import scapy.all as scapy
import time
import os
def scan():
    print("Local network scanning,please wait...")
    arp_request = scapy.ARP(pdst="192.168.1.1/24")
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=5, verbose=False)[0]
    clients_list = []
    os.system("clear")
    for element in answered_list:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        clients_list.append(client_dict)
    return clients_list
def print_result(results_list):
    print("\t\033[1;32m****Scan completed successfully****\033[0;33m\n")
    print("\t  IP Address\t\t  MAC Address\n---------------------------------------------------------")
    for client in results_list:
        print("\t",client["ip"] + "\t\t" + client["mac"])
results_list=scan()
print_result(results_list)
time.sleep(30)