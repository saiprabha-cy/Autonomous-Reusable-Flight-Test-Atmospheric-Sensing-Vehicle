import math
from atmosphere import atmosphere
# -----------------------------
# AEROSENSE-01 Preliminary Model
# -----------------------------

# Atmospheric conditions
rho = 1.225          # kg/m^3
temperature = 288.15 # K
gamma = 1.4
R = 287.05           # J/(kg K)

# Vehicle
diameter = 0.100     # m
velocity = 250.0     # m/s
Cd = 0.30

# Reference area
area = math.pi * diameter**2 / 4

# Speed of sound
speed_of_sound = math.sqrt(gamma * R * temperature)

# Mach number
mach = velocity / speed_of_sound

# Dynamic pressure
q = 0.5 * rho * velocity**2

# Drag
drag = q * Cd * area

# Design load
design_load = 1.5 * drag

print("AEROSENSE-01 PRELIMINARY ANALYSIS")
print("----------------------------------")
print(f"Reference area     : {area:.6f} m^2")
print(f"Speed of sound     : {speed_of_sound:.2f} m/s")
print(f"Mach number        : {mach:.3f}")
print(f"Dynamic pressure   : {q/1000:.2f} kPa")
print(f"Estimated drag     : {drag:.2f} N")
print(f"Design axial load  : {design_load:.2f} N")

print("\nVELOCITY SWEEP")
print("V (m/s) | Mach | q (kPa) | Drag (N)")
print("--------------------------------------")

for velocity in [50, 100, 150, 200, 250, 300]:

    mach = velocity / speed_of_sound
    q = 0.5 * rho * velocity**2
    drag = q * Cd * area

    print(
        f"{velocity:7.0f} | "
        f"{mach:4.2f} | "
        f"{q/1000:7.2f} | "
        f"{drag:8.2f}"
    )