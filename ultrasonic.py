from pybricks.pupdevices import UltrasonicSensor
from pybricks.parameters import Port

sensor = UltrasonicSensor(Port.F)

def distance() -> int:
    return sensor.distance()

def lights_on(brightness: int = 100):
    _ = sensor.lights.on(brightness)

def lights_off():
    _ = sensor.lights.off()
