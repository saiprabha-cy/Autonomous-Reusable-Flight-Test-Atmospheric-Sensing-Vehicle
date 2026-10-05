# AEROSENSE-01 — Preliminary Mission Analysis & Engineering Baseline

## Stage 1 — Python/MATLAB Calculation & Requirements

AEROSENSE-01 is a multidisciplinary aerospace flight-test and atmospheric sensing demonstrator developed as a portfolio-level engineering project.

The objective of Stage 1 was to establish the **numerical engineering baseline** that will drive the subsequent CAD, CFD, PCB, embedded software, telemetry, and manufacturing stages.

This stage uses Python for preliminary engineering calculations. MATLAB/Octave will be used later where matrix-based analysis, dynamic modelling, control-oriented calculations, or visualization provide additional value.

---

## 1. Stage Objective

The primary purpose of this stage was to answer:

* What is the preliminary vehicle size?
* What aerodynamic environment will the vehicle experience?
* What are the expected aerodynamic loads?
* What mass must the structure and avionics support?
* What electrical power is required?
* What telemetry data rate is required?
* What preliminary engineering requirements should drive the CAD and avionics design?

The results are **preliminary design estimates**, not flight qualification data.

---

# 2. Preliminary Vehicle Definition

| Parameter                   |                    Preliminary Value |
| --------------------------- | -----------------------------------: |
| Vehicle type                |     Instrumented flight-test vehicle |
| Configuration               | Axisymmetric body + stabilizing fins |
| Maximum diameter            |                               100 mm |
| Target overall length       |                              ~800 mm |
| Target mass                 |                              ~1.6 kg |
| Reference altitude range    |                               0–5 km |
| Analysis velocity range     |                           50–300 m/s |
| Nominal design velocity     |                              250 m/s |
| Maximum analysis velocity   |                              300 m/s |
| Primary flight computer     |                                STM32 |
| Ground/telemetry controller |                                ESP32 |
| Primary sensors             |         IMU + pressure + temperature |
| Data storage                |                              microSD |
| Manufacturing               |                                  FDM |
| CAD platform                |                           Fusion 360 |
| CFD platform                |                             SimScale |

The 300 m/s condition is an **analysis-envelope condition**, not a statement that the final vehicle will actually reach this velocity.

---

# 3. Atmospheric Model

The preliminary atmospheric model uses the **International Standard Atmosphere (ISA) troposphere model from 0–11 km**.

The model calculates:

* Temperature
* Atmospheric pressure
* Air density
* Speed of sound

The implementation is contained in:

```text
atmosphere.py
```

### Model constants

```text
R     = 287.05 J/(kg·K)
g     = 9.80665 m/s²
γ     = 1.4
T₀    = 288.15 K
P₀    = 101325 Pa
L     = 0.0065 K/m
```

### Calculated atmospheric conditions

| Altitude | Temperature |   Pressure |     Density | Speed of Sound |
| -------: | ----------: | ---------: | ----------: | -------------: |
|      0 m |    288.15 K | 101.33 kPa | 1.225 kg/m³ |     340.29 m/s |
|     1 km |    281.65 K |  89.87 kPa | 1.112 kg/m³ |     336.43 m/s |
|     2 km |    275.15 K |  79.50 kPa | 1.006 kg/m³ |     332.53 m/s |
|     3 km |    268.65 K |  70.11 kPa | 0.909 kg/m³ |     328.58 m/s |
|     4 km |    262.15 K |  61.64 kPa | 0.819 kg/m³ |     324.58 m/s |
|     5 km |    255.65 K |  54.02 kPa | 0.736 kg/m³ |     320.53 m/s |

The atmospheric model provides the density and speed-of-sound inputs required by the aerodynamic analysis.

---

# 4. Aerodynamic Envelope

The aerodynamic model uses:

$$
q=\frac{1}{2}\rho V^2
$$

where:

* \(q\) = dynamic pressure
* \(\rho\) = atmospheric density
* \(V\) = vehicle velocity

The preliminary drag model uses:

$$
D=qC_DA
$$

with:

```text
Vehicle diameter = 0.100 m
Cd                = 0.30
Reference area    = 0.007854 m²
```

A preliminary structural design factor of:

```text
Load factor = 1.5
```

was applied to the calculated aerodynamic drag.

Therefore:

$$
F_{design}=1.5D
$$

The aerodynamic calculations are contained in:

```text
aerodynamics.py
```

---

## 5. Sea-Level Aerodynamic Results

|    Velocity |     Mach | Dynamic Pressure |        Drag |  Design Load |
| ----------: | -------: | ---------------: | ----------: | -----------: |
|      50 m/s |     0.15 |         1.53 kPa |      3.61 N |       5.41 N |
|     100 m/s |     0.29 |         6.13 kPa |     14.43 N |      21.65 N |
|     150 m/s |     0.44 |        13.78 kPa |     32.47 N |      48.71 N |
|     200 m/s |     0.59 |        24.50 kPa |     57.73 N |      86.59 N |
| **250 m/s** | **0.73** |    **38.28 kPa** | **90.20 N** | **135.30 N** |
|     300 m/s |     0.88 |        55.13 kPa |    129.89 N |     194.83 N |

