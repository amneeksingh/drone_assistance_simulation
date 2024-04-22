# diagnostics.py
import random

def check_battery():
    """Simulate a battery level check."""
    battery_level = random.randint(20, 100)  # Random battery level percentage
    print(f"Battery level: {battery_level}%")
    return battery_level

def check_sensors():
    """Simulate checking the operational status of sensors."""
    sensors = ['GPS', 'altimeter', 'camera']
    status = {sensor: random.choice([True, False]) for sensor in sensors}
    for sensor, is_ok in status.items():
        print(f"{sensor} status: {'OK' if is_ok else 'FAIL'}")
    return status

def perform_system_check():
    """Perform a comprehensive system health check."""
    print("Performing system diagnostics...")
    battery_status = check_battery() > 20
    sensor_status = all(check_sensors().values())

    if battery_status and sensor_status:
        print("All systems GO!")
        return True
    else:
        print("System diagnostics failed!")
        return False

if __name__ == "__main__":
    perform_system_check()
