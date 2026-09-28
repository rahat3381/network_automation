from netmiko import ConnectHandler
device = {
    "host": "10.10.10.2",
    "username": "admin",
    "password": "cisco-automation123",
    "device_type": "cisco_ios"
}
show_commands = [
    "show ip interface brief",
    "show etherchannel summary",
    "show port-channel summary",
    "show standby brief",
    "show ip route",
    "show ip bgp summary",
    "show ip ospf neighbor",
    "show ip isis neighbor",
    "show ip access-list",
    "show route-map OSPF_TO_BGP permit 10",
    "show route-map BGP_LOCAL_PREF_IN permit 10",
    "show spanning-tree"
]
print(f"Connecting to {device['host']} to verify operational state...")
connection = ConnectHandler(**device)
connection.enable()
for cmd in show_commands:
    print(f"\n=========================================")
    print(f" {cmd.upper()}")
    print(f"=========================================")
    print(connection.send_command(cmd))
connection.disconnect()
print("\nVerification complete.")
