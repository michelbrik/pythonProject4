import gpiozero

led = gpiozero.LED(17)
led.on()
led.sleep(1)
led.off()
led.sleep(1)


