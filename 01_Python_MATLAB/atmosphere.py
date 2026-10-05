import math

# AEROSENSE-01 Standard Atmosphere Model
# ISA troposphere: 0-11 km

R = 287.05       # J/(kg K)
g = 9.80665      # m/s^2
gamma = 1.4

T0 = 288.15      # K
P0 = 101325.0    # Pa
L = 0.0065       # K/m


def atmosphere(altitude_m):

    if altitude_m < 0 or altitude_m > 11000:
        raise ValueError("Altitude must be between 0 and 11000 m")

    T = T0 - L * altitude_m

    P = P0 * (T / T0) ** (g / (R * L))

    rho = P / (R * T)

    a = math.sqrt(gamma * R * T)

    return T, P, rho, a


if __name__ == "__main__":

    print("AEROSENSE-01 ATMOSPHERIC MODEL")
    print("--------------------------------")
    print("Altitude | Temp(K) | Pressure(kPa) | Density(kg/m^3) | Speed of Sound(m/s)")
    print("------------------------------------------------------------------------")

    for altitude in [0, 1000, 2000, 3000, 4000, 5000]:

        T, P, rho, a = atmosphere(altitude)

        print(
            f"{altitude:8.0f} | "
            f"{T:7.2f} | "
            f"{P/1000:13.2f} | "
            f"{rho:16.3f} | "
            f"{a:20.2f}"
        )