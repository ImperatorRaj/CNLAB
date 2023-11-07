import socket
import threading

IP = "127.0.0.1"
PORT = 5655

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((IP, PORT))
server.listen()

print("[LISTENING] Server is listening")

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected")

    filename = conn.recv(1024).decode()
    print(f"[RECV] Receiving the filename")

    file = open(f"received_{addr[0]}_{addr[1]}.txt", "w")
    conn.send("Filename received.".encode())

    data = conn.recv(1024)
    print(f"[RECV] Receiving the file data from {addr}")
    file.write(data.decode())
    conn.send("File data received".encode())

    file.close()
    conn.close()
    print(f"[DISCONNECTED] {addr} disconnected")

while True:
    conn, addr = server.accept()
    thread = threading.Thread(target=handle_client, args=(conn, addr))
    thread.start()
