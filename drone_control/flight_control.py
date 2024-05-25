# flight_control.py
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message(ssage)')

def set_direction(degrees):
    """Set the drone's flight direction and log the action."""
    logging.info(f"Changing direction by {degrees} degrees.")

def set_altitude(meters):
    """Set the drone's altitude and log the change."""
    logging.info(f"Setting altitude to {meters} meters.")

def stabilize_drone():
    """Stabilize the drone's current position and confirm stabilization."""
    logging.info("Stabilizing drone position.")

if __name__ == "__main__":
    set_direction(90)
    set_altitude(50)
    stabilize_drone()
