from socket import *
serverName = 'myserver'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
message = input("Input:\n")
clientSocket.send(message.encode('utf-8'))
modifiedMessage = clientSocket.recvfrom(1024)
print(modifiedMessage.decode())
clientSocket.close()
