# server_communication.py
import socket
import json

def create_server_socket(ip, port):
    """Create a server socket that listens for incoming connections."""
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((ip, port))
    server_socket.listen()
    print("Server listening on", ip, ":", port)
    return server_socket

def handle_drone_connection(client_socket):
    """Handle incoming data from a drone and send back commands."""
    try:
        while True:
            data = client_socket.recv(1024).decode('utf-8')
            if not data:
                break
            print("Received data from drone:", data)
            
            # Send a command back to the drone
            command = {'action': 'adjust_altitude', 'value': 'increase'}
            json_command = json.dumps(command)
            client_socket.sendall(json_command.encode('utf-8'))
            print("Sent command to drone.")
    except ConnectionResetError:
        print("Connection lost with drone.")
    finally:
        client_socket.close()

if __name__ == "__main__":
    server_ip = '192.168.1.10'
    server_port = 65432
    server_socket = create_server_socket(server_ip, server_port)
    
    while True:
        client_socket, addr = server_socket.accept()
        print("Connected to drone at", addr)
        handle_drone_connection(client_socket)
