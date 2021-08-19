from netmiko import ConnectHandler
from pprint import pprint
from devic_info import R_4, R_2, R_3, R_1

dm_router1 = ConnectHandler(**R_1)
dm_router1.enable()
dm_router1.config_mode()

vpn_config = [
    "interface tunnel 0",
    "ip address 10.10.10.1 255.255.255.0",
    "ip nhrp network-id 123",
    "ip nhrp nhs 10.10.10.3",
    "ip nhrp map 10.10.10.3 34.34.34.1",
    "tunnel source s3/0",
    "tunnel destination 34.34.34.1"
]
print(dm_router1.send_config_set(vpn_config))

print("<<===============================this is router-2===========================>>")

dm_router2 = ConnectHandler(**R_2)
dm_router2.enable()
dm_router2.config_mode()

vpn_config2 = [
    "interface tunnel 0",
    "ip address 10.10.10.2 255.255.255.0",
    "ip nhrp network-id 123",
    "ip nhrp nhs 10.10.10.3",
    "tunnel source s3/0",
    "tunnel destination 34.34.34.1"
]
print(dm_router2.send_config_set(vpn_config2))

dm_router3 = ConnectHandler(**R_3)
dm_router3.enable()
dm_router3.config_mode()

vpn_config3 = [
    "interface tunnel 0",
    "ip address 10.10.10.3 255.255.255.0",
    "ip nhrp network-id 123",
    "tunnel mode gre multipoint",
    "tunnel source f0/0"
    ]
print(dm_router3.send_config_set(vpn_config3))