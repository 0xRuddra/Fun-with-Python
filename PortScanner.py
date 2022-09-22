#!/bin/python3

import sys
import socket
from datetime import datetime

if len(sys.argv) ==2: #sys.argv will check if the user gives the ip or not
        target=socket.gethostbyname(sys.argv[1]) # socket.gethostbyname will convert arg in ipv4
else:
        print("invalid hostname")
        print("Plese enter: python3 scanner.py <ip>")
        sys.exit()

print("_"*50)
print("Scanning Target : "+target)
print("Time : "+str(datetime.now()))
print("_"*50)

try:

        for port in range(50,85):
                sckt=socket.socket(socket.AF_INET,socket.SOCK_STREAM) #socket.socket() is for creating a socket.. socket.AF_INET is the ip and socket.SOCK_STREAM is port
                socket.setdefaulttimeout(1)
                result=sckt.connect_ex((target,port)) #if socket can not build a connection then it will return 1 
                print(f"checking port: {port}")
                if result ==0:
                        print(f"{port} is open")
                        sckt.close()


except KeyboardInterrupt:
        print("\n Scanner stoped")
        sys.exit()
except socket.gaierror:
        print("hostname could not be resolved")
        sys.exit()
except socket.error:
        print(f"{target} is not open")
        sys.exit()
