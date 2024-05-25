# server_communication.py
import socket
import json
import logging
from drone_control.drone_dispatch import dispatch_drone, perform_maintenance

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def create_server_socket(ip, port):
    """Create a server socket that listens for incoming connections."""
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((ip, port))
        server_socket.listen()
        logging.info("Server listening on {}:{}".format(ip, port))
        return server_socket
    except socket.error as e:
        logging.error("Failed to create server socket: {}".format(e))
        exit()

def get_initial_request(client_socket):
    """Read the initial request to determine the type of client connection."""
    try:
        initial_data = client_socket.recv(1024).decode('utf-8')
        if not initial_data:
            return None, "No data received"
        # Assuming the data includes a command type field for simplicity
        request_info = json.loads(initial_data)
        return request_info.get('command'), request_info
    except json.JSONDecodeError as e:
        logging.error("JSON decode error: {}".format(str(e)))
        return None, "Invalid JSON format"
    except Exception as e:
        logging.error("Error receiving initial request: {}".format(str(e)))
        return None, str(e)

def assistance_request_handler(client_socket, addr, data):
    """Handle incoming assistance requests and dispatch drones."""
    try:
        logging.info(f"Assistance request received from {addr}: {data}")
        # Assume data contains location
        dispatch_drone(data['location'])
        client_socket.sendall("Drone dispatched.".encode('utf-8'))
    except KeyError:
        client_socket.sendall("Location data missing.".encode('utf-8'))
    except Exception as e:
        logging.error(f"Error handling request from {addr}: {str(e)}")
    finally:
        client_socket.close()

def handle_drone_connection(client_socket):
    """Handle incoming data from a drone and send back commands."""
    try:
        while True:
            data = client_socket.recv(1024).decode('utf-8')
            if not data:
                break
            logging.info("Received data from drone: {}".format(data))
            
            # Send a command back to the drone
            command = {'action': 'adjust_altitude', 'value': 'increase'}
            json_command = json.dumps(command)
            client_socket.sendall(json_command.encode('utf-8'))
            logging.info("Sent command to drone.")
    except ConnectionResetError:
        logging.info("Connection lost with drone.")
    finally:
        client_socket.close()
        logging.info("Closed connection with drone.")

if __name__ == "__main__":
    server_ip = '192.168.1.10'
    server_port = 65432
    server_socket = create_server_socket(server_ip, server_port)
    
    while True:
        try:
            client_socket, addr = server_socket.accept()
            command, request_data = get_initial_request(client_socket)
            if command == 'request_assistance':
                assistance_request_handler(client_socket, addr, request_data)
            else:
                    handle_drone_connection(client_socket)
        except KeyboardInterrupt:
            server_socket.close()
            logging.info("Server shutdown.")
            break
