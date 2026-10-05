# AEROSENSE-01 Mass Budget

components = {
    "Primary structure": 650,
    "Internal supports": 100,
    "Flight computer PCB": 80,
    "Sensors": 70,
    "Battery": 200,
    "Telemetry electronics": 50,
    "Wiring/connectors": 60,
    "Data storage": 20,
    "Recovery/interface hardware": 100,
    "Fasteners": 40,
}

margin_percent = 15

dry_mass = sum(components.values())
margin = dry_mass * margin_percent / 100
total_mass = dry_mass + margin

print("AEROSENSE-01 MASS BUDGET")
print("=========================")

for name, mass in components.items():
    print(f"{name:32} {mass:6.1f} g")

print("-----------------------------------------")
print(f"Estimated dry mass       : {dry_mass:.1f} g")
print(f"Mass margin ({margin_percent}%)      : {margin:.1f} g")
print(f"Total estimated mass     : {total_mass:.1f} g")
print(f"Total estimated mass     : {total_mass/1000:.3f} kg")