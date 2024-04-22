# flight_control.py
def set_direction(degrees):
    """Set the drone's flight direction."""
    print(f"Changing direction by {degrees} degrees.")

def set_altitude(meters):
    """Set the drone's altitude."""
    print(f"Setting altitude to {meters} meters.")

def stabilize_drone():
    """Stabilize the drone's current position."""
    print("Stabilizing drone position.")

if __name__ == "__main__":
    set_direction(90)
    set_altitude(50)
    stabilize_drone()
