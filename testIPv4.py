import ipaddress 
import sys
if(len(sys.argv) < 2): print('<commnad like> : python3 IPadd_handle.py <xx.xx.xx.xx/yy>')
else:
    ip = ipaddress.IPv4Address(sys.argv[1])
    #Class A
    if ip > ipaddress.IPv4Address('10.0.0.0') and ip <ipaddress.IPv4Address('10.255.255.255'): print("Class A")
    #Class B
    elif ip > ipaddress.IPv4Address('172.16.0.0') and ip <ipaddress.IPv4Address('172.31.255.255'): print( "Class B")
    #Class C
    elif ip > ipaddress.IPv4Address('192.168.0.0') and ip <ipaddress.IPv4Address('192.168.255.255'): print("Class C")
    else: print("Public address")
    