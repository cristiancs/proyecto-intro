from socketIO_client  import SocketIO
from temperaturaAgua import *
from dht22 import*
import time

socketIO = SocketIO("intro.cristiannavarrete.com",3000)
while True:
        tagua= readDatos()
        tdht22= tempdht22()
        hdht22= humedht22()
        print tagua
        print tdht22
        print hdht22
        socketIO.emit("register", tagua)
        print "enviado ds18b20"
        socketIO.emit("register", tdht22)
        print "enviado temperatura dht22"
        socketIO.emit("register", hdht22)
        print "enviado humedad dht22"
        socketIO.wait(900)
