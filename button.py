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

button = machine.Pin(2, machine.Pin.IN)
count = 0
while True:
    if button.value() == 1:
        if count == 0:
            s = usocket.socket()
            s.connect(("192.168.100.98", 1234))
            s.send(bytes("{}".format(count), "utf-8"))
            res = s.recv(1024)
            print(res.decode("utf-8"))
            s.close()
            count = 1
            break

        if count == 1:
            s = usocket.socket()
            s.connect(("192.168.100.98", 1234))
            s.send(bytes("{}".format(count), "utf-8"))
            res = s.recv(1024)
            print(res.decode("utf-8"))
            s.close()
            count = 0
            break