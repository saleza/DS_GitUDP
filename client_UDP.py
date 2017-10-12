# -*- coding: utf-8 -*-

import socket

UDP_IP = "192.168.0.202"
UDP_PORT = 5005


sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.settimeout(1.0)

sock.connect(UDP_IP,UDP_PORT)
sock.send("cinema",UDP_IP, UDP_PORT)


trameReponse, addr = sock.recvfrom(1024)

print "Réception de la trame de réponse", trameReponse.encode("hex")

code = (float)(trameReponse[3] << 24)
code = code + (trameReponse[4] << 16)
code = code + (trameReponse[5] << 8)
code = code + 

print code

