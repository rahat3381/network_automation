from netmiko import ConnectHandler
from datetime import datetime

device = {
    "host": "10.10.10.2",
    "username": "admin",
    "password": "cisco-automation123",
    "device_type": "cisco_ios"
}

print("Connecting to router...")
connection = ConnectHandler(**device)
connection.enable()

print("Pulling running-config...")
running_config = connection.send_command("show running-config")

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"router_running_config_{timestamp}.txt"

with open(filename, "w") as file:
    file.write(running_config)

print(f"Success! Configuration saved to: {filename}")
connection.disconnect()
