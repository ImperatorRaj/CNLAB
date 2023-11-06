import socket
import random
import time
loss_prob = 0.1

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '127.0.0.1'
    port = 9915

    window = 2
    frames = ['frame 0', 'frame 1', 'frame 2', 'frame 3', 'frame 4', 'frame 5']
    framesNo = 0

    server_socket.bind((host, port))
    server_socket.listen(1)

    print("server listening at: {host}:{port}")
    client_socket, client_add = server_socket.accept()

    while 1:
        send_list = ""
        for i in range(window):
            if loss_prob<random.random():
                if(framesNo+i<6):
                    send_list+=(frames[framesNo+i])+","
        print(send_list[:-1])
        client_socket.sendall(send_list[:-1].encode())
        print('Frames sent from', framesNo)
        ##time.sleep(3)
        ack = client_socket.recv(1024).decode('utf-8')
        if 'ACK' in ack:
            req = int(ack[-1])
            if(req<6):
                framesNo=req
            else:
                print("_________________ALL FRAMES SENT___________________")
                client_socket.send('FIN'.encode('utf-8'))
                client_socket.close()
                server_socket.close()
                break

    client_socket.close()
    server_socket.close()

if __name__ == '__main__':
    main()
