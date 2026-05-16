# ESP32 Smart Motion Lighting System

---

#  Deutsche Version

## Projektbeschreibung

Dieses Projekt demonstriert ein intelligentes adaptives Beleuchtungssystem mit einem ESP32 Mikrocontroller, einem LDR-Lichtsensor, einem PIR-Bewegungssensor und PWM-Technologie.

Das System analysiert kontinuierlich die Umgebungshelligkeit und Bewegungen in Echtzeit.

### Funktionsweise

- Bei ausreichendem Umgebungslicht bleiben die LEDs ausgeschaltet.
- Wenn die Umgebung dunkel wird, aktiviert das System die Beleuchtung.
- Sobald eine Bewegung erkannt wird, schalten die LEDs auf maximale Helligkeit.
- Nach der Bewegung bleiben die LEDs für 10 Sekunden hell.
- Danach wechseln die LEDs automatisch in einen gedimmten Energiesparmodus.

Die rote und grüne LED sind parallel an GPIO14 angeschlossen und werden gemeinsam gesteuert.

---

# Verwendete Komponenten

| Komponente | Beschreibung |
|---|---|
| ESP32 DevKit V1 | Hauptcontroller |
| LDR Sensor | Misst die Lichtintensität |
| PIR Bewegungssensor | Erkennt Bewegungen |
| Rote LED | Beleuchtungsausgang |
| Grüne LED | Beleuchtungsausgang |
| PWM Steuerung | Dynamische Helligkeitsregelung |
| Breadboard & Jumper Kabel | Verbindung der Komponenten |

---

# Pin-Verbindungen

| Komponente | ESP32 Pin |
|---|---|
| LDR Sensor AO | GPIO34 |
| PIR Sensor OUT | GPIO27 |
| LEDs | GPIO14 |
| Interne blaue LED | GPIO2 |
| VCC | 3V3 / VIN |
| GND | GND |

---

# Systemlogik

| Situation | Verhalten |
|---|---|
| Helle Umgebung | LEDs AUS |
| Dunkle Umgebung ohne Bewegung | LEDs gedimmt |
| Dunkle Umgebung mit Bewegung | LEDs maximale Helligkeit |
| Nach Bewegung | LEDs bleiben 10 Sekunden hell |
| Danach | Rückkehr zum Energiesparmodus |

---

# MicroPython Code

```python
from machine import Pin, ADC, PWM
import time

# LEDs connected together on GPIO14
leds = PWM(Pin(14))
leds.freq(1000)

# Internal ESP32 blue LED
internal_led = Pin(2, Pin.OUT)

# LDR light sensor on GPIO34
light_sensor = ADC(Pin(34))
light_sensor.atten(ADC.ATTN_11DB)
light_sensor.width(ADC.WIDTH_12BIT)

# PIR motion sensor on GPIO27
motion_sensor = Pin(27, Pin.IN)

# Keep LEDs bright for 10 seconds after motion
motion_timeout = 10
last_motion_time = 0

print("Smart Motion Lighting System Running...")

while True:

    light_value = light_sensor.read()
    motion = motion_sensor.value()

    print("Light:", light_value)
    print("Motion:", motion)

    # Bright environment
    if light_value < 1800:

        leds.duty(0)
        internal_led.off()

        print("Bright Environment -> LEDs OFF")

    # Dark environment
    else:

        if motion == 1:

            last_motion_time = time.time()

            leds.duty(1023)
            internal_led.on()

            print("Motion Detected -> LEDs HIGH")

        else:

            elapsed = time.time() - last_motion_time

            if elapsed < motion_timeout:

                leds.duty(1023)
                internal_led.on()

                print("Waiting Timeout -> LEDs STILL ON")

            else:

                leds.duty(250)
                internal_led.on()

                print("No Motion -> LEDs DIM")

    print("---------------------------")

    time.sleep(0.5)
```

---

# Praktische Anwendungen

Dieses intelligente Beleuchtungssystem kann verwendet werden in:

