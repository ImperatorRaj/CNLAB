import socket

IP = "127.0.0.1"
PORT = 5655

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((IP, PORT))

filename = input("Enter the file name to send along with the path ")
file = open(filename, "r")
data = file.read()

client.send(filename.encode())
msg = client.recv(1024).decode()
print(f"[SERVER] {msg}")

client.send(data.encode())
msg = client.recv(1024).decode()
print(f"[SERVER] {msg}")

file.close()
client.close()
