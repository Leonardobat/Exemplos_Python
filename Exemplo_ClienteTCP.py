#! /bin/env/python
# -*- coding: utf-8 -*-
""" Model of a TCP Client.

    This file has a generic implementation of a simple TCP Client.
    :Author: Leonardo B.
"""
from socket import socket

TCP_Data = ("", 20305)
sock = socket()
sock.connect(TCP_Data)
print("Starting")
sock.send(b"HELLO")
print(sock.recv(2048))
sock.send(b"08:af:e6:90:8a:f1")
print(sock.recv(2048))
sock.send(b"OK")
while True:
    a = input("Mensagem: ")
    if a == "":
        b = sock.recv(2048)
        print(b)
    if a == "exit":
        sock.close()
        exit()
    else:
        sock.send(bytes(a, "ASCII"))
        print(sock.recv(2048))
