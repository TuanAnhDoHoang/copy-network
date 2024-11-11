from faker import Faker
import ipaddress

gen = Faker()
ipv4 = gen.ipv4()
ipv4_p = gen.ipv4_private()
ipv4_b = gen.ipv4_public()
ipv6 = gen.ipv6()

ipv4 = ipaddress.IPv4Network(ipv4)
ipv4_p = ipaddress.IPv4Network(ipv4_p)
ipv4_b = ipaddress.IPv4Network(ipv4_b)
ipv6 = ipaddress.IPv6Network(ipv6)

print(f'''
    IPv4 : {ipv4}
    IPv4 private: {ipv4_p}
    IPv4 public: {ipv4_b}
    IPv6: {ipv6}
      ''')