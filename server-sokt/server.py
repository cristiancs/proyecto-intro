import SocketServer

#crear servidor para correr socket 

class MiHandler(SocketServer.baseRequestHandler):
	#se llama en cada conceccion
	def handler(self):
		#valores
		self.data= self.request.recv(1024)# bits
		# aqui trabajo valores segun quiera
		print "data recibido" seld.data
		self.request.send(int(self.data)) #or str
#crear server
def main():
	host="http://intro.cristiannavarrete.com/"
	port=3000

	server1= SocketServer.TPCServer((host,port),MiHandler)
	server1.serve_forever() # anda para siempre
