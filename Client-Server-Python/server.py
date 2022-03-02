###################  Program server  ##########################################
import socket


def server_program():
    # Preluam hostname-ul
    host = socket.gethostname()
    port = 8212  #Initializam portul

    server_socket = socket.socket()

    server_socket.bind((host, port))  # Cream legatura cu host-ul si portul

    # Stabilim cate conexiuni se pot face la server simultan
    server_socket.listen(1)
    print("Hello! Esti in asteptare de noi conexiuni :D")
    conn, address = server_socket.accept()  # Acceptam noi conexuni
    print("Ai o noua conexiune de la Marin Ioana 1082: " + str(address))
    while True:
        # Primim mesaje de la server. Nu vom putea primi pachete de date mai mare de 1024 bytes
        data = conn.recv(1024).decode()
        if not data:
            # Daca nu primim niciun mesaj, break
            break
        print("Received from marinioana1082: " + str(data))
        data = input(' -> ')
        conn.send(data.encode())  # Trimitem mesajele catre client

    conn.close()  # Inchidem conexiunea
    print("Conexiune incheiata! bye :D")


if __name__ == '__main__':
    server_program()
