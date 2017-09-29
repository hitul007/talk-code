import socket
import threading


TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 2048  # Normally 1024, but we want fast response

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)


def connection(conn):
    data = conn.recv(BUFFER_SIZE)
    if not data: return
    print("received data:", data)
    conn.send(data)  # echo


while True:
    conn, addr = s.accept()
    print('Connection address:', addr)

    while 1:
        t = threading.Thread(target=connection, args=(conn,))
        t.start()
        break
