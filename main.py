from machine import Pin, ADC, PWM
import time

leds = PWM(Pin(14))
leds.freq(1000)

internal_led = Pin(2, Pin.OUT)

light_sensor = ADC(Pin(34))
light_sensor.atten(ADC.ATTN_11DB)
light_sensor.width(ADC.WIDTH_12BIT)

motion_sensor = Pin(27, Pin.IN)

motion_timeout = 10
last_motion_time = 0

print("Smart Motion Lighting System Running...")

while True:
    light_value = light_sensor.read()
    motion = motion_sensor.value()

    print("Light:", light_value)
    print("Motion:", motion)

    if light_value < 1800:
        leds.duty(0)
        internal_led.off()
        print("Bright Environment -> LEDs OFF")

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