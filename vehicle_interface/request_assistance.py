# request_assistance.py
import requests
import json

def send_assistance_request(vehicle_data):
    """Send an automated request for assistance to the system's server."""
    server_url = "http://localhost:5000/assistance_request"
    headers = {'Content-Type': 'application/json'}
    response = requests.post(server_url, data=json.dumps(vehicle_data), headers=headers)
    print(f"Response from server: {response.text}")

if __name__ == "__main__":
    vehicle_data = {
        'vehicle_id': 'VH123456',
        'problem': 'engine_overheat',
        'location': {'latitude': 34.0522, 'longitude': -118.2437}
    }
    send_assistance_request(vehicle_data)
