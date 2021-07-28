# -*- coding: utf-8 -*-
# """
# Created on Tue Dec  1 21:32:08 2020

# @author: may.shalaby
# """

from socket import *
serverName = 'DESKTOP-0E04QJ6'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = input('Input lowercase message:').encode()
clientSocket.sendto(message, (serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print (modifiedMessage)
clientSocket.close()