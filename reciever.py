import usocket

s = usocket.socket()
MYespIP="192.168.100.98"

s.bind((MYespIP, 1234))
s.listen(5)
print("el servidor esta escuchando en 192.168.100.98: 1234")

while True:
    clientSocket, address = s.accept()
    print("connection from {} has been established".format(address))
    msg = clientSocket.recv(1024)
    print(msg.decode("utf-8"))
    clientSocket.send(bytes("Hola desde el server!", "utf-8"))
    clientSocket.close()