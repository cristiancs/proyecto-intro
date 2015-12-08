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

//Conectamos con MYSQL
var connection = mysql.createConnection(config.mysql);
connection.connect();
// Detectar conexiones a la DB
io.on('connection', function(socket){
	socket.on('register', function(data){
		if(data.token === config.token){
			// Guardamos Datos
			connection.query("INSERT INTO `intro`.`registros` (`id`, `valor`,`, `fecha`) VALUES ('"+data.id+"', '"+data.valor+"', '"+(new Date())+"')");
			socket.emit('update',{id: data.id,valor: data.valor})
		}
	});
});
server.listen(3000);