At the nominal 250 m/s condition:

```text
Mach number       ≈ 0.735
Dynamic pressure  ≈ 38.28 kPa
Estimated drag    ≈ 90.20 N
Design axial load ≈ 135.30 N
```

These values establish the preliminary aerodynamic loading condition that will later be used to guide structural CAD and CFD analysis.

---

# 6. Altitude Effect

Aerodynamic performance was also evaluated at:

```text
0 m
2000 m
5000 m
```

At higher altitude, atmospheric density decreases, resulting in lower dynamic pressure and aerodynamic drag for the same velocity.

For example, at 250 m/s:

| Altitude | Dynamic Pressure |    Drag | Design Load |
| -------: | ---------------: | ------: | ----------: |
|      0 m |        38.28 kPa | 90.20 N |    135.30 N |
|     2 km |        31.45 kPa | 74.11 N |    111.16 N |
|     5 km |        23.00 kPa | 54.20 N |     81.30 N |

This demonstrates why aerodynamic loading cannot be defined from velocity alone; the atmospheric operating condition must also be considered.

---

# 7. Preliminary Mass Budget

The initial mass budget was created to determine whether the proposed vehicle architecture is compatible with the target mass.

The calculation is contained in:

```text
mass_budget.py
```

### Preliminary allocation

| Subsystem                   |         Mass |
| --------------------------- | -----------: |
| Primary structure           |        650 g |
| Internal supports           |        100 g |
| Flight computer PCB         |         80 g |
| Sensors                     |         70 g |
| Battery                     |        200 g |
| Telemetry electronics       |         50 g |
| Wiring/connectors           |         60 g |
| Data storage                |         20 g |
| Recovery/interface hardware |        100 g |
| Fasteners                   |         40 g |
| **Estimated dry mass**      |   **1370 g** |
| **15% mass margin**         |  **205.5 g** |
| **Total estimated mass**    | **1575.5 g** |

Therefore:

```text
Estimated design mass ≈ 1.575 kg
```

This supports the preliminary target of approximately:

```text
1.6 kg
```

The mass budget will be updated after the CAD geometry, PCB, sensor selection, battery selection, wiring, and manufactured components are defined.

---

# 8. Preliminary Power Budget

The power model estimates the electrical demand of the flight avionics.

The calculation is contained in:

```text
power_budget.py
```

### Preliminary loads

| Subsystem                 |    Current |
| ------------------------- | ---------: |
| STM32                     |      80 mA |
| IMU                       |      10 mA |
| Pressure sensor           |       5 mA |
| Temperature sensor        |       2 mA |
| microSD                   |      50 mA |
| Telemetry interface       |      40 mA |
| Regulator/system overhead |      30 mA |
| **Total**                 | **217 mA** |

At a nominal 3.3 V:

$$
P=VI
$$

giving:

```text
Average power ≈ 0.72 W
```

For a preliminary one-hour operating duration:

```text
Nominal energy ≈ 0.72 Wh
```

With a 50% design margin:

```text
Design energy ≈ 1.07 Wh
```

This is a preliminary electronics-only estimate. Final battery selection will be performed after the actual power architecture, regulators, sensors, storage device, telemetry hardware, and operating duty cycles are finalized.

---

# 9. Telemetry Budget

The telemetry calculation determines the minimum communication bandwidth required by the proposed flight-data packet.

The calculation is contained in:

```text
telemetry_budget.py
```

### Preliminary telemetry parameters

```text
Packet size       = 56 bytes
Telemetry rate    = 20 packets/s
```

Therefore:

```text
Data rate         = 1120 bytes/s
Raw payload rate  = 8960 bit/s
UART line rate    = 11200 bit/s
```

The UART calculation assumes standard:

```text
8 data bits
1 start bit
1 stop bit
```

per transmitted byte.

### Candidate communication rates

| Baud Rate | Capacity / Required Rate | Preliminary Status |
| --------: | -----------------------: | ------------------ |
|      9600 |                    0.86× | Marginal           |
|     19200 |                    1.71× | Sufficient         |
| **38400** |                **3.43×** | **Sufficient**     |
|     57600 |                    5.14× | Sufficient         |
|    115200 |                   10.29× | Sufficient         |

A preliminary baseline of **38.4 kbps UART** provides comfortable bandwidth while avoiding unnecessary over-specification.

The final telemetry rate and physical RF link will be selected during the avionics and communication stages.

---

# 10. Preliminary Telemetry Packet

The planned telemetry frame contains information required for flight-state monitoring and post-flight analysis.

The preliminary packet includes:

```text
Sync
Packet type
Payload length
Sequence number
Timestamp
Vehicle state
Altitude
Pressure
Temperature
Acceleration X/Y/Z
Gyroscope X/Y/Z
Battery measurement
Fault flags
CRC
```

The packet architecture is intentionally designed to support:

* Packet synchronization
* Sequence tracking
* Corruption detection
* Flight-state identification
* Sensor monitoring
* Fault reporting
* Ground-station visualization
* Post-flight telemetry replay

