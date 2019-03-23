#! env python3
# sort ipv4 addresses
import ipaddress

f=open('ip/ips')
l=[]
for ip in f:
    l.append(int(ipaddress.ip_address(str.strip(ip))))

l.sort()

for x in l:
    print(ipaddress.ip_address(x))
