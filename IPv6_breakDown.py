import ipaddress
import sys

if len(sys.argv) < 2: 
    print(f'command form: python3 {sys.argv[0]} <ipv6/xx> ')
else:
    ipv6_address = sys.argv[1]
    ipv6_address = ipaddress.IPv6Network(ipv6_address)

    print('''
        Địa chỉ ipv6 có 3 loại: multicast -> trỏ một nhóm thiết bị và unicast  -> trỏ 1 thiết bị và anycast
        1)Unicast : địa chỉ trỏ đến 1 thiết bị 
        - unique -> trỏ 1 thiết bị private
        - global -> trỏ 1 thiết bị đại diện public
        - link-local -> Giao tiếp trong mạng nội bộ mà không cần định tuyến  (FE80::/10)
        - loopback : dạng ::-1
        ***********************************
         Chương trình làm rõ 1 địa chỉ ipv6
        ************************************
        ''')

    print("Địa chỉ IPv6:", ipv6_address)
    print("Địa chỉ dạng nén:", ipv6_address.compressed)
    print("Địa chỉ netmask: ", ipv6_address.with_netmask)
    print("Địa chỉ dạng đầy đủ:", ipv6_address.exploded)
    print("Là địa chỉ toàn cục?", ipv6_address.is_global)
    print("Là địa chỉ liên kết cục bộ?", ipv6_address.is_link_local)
    print("Là địa chỉ multicast?", ipv6_address.is_multicast)
    print("Là địa chỉ loopback?", ipv6_address.is_loopback)
    print("Là địa chỉ chỉ định riêng (unique local)?", ipv6_address.is_private)
    print("Là địa chỉ không xác định?", ipv6_address.is_unspecified)