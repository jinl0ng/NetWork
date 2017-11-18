from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print("working\n")
while 1:
    connectionSocket, addr = serverSocket.accept()
    message = connectionSocket.recvfrom(1024)
    modifiedMessage = message.decode().upper()
    connectionSocket.send(modifiedMessage.encode('utf-8'))

