# AEROSENSE-01 Power Budget

voltage = 3.3  # V

loads = {
    "STM32": 80,
    "IMU": 10,
    "Pressure sensor": 5,
    "Temperature sensor": 2,
    "microSD": 50,
    "Telemetry interface": 40,
    "Regulator/system overhead": 30,
}

mission_hours = 1.0
margin_percent = 50

total_current = sum(loads.values())

power = voltage * total_current / 1000

energy = power * mission_hours

design_energy = energy * (1 + margin_percent / 100)

print("AEROSENSE-01 POWER BUDGET")
print("==========================")

for name, current in loads.items():
    print(f"{name:30} {current:5.1f} mA")

print("------------------------------------------")
print(f"Total current          : {total_current:.1f} mA")
print(f"Average power          : {power:.2f} W")
print(f"Mission duration       : {mission_hours:.2f} h")
print(f"Nominal energy         : {energy:.2f} Wh")
print(f"Design energy (+{margin_percent}%) : {design_energy:.2f} Wh")