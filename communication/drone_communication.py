# drone_communication.py
import socket
import json
import time

def create_drone_socket(server_ip, server_port):
    """Create a socket connection to the server."""
    drone_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    drone_socket.connect((server_ip, server_port))
    return drone_socket

def send_data(drone_socket, data):
    """Send sensor data serialized as JSON to the server."""
    json_data = json.dumps(data)
    drone_socket.sendall(json_data.encode('utf-8'))

def receive_commands(drone_socket):
    """Receive commands from the server."""
    response = drone_socket.recv(1024).decode('utf-8')
    return response

if __name__ == "__main__":
    server_ip = '192.168.1.10'  # Server IP address
    server_port = 65432  # Server port number
    drone_socket = create_drone_socket(server_ip, server_port)

    try:
        while True:
            # Simulated sensor data
            sensor_data = {
                'temperature': 55,
                'pressure': 101.3,
                'location': {'latitude': 34.0522, 'longitude': -118.2437}
            }
            send_data(drone_socket, sensor_data)
            print("Data sent to server.")

            # Receiving commands from the server
            commands = receive_commands(drone_socket)
            print("Received commands from server:", commands)
            
            time.sleep(5)  # Sleep for 5 seconds before next send
    except KeyboardInterrupt:
        drone_socket.close()
        print("Disconnected from server.")
