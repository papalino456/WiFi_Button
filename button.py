import usocket
import urandom
import subprocess
while True:
    n = urandom.randint(1, 10000)
    s = usocket.socket()
    s.connect(("192.168.100.98", 1234))
    s.send(bytes("n={}".format(n), "utf-8"))
    res = s.recv(1024)
    print(res.decode("utf-8"))
    s.close()
