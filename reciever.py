import usocket
import machine
import network

sta_if = network.WLAN(network.STA_IF)
if not sta_if.isconnected():
    print('connecting to network...')
    sta_if.active(True)
    sta_if.connect('HALL9000', 'ANIROC1966')
    while not sta_if.isconnected():
        pass
print('network config:', sta_if.ifconfig())

s = usocket.socket()
MYespIP= sta_if.ifconfig()[0]

actuator = machine.Pin(2,machine.Pin.OUT)

s.bind((MYespIP, 1234))
s.listen(5)
print("el servidor esta escuchando en ", sta_if.ifconfig())

while True:
    clientSocket, address = s.accept()
    print("connection from {} has been established".format(address))
    msg = clientSocket.recv(1024).decode("utf-8")
    print("el valor recibido fue: ", msg)
    clientSocket.send(bytes("Valor recivido! %s" %msg, "utf-8"))
    clientSocket.close()
    if msg == "1":
        actuator.on()
    if msg == "0":
        actuator.off()