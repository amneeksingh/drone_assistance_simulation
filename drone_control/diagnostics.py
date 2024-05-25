# diagnostics.py
import random
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def check_battery():
    """Simulate a battery level check with a random battery level percentage."""
    battery_level = random.randint(20, 100)
    logging.info(f"Battery level: {battery_level}%")
    return battery_level > 20  # True if battery is above 20%

def check_sensors():
    """Simulate checking the operational status of sensors."""
    sensors = ['GPS', 'altimeter', 'camera']
    status = {sensor: random.choice([True, False]) for sensor in sensors}
    for sensor, is_ok in status.items():
        logging.info(f"{sensor} status: {'OK' if is_ok else 'FAIL'}")
    return all(status.values())

def perform_system_check():
    """Perform a comprehensive system health check and log the diagnostics."""
    logging.info("Performing system diagnostics...")
    battery_status = check_battery()
    sensor_status = check_sensors()

    if battery_status and sensor_status:
        logging.info("All systems GO!")
        return True
    else:
        logging.error("System diagnostics failed!")
        return False

if __name__ == "__main__":
    perform_system_check()
