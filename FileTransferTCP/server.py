import socket

IP = "127.0.0.1"
PORT = 5555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((IP, PORT))
server.listen()

print("[LISTENING] Server is listening")

while True:
    conn, addr = server.accept()
    print(f"[NEW CONNECTION] {addr} connected")

    filename = conn.recv(1024).decode()
    print(f"[RECV] Receiving the filename")

    file = open(f"received.txt", "w")
    conn.send("Filename received.".encode())

    data = conn.recv(1024)
    print("Content of data is ",data.decode())
    print(f"[RECV] Receiving the file data")
    file.write(data.decode())
    conn.send("File data received".encode())

    file.close()
    conn.close()
    print(f"[DISCONNECTED] {addr} disconnected")
