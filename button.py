import usocket
button = machine.Pin(2, machine.Pin.IN)
while True:
    if button.value == 1:
        n = 1
        s = usocket.socket()
        s.connect(("192.168.100.98", 1234))
        s.send(bytes("n={}".format(n), "utf-8"))
        res = s.recv(1024)
        print(res.decode("utf-8"))
        s.close()