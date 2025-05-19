# Import all the pybricks things we need
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, UltrasonicSensor
from pybricks.parameters import Direction, Port
from pybricks.tools import wait, StopWatch

# Import our things to use
from . import constants # Numbers
from . import states # States
from . import colour_sensors # Colour sensors
from . import motors # Motors
from . import util # Utilities


# Setup hub and watch
hub = PrimeHub()
watch = StopWatch()
ultrasonic = UltrasonicSensor(Port.F)


# Set motor powers
def set_motor_powers(left: int, right: int):
    motors.left.dc(left)
    motors.right.dc(right)

# States
state = states.SEARCHING
last_state = states.SEARCHING

# Main loop
while True:
    # If the state has changed since the last loop
    if state != last_state:
        print(f"\n--- Transitioned to state: {state} ---")
        # Save this loop's state to check against next round
        last_state = state

    # STATE: Searching
    if state == states.SEARCHING:
        # If the robot sees something to charge at
        # and it is close enough
        if ultrasonic.distance() <= constants.CHARGE_DISTANCE:
            watch.reset() # Reset the stopwatch
            state = states.CHARGE # Charge
        else:
            print("Turning to search...")
            set_motor_powers(-50, 50) # Rotate

    # STATE: Charge
    elif state == states.CHARGE:
        # Check if the robot sees the white line
        if colour_sensors.sees_white(): 
            print("Line detected! Stopping motors.")
            # Stop both motors
            set_motor_powers(0,0)
            ultrasonic.lights.off()
            state = states.LINE_DETECTED
        else:
            ultrasonic.lights.on(100)
            # Gradual ramp-up with a 25 min and 70 max power
            MIN_POWER = 25
            MAX_POWER = 70

            raw = watch.time() * 0.5 # Raw power
            # Make sure the power is within our minimum and maximum
            power = util.clamp(raw, MIN_POWER, MAX_POWER)
            power = int(power) # Make sure it is a whole number

            print(f"Charging with power: {power}")
            # Set both motors to drive at the power we calculated
            set_motor_powers(power, power)

    # STATE: Line detected
    elif state == states.LINE_DETECTED:
        print("Backing up after line detection...")
        set_motor_powers(-50, -50) # Set both motors to go backwards
        # Don't go back to searching until we are no longer on the line
        if not colour_sensors.sees_white():
            state = states.SEARCHING
