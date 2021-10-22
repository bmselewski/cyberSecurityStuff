#Brendan Selewski bms4yzc 10/8/2021
import socket
import sys
from datetime import datetime

target = raw_input("Enter a target to scan: ")
targetIP = socket.gethostbyname(target)
portStart = raw_input("Enter a start port: ")
portEnd = raw_input("Enter an end port: ")


print "Scan of", targetIP, "on ports", portStart, "to", portEnd, "starting at", datetime.now()


try:
    for port in range(int(portStart),int(portEnd)+1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((targetIP, port))
        if result == 0:
            print "Port", port, ": Open"
        else:
	    print "Port", port, ": Closed"

        s.close()
except socket.timeout:
    print "Timeout error"
    sys.exit()