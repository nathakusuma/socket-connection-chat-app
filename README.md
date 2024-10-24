# Socket Connection Chat Application

A simple real-time chat application built with Python using socket programming. This application allows multiple clients to connect to a central server and exchange messages in a group chat environment.

## Features

- Real-time messaging
- Multiple client support
- User name registration
- Join/Leave notifications
- Environment variable configuration
- Clean disconnect handling

## Prerequisites

- Python 3.x
- python-dotenv (1.0.1 or higher)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/nathakusuma/socket-connection-chat-app.git
cd socket-connection-chat-app
```

2. Create a virtual environment:
```bash
python3 -m venv .venv
source .venv/bin/activate  # For Unix/macOS
# or
.venv\Scripts\activate  # For Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Copy `.env.example` to `.env` and modify the values.

## Usage

### Starting the Server

1. Run the server:
```bash
python server_main.py
```
The server will start and display the IP and port it's running on.

### Connecting Clients

1. Run the client in a new terminal or a new device:
```bash
python client_main.py
```

2. When prompted, enter your name to join the chat.

3. Start chatting! Messages will be broadcast to all connected clients.

4. To quit, type 'quit' or use Ctrl+C.

## Project Structure

```
socket-connection-chat-app/
├── server_main.py      # Server implementation
├── client_main.py      # Client implementation
├── requirements.txt    # Project dependencies
├── .gitignore          # List of ignored files and directories
├── .env                # Environment variables
└── .env.example        # Example of environment variables
```

## Features Details

### Server (`server_main.py`)
- Handles multiple client connections using threading
- Manages client name registration
- Broadcasts messages to all connected clients
- Handles client disconnections gracefully
- Sends join/leave notifications

### Client (`client_main.py`)
- Connects to server using configured host/port
- Supports username registration
- Runs separate threads for sending and receiving messages
- Handles server disconnection gracefully
- Provides clean exit functionality

## Environment Variables

- `SERVER_IP`: The IP address of the server
- `SERVER_PORT`: The port number for the server

## Error Handling

The application includes error handling for:
- Failed server connections
- Client disconnections
- Invalid messages
- Network interruptions