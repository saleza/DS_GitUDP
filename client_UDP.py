# -*- coding: utf-8 -*-

import socket

UDP_IP = "192.168.0.202" #Adresse IP du serveur
UDP_PORT = 5005 #Port du serveur

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.settimeout(1.0)

sock.connect((UDP_IP,UDP_PORT)) #On se connecte au serveur
sock.send('cinema') #On envoi le mot clé "cinéma" au serveur

trameReponse, addr = sock.recvfrom(1024) #On reçoit la réponse venant du serveur contenant le code sur 4 octet
trameretour = bytearray(trameReponse) #On met la trame dans un tableau de 4 octet

print "Réception de la trame de réponse", trameReponse.encode("hex") #Affichage de la trame reçue en hexa

code = (trameretour[0])              #On recoit le premier octet du numéro
code = code + (trameretour[1] << 8)  #On décale le 2ème octet de 8 bits vers la gauche en lui ajoutant le numéro précèdent
code = code + (trameretour[2] << 16) #On décale le 3ème octet de 16 bits vers la gauche en lui ajoutant le numéro précédent
code = code + (trameretour[3] << 24) #On décale le 4ème octet de 24 bits vers la gauche en lui ajoutant le numéro précèdent
  
print code  #On affiche le code

