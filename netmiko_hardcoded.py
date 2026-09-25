from netmiko import ConnectHandler

device = {
    "host": "10.10.10.2",
    "username": "admin",
    "password": "cisco-automation123",
    "device_type": "cisco_ios"
}

commands = [
    "spanning-tree mode rapid-pvst",
    "spanning-tree vlan 10,20 priority 4096",
    "vlan 10",
    "name WEB_SERVERS",
    "vlan 20",
    "name APP_SERVERS",
    
    "interface GigabitEthernet1/0/1",
    "switchport mode access",
    "switchport nonegotiate",
    "switchport access vlan 10",

    "interface GigabitEthernet1/0/2",
    "switchport mode access",
    "switchport nonegotiate",
    "switchport access vlan 20",
    
    "interface GigabitEthernet1/0/3",
    "switchport mode trunk",
    "switchport nonegotiate",
    "switchport trunk allowed vlan 10,20",
    "channel-group 500 mode active",
    "ip router isis CORE",
    
    "interface GigabitEthernet1/0/4",
    "switchport mode trunk",
    "switchport nonegotiate",
    "switchport trunk allowed vlan 10,20",
    "channel-group 500 mode active",
    "ip router isis CORE",
    
    "interface Port-channel 500",
    "switchport mode trunk",
    "switchport nonegotiate",

    "interface Vlan10",
    "ip address 192.168.10.2 255.255.255.0",
    "standby version 2",
    "standby 500 ip 192.168.10.1",
    "standby 500 priority 110",
    "standby 500 preempt",
    "no shutdown",
    
    "interface Vlan20",
    "ip address 192.168.20.2 255.255.255.0",
    "standby version 2",
    "standby 500 ip 192.168.20.1",
    "standby 500 priority 110",
    "standby 500 preempt",
    "no shutdown",
    
    "ip access-list extended AUTOMATION-FILTER-LIST",
    "permit tcp any any eq 80",
    "permit tcp any any eq 443",
    "permit tcp any any eq 3389",
    "permit tcp any any eq 3390",
    "permit udp any any eq 3389",
    "permit udp any any eq 3390",
    "deny ip any any",
    
    "route-map OSPF_TO_BGP permit 10",
    "match ip address AUTOMATION-FILTER-LIST",
    "route-map OSPF_TO_BGP permit 20",
    
    "route-map BGP_LOCAL_PREF_IN permit 10",
    "match ip address AUTOMATION-FILTER-LIST",
    "set local-preference 200",
    "route-map BGP_LOCAL_PREF_IN permit 20",
    
    "ip route 0.0.0.0 0.0.0.0 10.10.10.1",
    
    "router ospf 500",
    "router-id 10.10.10.2",
    "network 192.168.10.0 0.0.0.255 area 0",
    "network 192.168.20.0 0.0.0.255 area 0",
    
    "router eigrp 500",
    "eigrp router-id 10.10.10.2",
    "network 10.0.0.0 0.255.255.255",
    
    "router bgp 65000",
    "bgp router-id 10.10.10.2",
    "neighbor 10.10.10.5 remote-as 65001",
    "neighbor 10.10.10.5 route-map BGP_LOCAL_PREF_IN in",
    "redistribute ospf 500 route-map OSPF_TO_BGP",
    "network 192.168.10.0 mask 255.255.255.0",
    "network 192.168.20.0 mask 255.255.255.0",
    
    "router isis CORE",
    "net 49.0001.0000.0000.0002.00",
    "is-type level-2-only"
]

print("Pushing fully hardcoded config via Netmiko...")
connection = ConnectHandler(**device)
connection.enable()

output = connection.send_config_set(commands)
print(output)

connection.save_config()
connection.disconnect()
print("Deployment complete.")
