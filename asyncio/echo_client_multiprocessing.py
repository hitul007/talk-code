import socket
import random
from multiprocessing import Pool


def send_message():
    TCP_IP = '127.0.0.1'
    TCP_PORT = 5005
    BUFFER_SIZE = 2048
    MESSAGE = str(random.randint(100000000, 9999999999))

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    s.send(MESSAGE)
    data = s.recv(BUFFER_SIZE)
    print(data)
    s.close()


send_message()
