#!/usr/bin/python
import socket

HOST = 'localhost'
#HOST = '192.168.1.103'
PORT = 50007
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print 'Connected by', addr
while 1:
    data = conn.recv(4096)
    if not data: break
    conn.send(data)
conn.close()
