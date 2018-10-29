from socket import *
import threading
from time import sleep

client_count = 0
connection_list = []
address_list = []
f1 = open("login.txt", "r")
f2 = open("passwords.txt", "r")
email_ids = f1.readlines()
passwords = f2.readlines()
working_emails = []
response = 0
final_text = ""


def new_client_conn(conn1, address1):
    global client_count, connection_list, working_emails, address_list, response
    client_count += 1
    connection_list.append(conn1)
    address_list.append(address1[0])
    print(connection_list)
    d = conn1.recv(2048).decode()
    response += 1
    working_emails.append(d)
    print(working_emails)


def send_data():
    send_index_start = 0
    global connection_list, client_count, final_text, working_emails, final_text, response
    increment = int(len(email_ids) / client_count)
    for conn2 in connection_list:
        send_data1 = b""
        send_data2 = b""
        for i in range(send_index_start, send_index_start + increment):
            send_data1 += email_ids[i].encode()
            send_data2 += passwords[i].encode()
        send_index_start += increment
        conn2.send(send_data1)
        conn2.send(send_data2)
        print(send_data1)
    while response != client_count:
        True
    final_text = "".join(working_emails)
    print("dd", final_text)


def start_server():
    server_socket = socket()
    server_socket.bind(('', 800))
    print("server started")
    server_socket.listen(4)
    while True:
        conn, address = server_socket.accept()
        threading._start_new_thread(new_client_conn, (conn, address))
