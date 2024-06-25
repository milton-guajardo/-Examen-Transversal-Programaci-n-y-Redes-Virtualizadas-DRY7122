# vlan.py
# Solicitar al usuario el número de VLAN
vlan = int(input("Ingrese el número de VLAN: "))

# Determinar si la VLAN pertenece al rango normal o extendido
if 1 <= vlan <= 1005:
    print(f"La VLAN {vlan} pertenece al rango normal.")
elif 1006 <= vlan <= 4094:
    print(f"La VLAN {vlan} pertenece al rango extendido.")
else:
    print("Número de VLAN no válido.")