- Smart Homes
- Intelligente Straßenbeleuchtung
- Sicherheitsbeleuchtung
- Solarbeleuchtungssysteme
- Erneuerbare Energiesysteme
- Garagen
- Korridore
- Lagerhäuser
- Energieeffiziente Automatisierungsprojekte

Das System hilft dabei, elektrische Energie effizient zu sparen und Beleuchtung nur bei Bedarf zu aktivieren.

---

---

#  English Version

## Project Description

This project demonstrates an intelligent adaptive lighting system using an ESP32 microcontroller, an LDR light sensor, a PIR motion sensor, and PWM technology.

The system continuously analyzes ambient light intensity and movement in real time.

### System Operation

- When enough ambient light is available, the LEDs remain OFF.
- When the environment becomes dark, the system activates the lighting.
- As soon as motion is detected, the LEDs switch to maximum brightness.
- After motion is detected, the LEDs stay bright for 10 seconds.
- After the timeout period, the LEDs automatically return to a dim energy-saving mode.

The red and green LEDs are connected in parallel on GPIO14 and operate together.

---

# Used Components

| Component | Description |
|---|---|
| ESP32 DevKit V1 | Main controller |
| LDR Sensor | Measures light intensity |
| PIR Motion Sensor | Detects movement |
| Red LED | Lighting output |
| Green LED | Lighting output |
| PWM Control | Dynamic brightness control |
| Breadboard & Jumper Wires | Component connections |

---

# Pin Connections

| Component | ESP32 Pin |
|---|---|
| LDR Sensor AO | GPIO34 |
| PIR Sensor OUT | GPIO27 |
| LEDs | GPIO14 |
| Internal Blue LED | GPIO2 |
| VCC | 3V3 / VIN |
| GND | GND |

---

# System Logic

| Situation | Behavior |
|---|---|
| Bright environment | LEDs OFF |
| Dark environment without motion | LEDs dimmed |
| Dark environment with motion | LEDs maximum brightness |
| After motion | LEDs stay bright for 10 seconds |
| After timeout | Return to energy-saving mode |

---

# MicroPython Code

```python
from machine import Pin, ADC, PWM
import time

# LEDs connected together on GPIO14
leds = PWM(Pin(14))
leds.freq(1000)

# Internal ESP32 blue LED
internal_led = Pin(2, Pin.OUT)

# LDR light sensor on GPIO34
light_sensor = ADC(Pin(34))
light_sensor.atten(ADC.ATTN_11DB)
light_sensor.width(ADC.WIDTH_12BIT)

# PIR motion sensor on GPIO27
motion_sensor = Pin(27, Pin.IN)

# Keep LEDs bright for 10 seconds after motion
motion_timeout = 10
last_motion_time = 0

print("Smart Motion Lighting System Running...")

while True:

    light_value = light_sensor.read()
    motion = motion_sensor.value()

    print("Light:", light_value)
    print("Motion:", motion)

    # Bright environment
    if light_value < 1800:

        leds.duty(0)
        internal_led.off()

        print("Bright Environment -> LEDs OFF")

    # Dark environment
    else:

        if motion == 1:

            last_motion_time = time.time()

            leds.duty(1023)
            internal_led.on()

            print("Motion Detected -> LEDs HIGH")

        else:

            elapsed = time.time() - last_motion_time

            if elapsed < motion_timeout:

                leds.duty(1023)
                internal_led.on()

                print("Waiting Timeout -> LEDs STILL ON")

            else:

                leds.duty(250)
                internal_led.on()

                print("No Motion -> LEDs DIM")

    print("---------------------------")

    time.sleep(0.5)
```

---

# Practical Applications

This intelligent lighting system can be used in:

- Smart homes
- Smart street lighting
- Security lighting
- Solar-powered lighting systems
- Renewable energy systems
- Garages
- Corridors
- Warehouses
- Energy-efficient automation projects

The system helps reduce electrical energy consumption and activates lighting only when needed.

---

## Ahmad Azroun
Renewable Energy Manager | IoT & Smart Energy Systems Developer
