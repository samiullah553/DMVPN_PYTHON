from netmiko import ConnectHandler
from devic_info import R_1, R_2, R_3, R_4

connection1 = ConnectHandler(**R_1)
connection1.enable()
connection1.config_mode()
eigrp_router1 = [
    "interface tunnel 0",
    "shutdown",
    "router eigrp 10",
    "no auto",
    "network 1.1.1.1",
    "network 10.10.10.1",
    "interface tunnel 0",
    "no shutdown",
    "interface tunnel 0",
    "ip nhrp map multicast 34.34.34.1"
    ] 
print(connection1.send_config_set(eigrp_router1))

connection2 = ConnectHandler(**R_2)
connection2.enable()
connection2.config_mode()

eigrp_router2 = [
    "interface tunnel 0",
    "shutdown",
    "router eigrp 10",
    "no auto",
    "network 2.2.2.2",
    "network 10.10.10.2",
    "interface tunnel 0",
    "no shutdown",
    "interface tunnel 0",
    "ip nhrp map multicast 34.34.34.1"
]
print(connection2.send_config_set(eigrp_router2))

connection3 = ConnectHandler(**R_3)
connection3.enable()
connection3.config_mode()

eigrp_router3 = [
    "interface tunnel 0",
    "shutdown",
    "router eigrp 10",
    "network 10.10.10.3",
    "no auto","interface tunnel 0",
    "no shutdown",
    "interface tunnel 0",
    "ip nhrp map multicast dynamic",
    "interface tunnel 0",
    "no ip split-horizon eigrp 10"
]
print(connection3.send_config_set(eigrp_router3))
