import ipaddress
import sys
import math

def IP_analyst(IP):
    IP = str(IP)
    ip = IP[:IP.find('/')]
    ip = ipaddress.ip_address(ip)
    netmask = ipaddress.IPv4Network(IP).netmask
    return ip, netmask
def mask_to_numHost(mask):
    # Caculating number of host available from subnetmask
    bit_subNet = mask%8
    octet_net = mask//8
    octet_remainder = 4 - octet_net
    #Host = octet hoàn chỉnh + octet bị chiếm

    numHost = 1
    # A class
    if octet_remainder == 3: 
        numHost *= 2*pow(2,8) 
        if bit_subNet > 0:
           bit_remainder = 8 - bit_subNet
           numHost *= sum(pow(2, x) for x in range (bit_remainder))
           return numHost
    # B class
    elif octet_remainder == 2:
        numHost *= 1*pow(2, 8)
        if bit_subNet > 0:
            bit_remainder = 8 - bit_subNet
            numHost *= sum(pow(2, x) for x in range(bit_remainder))
            return numHost
    # C class
    elif octet_remainder == 1:
        numHost *= 0*pow(2, 8) 
        if bit_subNet > 0:
           bit_remainder = 8 - bit_subNet 
           numHost += sum(pow(2, x) for x in range(bit_remainder))
           return numHost
def numhost_to_mask(numhost):
    # Return minium mask <int> can satisfy num of hosts needed
#    mask = 0
#    host = 0
#    bit_subnet = 0 #num of bits for subnet
#    bit_remainder = 0 #num of bit have been used for hosts
#    octet = 0 # num of octet have been used for hosts
#    total_host_available = 0
#
#    while (host + octet*255) - 2 < numhost:
#        host += pow(2, bit_remainder)
#        if bit_remainder == 7:
#            octet+=1
#            bit_remainder = 0 - 1 
#            host = 0 # Sum of hosts per octet
#        bit_remainder+=1
#    print('Bit for Host: ', bit_remainder)
#    total_host_available = (host + octet*255) - 2
#    print('Total host avaiable : ', total_host_available)
#    int_mask = 32 - (octet*8 + bit_remainder)
#    return int_mask , (octet*8 + bit_remainder)
    return math.ceil(math.log2(numhost+2))
        
def Subnet_division(IP, hosts):
    #IP form : xx.xx.xx.xx/subnetMask
    #host : number of hosts needed to divide from the IP address
    IP = str(IP) 
    # Gen new subnet mask from hosts (new mask >= old mask)
    int_mask = int(IP[IP.find('/')+1:])
    largest_host = mask_to_numHost(int_mask)
    ip = str(IP)[:IP.find('/')]
    IP = ipaddress.IPv4Network(IP)
    if(hosts <= largest_host):
        bits_host = numhost_to_mask(hosts)
        jump = bits_host
        ip = list(IP.subnets(new_prefix=(32-bits_host)))
        #Return list subnets available with num of hosts needed
        return ip
    else:
        print("\nImpossible for this number of hosts division")
    
    return 0
if(len(sys.argv) == 1): print('<commnad like> : python3 IPadd_handle.py <xx.xx.xx.xx/yy>')
else: 
    ip = sys.argv[1]
    ip = ipaddress.IPv4Network(ip)
    while True:
        #Dạng 2: với 1 địa chỉ ip, cần chia ip đó với số host yêu cầu (bài toán con của bài toán 3) 
        #Dạng 3: Công ty có 30 phòng, mỗi phòng cần 45 máy, chia subnet với một địa chỉ ip cho trước
        print('''
        ##################################
        \n1: IP class and subnetMask default.
        \n2: Subnet division (VLSM method)
        \n3: Subnets division  
        \nYour choice:
        ''')
        choice = int(input()) #number
        if choice == 1:
            IP, netmask =  IP_analyst(ip)
            print(f'''
                \nIP address : {IP}
                \nNetmaks : {netmask}
                  ''')
        if choice == 2:    
            num_of_hostneeded = int(input('\nSố hosts cần cho mỗi subnet: '))
            list_subnets = Subnet_division(ip, num_of_hostneeded)
            for subnets in list_subnets:
                print(f'''
                \n===========================
                \nIP address : {subnets[0]}
                \nThe First address: {subnets[1]}
                \nBroadcast  : {subnets.broadcast_address}
                      ''')
        if choice == 3:
            num_subnet = int(input('\nNumber of subnet need to divide'))
            num_host = int(input('\nNumber of hosts per subnet needed'))
            n = math.ceil(math.log2(num_subnet))  # Num of bit for subnet
            m = math.ceil(math.log2(num_host + 2)) # Num of bit for subnet hosts

            int_mask = int(str(ip)[str(ip).find('/')+1:])
            if(n+m <= 32 - (32//int_mask)):
                print("\nIt possible to divide")
                print(f'n: {n} , m: {m}')
                print(f'Satisfy MAXIMMUM num of network address: {pow(2,n)} and num of Hosts/network: {pow(2,m) - 2}')
                bit_host_subnet = m 
                bit_net_subnet = 32 - m 
                subnets = list(ip.subnets(new_prefix=bit_net_subnet)) 
                for subnet in subnets:
                    print(f'''
                    \n{subnet}
                    \nRange of IP avaiable : 
                    \n{subnet[1]} -> {subnet[-2]}
                    ''')
            else:
                print("\nImpossible for divide")
            