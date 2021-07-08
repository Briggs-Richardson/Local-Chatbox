import socket
from _thread import *
import pickle

# Change to your personal specs
server = "192.168.0.136"
port = 5555
MAX_CONNECTIONS = 5


clients = []

# Set up socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Bind the socket to the ip and port
try:
    s.bind((server, port))
except socket.error as e:
    print(e)

s.listen(MAX_CONNECTIONS)
print("Server started. Waiting for connections")


# Sends a message to all clients except the sender
def send_all_clients(data, client_sender):
    for client in clients:
        if client != client_sender:
            client.send(data)


def threaded_client(conn):
    while True:
        try:
            data = conn.recv(2048)
            if not data:
                break
            else:
                #msg = pickle.loads(data)
                #print("received: ", data)
                #print("Sending to all other clients")
                send_all_clients(data, conn)
        except:
            break

    print("Lost connection")
    conn.close()


while True:
    connection, address = s.accept()   # Accept any incoming connections
    print("Connected to", address)
    clients += [connection]

    start_new_thread(threaded_client, (connection,))