The final packet format will be implemented during the telemetry and embedded-software stages.

---

# 11. Preliminary Sampling Requirements

The initial sensor and system sampling targets are:

| Parameter            | Target Rate |
| -------------------- | ----------: |
| IMU                  |      200 Hz |
| Pressure             |       50 Hz |
| Temperature          |       10 Hz |
| Battery monitoring   |       10 Hz |
| Telemetry            |       20 Hz |
| Mission data logging |     ~100 Hz |

These values are preliminary requirements and will be refined after the actual sensors and processor architecture are selected.

---

# 12. Engineering Requirements Established

Stage 1 establishes the following preliminary requirements for the next design stages.

### Geometry

```text
Maximum diameter       ≈ 100 mm
Overall length         ≈ 800 mm
Target mass            ≈ 1.6 kg
```

### Aerodynamics

```text
Nominal analysis speed = 250 m/s
Analysis envelope      = 50–300 m/s
Maximum analysis Mach  ≈ 0.94 at 300 m/s / 5 km
Preliminary Cd         = 0.30
Reference area         = 0.007854 m²
```

### Structural loading

```text
Nominal 250 m/s drag       ≈ 90.20 N
Nominal design axial load  ≈ 135.30 N
Maximum envelope design load
                           ≈ 194.83 N
```

The final structural loads will be updated after CFD produces a geometry-dependent drag estimate.

### Electrical

```text
Preliminary average current = 217 mA @ 3.3 V
Preliminary power           ≈ 0.72 W
Design energy estimate      ≈ 1.07 Wh
```

### Telemetry

```text
Packet size       = 56 bytes
Telemetry rate    = 20 Hz
Required UART rate ≈ 11.2 kbps
Preferred baseline = 38.4 kbps
```

---

# 13. Files in This Stage

```text
01_Python_MATLAB/
│
├── README.md
│
├── main_analysis.py
├── atmosphere.py
├── aerodynamics.py
├── mass_budget.py
├── power_budget.py
└── telemetry_budget.py
```

### Script responsibilities

| File                  | Purpose                                       |
| --------------------- | --------------------------------------------- |
| `main_analysis.py`    | Overall preliminary vehicle calculation       |
| `atmosphere.py`       | ISA atmospheric properties                    |
| `aerodynamics.py`     | Mach, dynamic pressure, drag and design loads |
| `mass_budget.py`      | Mass allocation and margin                    |
| `power_budget.py`     | Preliminary electrical power/energy budget    |
| `telemetry_budget.py` | Packet bandwidth and UART requirement         |

---

# 14. Engineering Limitations

The results in this stage are intentionally treated as **preliminary engineering estimates**.

Important limitations include:

### Aerodynamic coefficient

The value:

```text
Cd = 0.30
```

is an initial assumed value.

It will be replaced/refined using the geometry developed in CAD and subsequently evaluated using CFD.

### Structural loading

The 1.5 load factor is a preliminary design assumption.

Actual structural loading will depend on:

* aerodynamic pressure distribution
* vehicle geometry
* angle of attack
* fin configuration
* dynamic effects
* mounting conditions
* manufacturing characteristics

### Mass

The mass budget is an allocation rather than a measured hardware mass.

Actual values will be obtained after CAD and hardware definition.

### Power

The current values are preliminary subsystem estimates.

Final power consumption will depend on the selected:

* STM32 device
* sensors
* microSD hardware
* regulators
* telemetry hardware
* operating modes

### Telemetry

The UART calculation represents the local serial interface bandwidth requirement.

It does **not** by itself establish the achievable RF range or communication link margin.

RF link-budget analysis will be performed later.

---

# 15. Stage 1 Outcome

Stage 1 has established the first quantitative engineering baseline for AEROSENSE-01.

The project now has preliminary values for:

* Atmospheric environment
* Velocity envelope
* Mach number
* Dynamic pressure
* Aerodynamic drag
* Structural design load
* Mass budget
* Mass margin
* Electrical power
* Energy requirement
* Telemetry bandwidth
* Sampling rates
* Preliminary system requirements

These calculations provide the numerical inputs for the next stage.

---

# 16. Transition to Stage 2 — CAD

The next stage is:

## **CAD — Vehicle Architecture & Mechanical Integration**

The CAD model will not be created as a visually attractive standalone body.

It will be driven by the engineering requirements established here.

The CAD design will integrate:

* Outer aerodynamic body
* Nose geometry
* Stabilizing fins
* Internal avionics volume
* PCB mounting provisions
* Sensor mounting locations
* Battery location
* Telemetry/electronics space
* Internal structural supports
* Access/service interfaces
* Cable routing provisions
* Manufacturing/3D-print constraints

The resulting geometry will subsequently become the input for:

**CAD → CFD → Structural Analysis → KiCad → Manufacturing → Embedded Software → ESP32 Ground System → Telemetry → Validation**

---

## Stage 1 Status

**STATUS: COMPLETE**

The Python preliminary analysis successfully establishes a coherent engineering baseline for AEROSENSE-01.

**Next:** Stage 2 — **CAD / Mechanical & Avionics Integration**
