import socket
host= "http://intro.cristiannavarrete.com/"
port=3000

socket1=socket.socket()
#conectar con el servidor
socket1.connect((host,port))

#aquí tiene que llegar el valor desde el sensor
data="valor" #como acceder a ese valor 
socket.send(data)
valor=socket1.recv(1024)
socket1.close()
