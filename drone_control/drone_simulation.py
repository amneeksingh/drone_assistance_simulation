# drone_simulation.py
import logging
from flight_control import set_direction, set_altitude, stabilize_drone

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def simulate_drone_movement():
    """Simulate drone movement based on predefined flight patterns with logging."""
    flight_patterns = ['hover', 'circle', 'zigzag']
    for pattern in flight_patterns:
        logging.info(f"Starting {pattern} pattern.")
        if pattern == 'hover':
            stabilize_drone()
            set_altitude(10)
        elif pattern == 'circle':
            set_direction(360)
        elif pattern == 'zigzag':
            for angle in [45, -45] * 5:
                set_direction(angle)
        stabilize_drone()  # Stabilize after each pattern
        logging.info(f"Completed {pattern} pattern.")

if __name__ == "__main__":
    simulate_drone_movement()
