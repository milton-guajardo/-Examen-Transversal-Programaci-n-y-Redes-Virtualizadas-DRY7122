from netmiko import ConnectHandler
import json
# Parámetros de conexión al switch Cisco
device = {
    "device_type": "cisco_ios_telnet",
    "host": "20.1.1.1",
    "username": "admin",
    "password": "cisco",
     "port": 23,
    "secret": "cisco"
}

# Establecer conexión Telnet
net_connect = ConnectHandler(**device)


# Comando para listar interfaces (puedes ajustar el comando según el tipo de información que necesites)
interface_command = "show ip interface brief"

# Enviar comando al dispositivo y obtener la salida
output = net_connect.send_command(interface_command)

# Procesar la salida para obtener la lista de interfaces
interfaces = []
for line in output.splitlines():
    if line.strip() and not line.startswith('Interface'):
        parts = line.split()
        interface_info = {
            "interface": parts[0],
            "ip_address": parts[1],
            "status": parts[4],
            "protocol": parts[5]
        }
        interfaces.append(interface_info)

# Convertir la lista de interfaces a formato JSON
interfaces_json = json.dumps(interfaces, indent=4)

# Imprimir el resultado JSON
print(interfaces_json)