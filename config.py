from netmiko import ConnectHandler
from devic_info import R_1, R_2, R_3, R_4

router_1 = ConnectHandler(**R_1)
router_1.enable()
router_1.config_mode()

inter_loop_config = [
        "interface s3/0",
        "ip address 14.14.14.1 255.255.255.0",
        "no shutdown",
        "interface loopback 0",
        "ip address 1.1.1.1 255.255.255.255",
        "no shutdown"
]
print(router_1.send_config_set(inter_loop_config))

print("<<<<<<<<<<<<<<<<<<<<<<<<<no router-2 configuration >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

router_2 = ConnectHandler(**R_2)
router_2.enable()
router_2.config_mode()
inter_loop_config2 = [
        "interface s3/0",
        "ip address 24.24.24.1 255.255.255.0",
        "no shutdown",
        "interface loopback 0",
        "ip address 2.2.2.2 255.255.255.255",
        "no shutdown"
]
print(router_2.send_config_set(inter_loop_config2))

print("<<=============================router-3 configuration===========================================>>")

router_3 = ConnectHandler(**R_3)
router_3.enable()
router_3.config_mode()

inter_loop_config3 = [
        "interface f0/0",
        "ip address 34.34.34.1 255.255.255.0",
        "no shutdown",
        "interface loopback 0",
        "ip address 3.3.3.3 255.255.255.255",
        "no shutdown"
]
print(router_3.send_config_set(inter_loop_config3))

print("<<===================================this is internet router configuration ==========================>>")

router_4 = ConnectHandler(**R_4)
router_4.enable()
router_4.config_mode()

inter_loop_config4 = [
        "interface s3/0",
        "ip address 24.24.24.2 255.255.255.0",
        "no shutdown",
        "interface s3/1",
        "ip address 14.14.14.2 255.255.255.0",
        "no shutdown",
        "interface f0/0",
        "ip address 34.34.34.2 255.255.255.0",
        "no shutdown"
]
print(router_4.send_config_set(inter_loop_config4))
