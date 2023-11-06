import socket

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '127.0.0.1'
    port = 9915

    try:
        client_socket.connect((host,port))
        frame = 0
        window = 2
        while(1):
            recv_data = client_socket.recv(1024).decode()

            recv_data = recv_data.split(",")
            print(recv_data)

            if len(recv_data)==window and recv_data != ['FIN']:
                print("Recieved Frame ", frame, ":", recv_data)
                send_ack = "ACK-" + str(frame+window)
                client_socket.send(send_ack.encode())
                frame+=window
            elif recv_data == ['FIN']:
                print("_______________ALL FRAMES RECIEVED________________")
                client_socket.close()
                break
            else:
                print("All Frames Not Recieved...")
                send_nak = "NAK-"+str(frame)
                client_socket.send(send_nak.encode('utf-8'))

        client_socket.close()
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()
