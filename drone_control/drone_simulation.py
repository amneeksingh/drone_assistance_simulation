# drone_simulation.py
from flight_control import set_direction, set_altitude, stabilize_drone

def simulate_drone_movement():
    """Simulate drone movement based on predefined patterns."""
    flight_patterns = ['hover', 'circle', 'zigzag']
    for pattern in flight_patterns:
        if pattern == 'hover':
            stabilize_drone()
            set_altitude(10)  # Hover at 10 meters
        elif pattern == 'circle':
            set_direction(360)  # Complete a full circle
        elif pattern == 'zigzag':
            for angle in [45, -45] * 5:  # Zigzag pattern
                set_direction(angle)
        print(f"Executing {pattern} pattern.")
        stabilize_drone()  # Stabilize after each pattern

if __name__ == "__main__":
    simulate_drone_movement()
