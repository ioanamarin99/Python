################################  Program client ###########################################
import socket


def client_program():
    host = socket.gethostname()  # Preluam hostname-ul
    port = 8212  # Stabilim portul

    client_socket = socket.socket()  # Instantiere
    client_socket.connect((host, port))  # Ne conectam la server
    print("Hello, ioanamarin1082, te-ai conectat la server :D")
    print("Daca doresti sa inchei convorbirea, tasteaza bye")

    message = input(" -> ")  # Preluam inputul de la client

    while message.lower().strip() != 'bye': #Cat timp inputul de client nu este "bye"
        client_socket.send(message.encode())  # Trimitem mesajul
        data = client_socket.recv(1024).decode()  # Primim raspunsul de la server

        print('Received from server: ' + data)  # Afisam in terminal

        message = input(" -> ")  # Preluam din nou inputul de la client

    client_socket.close()  # Incheiam conexiunea
    print("Ai fost deconectat! Bye :D")


if __name__ == '__main__':
    client_program()
