from pybricks.pupdevices import ColorSensor
from pybricks.parameters import Port
from . import constants

# Initialise colour sensors
left = ColorSensor(Port.C)
right = ColorSensor(Port.D)

# Check if either side sees white
def sees_white() -> bool:
    return sees_white_sides() != (False, False)

# Check if each side sees white
def sees_white_sides() -> tuple[bool, bool]:
    # If the left colour sensor's detected reflection value
    # is over the threshold, it is white
    l = left.reflection() > constants.WHITE_THRESHOLD
    # Same but for the right colour sensor
    r = right.reflection() > constants.WHITE_THRESHOLD
    # Return both sides individually
    return (l, r)
