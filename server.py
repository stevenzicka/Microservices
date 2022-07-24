import socket
import threading

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

highest_temps_fahrenheit = {
    "Alaska": 100,
    "Arizona": 128,
    "California": 134,
    "Colorado": 115,
    "Florida": 108,
    "Hawaii": 100,
    "Illinois": 117,
    "Maine": 105,
    "Montana": 117,
    "Nevada": 125,
    "New York": 108,
    "Oregon": 119,
    "Texas": 120,
    "Washington": 120
}


def handle_client(conn, addr):
    print(f"[NEW CONNECTION {addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)

            if msg == DISCONNECT_MESSAGE:
                break

            """Check temp dictionary for highest temp"""
            highest_temp = 0
            for i in highest_temps_fahrenheit:
                if msg == i:
                    highest_temp = highest_temps_fahrenheit[i]

            print(f"[{addr}] {msg}")
            temp_return = str(highest_temp)
            conn.send(temp_return.encode(FORMAT))

    conn.close()


def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


print("[STARTING] server is starting...")
start()






