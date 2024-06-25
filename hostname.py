from netmiko import ConnectHandler

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


# Ingresar al modo enable
net_connect.enable()

# Comando para cambiar el hostname
hostname_command = "hostname Araya-Guajardo"

# Enviar comando al dispositivo
output = net_connect.send_config_set(hostname_command)

# Imprimir el resultado del cambio de hostname
print(output)

# Cerrar la conexión
net_connect.disconnect()