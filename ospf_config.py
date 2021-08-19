from netmiko import ConnectHandler
from devic_info import R_1, R_2, R_3, R_4

net_connect = ConnectHandler(**R_1)
net_connect.enable()
net_connect.config_mode()

ospf_config = [
    "router ospf 10",
    "network 14.14.14.0 0.0.0.255 area 0",
    "no shutdown"
]
print(net_connect.send_config_set(ospf_config))
print("<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

net_connect1 = ConnectHandler(**R_2)
net_connect1.enable()
net_connect1.config_mode()
 
ospf_config1 = [
    "router ospf 10",
    "network 24.24.24.0 0.0.0.255 area 0",
    "no shutdown"
]  
print(net_connect1.send_config_set(ospf_config1))

print("=========================This is router 3 configuration")
net_connect2 = ConnectHandler(**R_3)
net_connect2.enable()
net_connect2.config_mode()

ospf_config2 =[
    "router ospf 10",
    "network 34.34.34.0 0.0.0.255 area 0",
    "no shutdown"
]
print(net_connect2.send_config_set(ospf_config2))

print("<<++++++++++++++++++++this is internet router configuration ++++++++++++++++++++++++")
net_connect3 = ConnectHandler(**R_4)
net_connect3.enable()
net_connect3.config_mode()

ospf_config3 =[
    "router ospf 10",
    "network 14.14.14.0 0.0.0.255 area 0",
    "network 24.24.24.0 0.0.0.255 area 0",
    "network 34.34.34.0 0.0.0.255 area 0"
]
print(net_connect3.send_config_set(ospf_config3))
