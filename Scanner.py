import os
import platform
import socket
from datetime import datetime

class PortScanner():
    def __init__(self, ip):
        self.ip = ip
    
    def scanner(self):
        print("Scan report for", self.ip)
        print("{}\t{}\t{}".format("PORT", "STATE", "SERVICE"))
        for port in range(0,65536):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            connect = sock.connect_ex((self.ip, port))
            if connect == 0:
                try:
                    print("{}\t{}\t{}".format(str(port)+"/tcp", "open", socket.getservbyport(port, "tcp")))
                except:
                    continue
        

class DeviceScanner():
    def __init__(self, net_addr):
        self.net_addr = net_addr
        self.request = ""

    def get_platform(self):
        return platform.system()
    
    def check_platform(self):
        if self.get_platform() == "Windows":
            self.request = "ping -n 1 "
        elif self.get_platform() == "Linux":
            self.request = "ping -c 1 "
        else:
            self.request = "ping -c 1 "
    
    def scanner(self):
        net1 = self.net_addr.split('.')
        dot = '.'

        net2 = net1[0] + dot + net1[1] + dot + net1[2] + dot
        print ("Scanning in Progress:")

        for ip in range(1,10):
            addr = net2 + str(ip)
            # print("addr:", addr)
            self.check_platform()
            comm = self.request + addr
            # print("comm", comm)
            response = os.popen(comm)
            
            for line in response.readlines():
                if(line.count("rtt")): 
                    print (addr, "--> Live")

    
if __name__ == "__main__":
    pScan = PortScanner("192.168.1.1")
    pScan.scanner()
    
