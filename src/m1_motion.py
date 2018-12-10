"""
An opportunity to explore how to make an EV3 Robot move.

Authors: Dave Fisher, David Mutchler, Vibha Alangar,
their colleagues, and Lucas D'Alesio.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

# -----------------------------------------------------------------------------
# DONE: 2.
#   Follow along with the lecture to run this program:
#    - Using SSH from your computer
#   When you have successfully run this program, change this _TODO_ to DONE.
# -----------------------------------------------------------------------------

import simple_rosebotics as rb
import time

def main():
    """ Calls the other functions to test/demo them. """
    go_two_seconds()


def go_two_seconds():
    # -------------------------------------------------------------------------
    # DONE: 3.
    #   Make the robot move, by using this pattern:
    #    - Turn on (start) the wheel motors.
    #    - time.sleep(2)  # Pause here, let other processes run for 2 seconds
    #    - Turn off (brake or coast) the wheel motors.
    #
    # Use the DOT trick to figure out how to start, brake and coast motors.
    # -------------------------------------------------------------------------
    left_motor = rb.LargeMotor(rb.Plug("B"))  # Constructs Motor for left wheel
    left_motor.start()
    time.sleep(2)
    left_motor.brake()


def run_test_go_inches():
    """ Tests the go_inches function. """
    # DONE: 4.  Implement this function with at least 3 calls to go_inches
    #   with various inches and speeds.


def go_inches(inches, percent_of_max_speed):
    """
    Makes the EV3 Robot move the given number of inches at the given speed.

      :type inches: float
      :type percent_of_max_speed: float  -100 to 100
    """
    # DONE: 5.  Implement and test this function.


main()
