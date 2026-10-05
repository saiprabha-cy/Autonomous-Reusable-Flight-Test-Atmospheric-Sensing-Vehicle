# AEROSENSE-01 Telemetry Budget

packet_size = 56          # bytes
telemetry_rate = 20       # packets/sec

payload_rate = packet_size * telemetry_rate

# 8 bits per byte
raw_bit_rate = payload_rate * 8

# UART overhead approximation:
# 1 start bit + 8 data bits + 1 stop bit = 10 bits/byte
uart_bit_rate = payload_rate * 10

print("AEROSENSE-01 TELEMETRY BUDGET")
print("==============================")

print(f"Packet size          : {packet_size} bytes")
print(f"Telemetry rate       : {telemetry_rate} packets/s")
print(f"Data rate            : {payload_rate} bytes/s")
print(f"Raw payload rate     : {raw_bit_rate} bit/s")
print(f"UART line rate       : {uart_bit_rate} bit/s")

print("\nCandidate UART rates:")

for baud in [9600, 19200, 38400, 57600, 115200]:

    margin = baud / uart_bit_rate

    status = "SUFFICIENT" if margin >= 1.5 else "MARGINAL"

    print(
        f"{baud:6} baud -> "
        f"{margin:5.2f}x capacity -> {status}"
    )