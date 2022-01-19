# Echo client program
import socket


HOST = '192.168.23.11'    # The remote host
PORT = 15000              # The same port as used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        mop = input("""MATH OPERATIONS
    1 - SUM
    2 - SUB
    3 - DIV
    4 - MULT
    5 - Exit program
    Input: """)
        if mop == "1":
            usinp = input("Input X and Y: ")
        if mop == "2":
            usinp = input("Input X and Y: ")
        if mop == "3":
            usinp = input("Input X and Y: ")
        if mop == "4":
            usinp = input("Input X and Y: ")
        if mop == "5":
            break
        data_to_send = f"{mop} {usinp}".encode()
        s.sendall(data_to_send)
        data = s.recv(1024)
        print('Math result received by server: ', data.decode())
