# data_collector.py
import random
import time
from datetime import datetime

def collect_sensor_data():
    """Simulate collecting sensor data from the drone."""
    sensor_data = {
        'temperature': random.randint(-10, 40),  # Temperature in Celsius
        'pressure': random.randint(900, 1100),   # Atmospheric pressure in hPa
        'humidity': random.randint(20, 90),      # Humidity percentage
        'location': (random.uniform(-180, 180), random.uniform(-90, 90)),  # Random lat-long coordinates
        'timestamp': datetime.now().isoformat()  # Current timestamp
    }
    return sensor_data

def save_data(sensor_data):
    """Simulate saving data to a local or remote database."""
    print(f"Data collected at {sensor_data['timestamp']}: {sensor_data}")

def data_collection_cycle(interval=5):
    """Continuous data collection cycle."""
    try:
        while True:
            data = collect_sensor_data()
            save_data(data)
            time.sleep(interval)  # Wait for the next cycle
    except KeyboardInterrupt:
        print("Data collection stopped.")

if __name__ == "__main__":
    data_collection_cycle()
