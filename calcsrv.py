import socket
import mathop


# TCP PORT TO BE USED 15000
HOST = "192.168.23.11"  # The server ip address
PORT = 15000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            print('Received on server: ', repr(data))
            # LIST STRUCTURE: MATH OPERATION, X, Y
            recv_data_list = data.decode().split(' ')
            if recv_data_list[0] == "1":
                math_result = mathop.sum(int(recv_data_list[1]), int(recv_data_list[2]))
            if recv_data_list[0] == "2":
                math_result = mathop.sub(int(recv_data_list[1]), int(recv_data_list[2]))
            if recv_data_list[0] == "3":
                math_result = mathop.div(int(recv_data_list[1]), int(recv_data_list[2]))
            if recv_data_list[0] == "4":
                math_result = mathop.mult(int(recv_data_list[1]), int(recv_data_list[2]))
            data_to_send = f"{str(math_result)}"
            if not data_to_send:
                break
            conn.sendall(data_to_send.encode())
