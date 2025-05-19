from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction

# Initialise motors
left = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right = Motor(Port.B)

# Set motor powers
def set_powers(left_: int, right_: int):
    left.dc(left_)
    right.dc(right_)
