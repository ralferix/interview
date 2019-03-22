# sort ipv4 addresses
# x.x.x.x
# import ipaddress

def ip2dec(ip):
    ip_num=0
    mult=4
    for n in ip.split('.'):
        print(n)
        mult-=1
        ip_num+=256^mult*int(n)
        return(ip_num)

ips="""1.1.1.1
2.2.2.2
"""

for ip in ips:
    print ip2dec(ip)
