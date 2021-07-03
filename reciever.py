import usocket
import machine

s = usocket.socket()
MYespIP="192.168.100.98"

actuator = machine.Pin(2,machine.Pin.OUT)

s.bind((MYespIP, 1234))
s.listen(5)
print("el servidor esta escuchando en 192.168.100.98: 1234")

while True:
    clientSocket, address = s.accept()
    print("connection from {} has been established".format(address))
    msg = clientSocket.recv(1024).decode("utf-8")
    print("el valor recibido fue: ", msg)
    clientSocket.send(bytes("Valor recivido!", "utf-8"))
    clientSocket.close()
    if msg == 1:
        actuator.on()
    if msg == 0:
        actuator.off()