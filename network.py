# Because each client socket will be set to non-blocking for receiving data, we're going
# to run into run-time exceptions when either connecting or trying to receive data (there
# won't always be data to receive when attempting to get it), so we will just simply pass
# on run-time exceptions, since it's going to occur and we just want to ignore it (by design)

import socket
import pickle


class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.setblocking(0)
        self.server = "192.168.0.136"
        self.port = 5555
        self.address = (self.server, self.port)
        self.connect()

    def connect(self):
        try:
            self.client.connect(self.address)
        except socket.error as e:
            pass

    def send(self, data):
        msg = pickle.dumps(data)  # Convert given object to bytes
        self.client.send(msg)

    def receive(self):
        try:
            data = self.client.recv(2048*8)
            return pickle.loads(data)
        except socket.error as e:
            pass

