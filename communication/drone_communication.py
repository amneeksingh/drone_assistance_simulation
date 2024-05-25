# drone_communication.py
import socket
import json
import time
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def create_drone_socket(server_ip, server_port):
    """Create a socket connection to the server."""
    try:
        drone_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        drone_socket.connect((server_ip, server_port))
        logging.info("Connection established with server at {}.".format(server_ip))
        return drone_socket
    except socket.error as e:
        logging.error("Failed to create socket: {}".format(e))
        exit()

def send_data(drone_socket, data):
    """Send sensor data serialized as JSON to the server."""
    json_data = json.dumps(data)
    try:
        drone_socket.sendall(json_data.encode('utf-8'))
        logging.info("Data sent to server.")
    except socket.error as e:
        logging.error("Failed to send data: {}".format(e))

def receive_commands(drone_socket):
    """Receive commands from the server."""
    try:
        response = drone_socket.recv(1024).decode('utf-8')
        logging.info("Received commands from server: {}".format(response))
        return response
    except socket.error as e:
        logging.error("Failed to receive data: {}".format(e))
        return None

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
            commands = receive_commands(drone_socket)
            time.sleep(5)  # Sleep for 5 seconds before next send
    except KeyboardInterrupt:
        drone_socket.close()
        logging.info("Disconnected from server.")
