import os
import socket
import threading
import sys
from dotenv import load_dotenv

class ChatClient:
    def __init__(self, host, port):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.is_connected = False
        try:
            self.socket.connect((host, port))
            self.is_connected = True
        except Exception as e:
            print(f"Failed to connect to server: {e}")
            sys.exit()

        self.name = None
        # Event to signal when name registration is complete
        self.name_registered = threading.Event()

    def receive_messages(self):
        """Receive and print messages from the server"""
        while True:
            try:
                message = self.socket.recv(1024).decode()
                if message == "Enter your name: ":
                    self.name = input(message)
                    self.socket.send(self.name.encode())
                    # Signal that name registration is complete
                    self.name_registered.set()
                else:
                    print(message)
            except:
                print("\nDisconnected from server")
                self.is_connected = False
                self.socket.close()
                sys.exit()

    def send_messages(self):
        """Send messages to the server"""
        # Wait for name registration before starting to send messages
        self.name_registered.wait()

        while self.is_connected:
            try:
                message = input()
                if message.lower() == 'quit':
                    self.is_connected = False
                    self.socket.close()
                    sys.exit()
                self.socket.send(message.encode())
            except:
                print("\nDisconnected from server")
                self.is_connected = False
                self.socket.close()
                sys.exit()

    def start(self):
        """Start the client with separate threads for sending and receiving"""
        receive_thread = threading.Thread(target=self.receive_messages)
        receive_thread.daemon = True
        receive_thread.start()

        send_thread = threading.Thread(target=self.send_messages)
        send_thread.daemon = True
        send_thread.start()

        # Keep main thread alive
        try:
            while self.is_connected:
                pass
        except KeyboardInterrupt:
            print("\nDisconnecting from server...")
            self.is_connected = False
            self.socket.close()
            sys.exit()


# Run client
if __name__ == "__main__":
    load_dotenv()
    ip = str(os.getenv('SERVER_IP'))
    port = int(os.getenv('SERVER_PORT'))
    print(f"IP: {ip}, PORT: {port}")
    client = ChatClient(ip, port)
    client.start()
