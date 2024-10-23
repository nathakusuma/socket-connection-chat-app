import socket
import threading


class ChatServer:
    def __init__(self, host='localhost', port=2323):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        self.clients = {}  # Dictionary to store client connections and their names
        print(f"Server started on {host}:{port}")

    def broadcast(self, message, sender=None):
        """Send message to all clients except the sender"""
        for client in self.clients:
            if client != sender:
                try:
                    client.send(message)
                except:
                    self.remove_client(client)

    def handle_client(self, client_socket, client_address):
        """Handle individual client connection"""
        # Request and store client name
        client_socket.send("Enter your name: ".encode())
        client_name = client_socket.recv(1024).decode().strip()
        self.clients[client_socket] = client_name

        # Broadcast welcome message
        welcome_message = f"{client_name} joined the chat!".encode()
        self.broadcast(welcome_message, client_socket)

        while True:
            try:
                message = client_socket.recv(1024)
                if message:
                    # Broadcast message with client name
                    formatted_message = f"{client_name}: {message.decode()}".encode()
                    self.broadcast(formatted_message, client_socket)
                else:
                    self.remove_client(client_socket)
                    break
            except:
                self.remove_client(client_socket)
                break

    def remove_client(self, client_socket):
        """Remove client and broadcast their departure"""
        if client_socket in self.clients:
            client_name = self.clients[client_socket]
            del self.clients[client_socket]
            client_socket.close()
            departure_message = f"{client_name} left the chat!".encode()
            self.broadcast(departure_message)

    def start(self):
        """Start the server and accept client connections"""
        while True:
            client_socket, client_address = self.server_socket.accept()
            print(f"Connected with {client_address}")

            # Start new thread for client
            client_thread = threading.Thread(
                target=self.handle_client,
                args=(client_socket, client_address)
            )
            client_thread.daemon = True
            client_thread.start()


# Run server
if __name__ == "__main__":
    server = ChatServer()
    server.start()
