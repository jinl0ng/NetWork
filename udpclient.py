from socket import *
serverName = '39.108.6.163'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = input('Input')
clientSocket.sendto(message, (serverName, serverPort))
modifiedMessage, serverAddres = clientSocket.recvfrom(2048)
print (modifiedMessage)
clientSocket.close()
