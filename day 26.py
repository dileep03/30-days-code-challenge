#30-days-code-challenge- DAY 26(5/7/22)
#learning python basics

#device details
import socket

hostnm = socket.gethostname()
ipaddr = socket.gethostbyname(hostnm)

print("IP Address is:", ipaddr)
print("Hostname or Device Name =", hostnm)