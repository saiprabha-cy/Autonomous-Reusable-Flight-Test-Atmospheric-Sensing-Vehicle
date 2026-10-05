import math
from atmosphere import atmosphere

# Vehicle parameters
diameter = 0.100          # m
Cd = 0.30
area = math.pi * diameter**2 / 4

# Preliminary structural factor
load_factor = 1.5

velocities = [50, 100, 150, 200, 250, 300]
altitudes = [0, 2000, 5000]

print("AEROSENSE-01 AERODYNAMIC ENVELOPE")
print("=================================")

for altitude in altitudes:

    T, P, rho, a = atmosphere(altitude)

    print(f"\nAltitude: {altitude} m")
    print("-" * 72)
    print("Velocity | Mach | q(kPa) | Drag(N) | Design Load(N)")
    print("-" * 72)

    for velocity in velocities:

        mach = velocity / a
        q = 0.5 * rho * velocity**2
        drag = q * Cd * area
        design_load = drag * load_factor

        print(
            f"{velocity:8.0f} | "
            f"{mach:4.2f} | "
            f"{q/1000:6.2f} | "
            f"{drag:7.2f} | "
            f"{design_load:14.2f}"
        )