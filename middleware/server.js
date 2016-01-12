// Requeridos
var server = require('http').createServer();
var io     = require('socket.io')(server);
var mysql  = require('mysql');

// Configuración
var config   = {}
config.token = "9H1k2EHf1NNwMZ3uwx2sy7y1lK7jqy71";
config.mysql  = {
  host     : 'intro.cristiannavarrete.com',
  user     : 'root',
  password : 'dmedel123',
  database : 'intro'
}

console.log("Iniciando servidor de Socket");
//Conectamos con MYSQL
var connection = mysql.createConnection(config.mysql);
connection.connect();
// Detectar conexiones a la DB
io.on('connection', function(socket){
	console.log("Conexión Recibida");
	socket.on('register', function(data){
		// console.log("Solicitud de registro Recibida");
		// console.log(data);
		if(data.token === config.token){
			// console.log("Token Aceptado");
			// Guardamos Datos
			valor = data.value;
			if(valor == true){ valor = 1;}
			else if(valor == false){ valor = 0;}
			if(typeof valor == "string") {
				valor = Number(valor);
			}
			console.log(typeof valor);
			if(typeof valor == "int" || typeof valor == "number"){
				// console.log("Guardamos")
				connection.query("INSERT INTO `intro`.`registros` (`sensor_id`, `valor`, `fecha`) VALUES ('"+data.id+"', '"+valor+"', '"+(new Date().toISOString().slice(0, 19).replace('T', ' '))+"')");
				socket.emit('update',{id: data.id,valor: data.valor})
			}
			
		}
	});
	socket.on('askUpdate',function(data){
		console.log('askUpdate solicitado');
		socket.emit('askUpdate');
	})
});
server.listen(3000);