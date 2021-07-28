# -*- coding: utf-8 -*-
# """
# Created on Tue Dec  1 21:44:51 2020

# @author: may.shalaby
# """

from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('DESKTOP-0E04QJ6', serverPort))
print ("The server is ready to receive")
while 1:
    message, clientAddress = serverSocket.recvfrom(2048)
    modifiedMessage = message.upper()
    serverSocket.sendto(modifiedMessage, clientAddress)