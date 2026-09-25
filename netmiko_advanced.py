import yaml
import cli
from netmiko import ConnectHandler
with open('advanced_config.yaml') as f:
    data = yaml.safe_load(f)
device = {
    "host": "10.10.10.2",
    "username": "admin",
    "password": "cisco-automation123",
    "device_type": "cisco_ios"
}
commands = [
    # 1. VLANs & STP
    "spanning-tree mode rapid-pvst",
    "spanning-tree vlan 10,20 priority 4096",
    "vlan 10",
    "name WEB_SERVERS",
    "vlan 20",
    "name APP_SERVERS",
    
    "interface GigabitEthernet1/0/1",
    "no shutdown",
    "switchport mode access",
    "switchport nonegotiate",
    "switchport access vlan 10",

    "interface GigabitEthernet1/0/2",
    "no shutdown",
    "switchport mode access",
    "switchport nonegotiate",
    "switchport access vlan 20",
    
    "interface GigabitEthernet1/0/3",
    "no shutdown",
    "switchport mode trunk",
    "switchport nonegotiate",
    "switchport trunk allowed vlan 10,20",
    "channel-group 500 mode active",
    "ip router isis CORE",
    
    "interface GigabitEthernet1/0/4",
    "no shutdown",
    "switchport mode trunk",
    "switchport nonegotiate",
    "switchport trunk allowed vlan 10,20",
    "channel-group 500 mode active",
    "ip router isis CORE",
    
    "interface Port-channel 500",
    "no shutdown",
    "switchport mode trunk",
    "switchport trunk allowed vlan 10,20",
    "switchport nonegotiate",
