# real_time_analyzer.py
import json
import logging 
from data_collector import collect_sensor_data

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def analyze_data(data):
    """Analyze the data for any anomalies or specific conditions."""
    if data['temperature'] > 35:
        alert = "High temperature warning!"
    elif data['pressure'] < 950:
        alert = "Low pressure alert!"
    elif data['humidity'] < 25:
        alert = "Low humidity alert!"
    else:
        alert = "All readings are within normal parameters."
    return alert

def real_time_analysis():
    """Perform real-time analysis on streaming sensor data."""
    try:
        while True:
            data = collect_sensor_data()
            analysis_result = analyze_data(data)
            logging.info(f"Analysis at {data['timestamp']}: {analysis_result}")
    except KeyboardInterrupt:
        logging.info("Real-time analysis stopped.")

if __name__ == "__main__":
    real_time_analysis()
