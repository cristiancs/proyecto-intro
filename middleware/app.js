var express = require('express'),
passport = require('passport')
, util = require('util')
, FacebookStrategy = require('passport-facebook').Strategy
, logger = require('morgan')
, session = require('express-session')
, bodyParser = require("body-parser")
, cookieParser = require("cookie-parser")
, methodOverride = require('method-override'),
TelegramBot = require('node-telegram-bot-api')
var app = express();
var server = app.listen(3000);
var io = require('socket.io')(server);
mysql = require('mysql'),
graph = require('fbgraph');
var oldValues = {};
var config   = {};
config.token = "9H1k2EHf1NNwMZ3uwx2sy7y1lK7jqy71";
config.mysql  = {
	host     : 'intro.cristiannavarrete.com',
	user     : 'root',
	password : 'dmedel123',
	database : 'intro'
}
config.TELEGRAM_TOKEN = "161021421:AAFM9eBLhblkKv9VYr4O1ncBiNWTy7NkNfY"
config.FACEBOOK_APP_ID = "920628371347786"
config.FACEBOOK_APP_SECRET = "b0a0091ec10654ccc964a46b468b5ebd";
graph.setVersion("2.4");
graph.setAccessToken(config.FACEBOOK_APP_ID+'|'+config.FACEBOOK_APP_SECRET);

console.log("Iniciando servidor de Socket");


passport.serializeUser(function(user, done) {
	done(null, user);
});

passport.deserializeUser(function(obj, done) {
	done(null, obj);
});


//Conexión MYSQL
var connection = mysql.createConnection(config.mysql);
connection.connect();


// Telegram Bot
var bot = new TelegramBot(config.TELEGRAM_TOKEN, {polling: true});

bot.onText(/\/start/, function (msg, match) {
  var fromId = msg.from.id;
  var resp;
  console.log(msg.from);
  connection.query("SELECT id FROM telegram_users where userID = '"+fromId+"'",function(err, rows){
  	if(rows.length == 0){
  		connection.query("INSERT INTO telegram_users (userID,firstName,lastName,username) VALUES('"+fromId+"','"+msg.from.first_name+"','"+msg.from.last_name+"','"+msg.from.username+"')");
  		resp ="Haz sido registrado para recibir notificaciones de HomePI";
  	}
  	else{
  		resp ="Ya te encontrabas registrado para recibir mensajes de este Bot";
  	}
  	bot.sendMessage(fromId, resp);
  });
  
});




function verifyUpdate(){
	connection.query('SELECT sensor_id, fecha FROM registros WHERE fecha >= DATE_SUB(NOW(), INTERVAL 2 HOUR) ', function(err, rows) {
		var largo8,largo9;
		for (var i = rows.length - 1; i >= 0; i--) {
			if(rows[i].sensor_id == 8){
				largo8 = true;
			}
			if(rows[i].sensor_id == 9){
				largo9 = true;
			}
		};
		if(!largo8){
			connection.query('SELECT userID FROM registros WHERE username = "mhcristian" ', function(err, receptores) {
				bot.sendMessage(receptores[0].userID,'Hey!, el sensor 8 no ha enviado registros en las últimas 2 horas');
			});	
		}
		if(!largo9){
			connection.query('SELECT userID FROM registros WHERE username = "mhcristian" ', function(err, receptores) {
				bot.sendMessage(receptores[0].userID,'Hey!, el sensor 9 no ha enviado registros en las últimas 2 horas');
			});	
		}
	});
}

setTimeout(verifyUpdate,60*60*2);














// Use the FacebookStrategy within Passport.
//   Strategies in Passport require a `verify` function, which accept
//   credentials (in this case, an accessToken, refreshToken, and Facebook
//   profile), and invoke a callback with a user object.
passport.use(new FacebookStrategy({
	clientID: config.FACEBOOK_APP_ID,
	clientSecret: config.FACEBOOK_APP_SECRET,
	callbackURL: "http://temperatura.cristiannavarrete.com:3000/auth/facebook/callback"
},
function(accessToken, refreshToken, profile, done) {
		// asynchronous verification, for effect...
		graph.post("/oauth/access_token?client_id="+config.FACEBOOK_APP_ID+"&client_secret="+config.FACEBOOK_APP_SECRET+"&grant_type=fb_exchange_token&fb_exchange_token="+accessToken, function(err, res) {
			connection.query("INSERT INTO facebook_users (fbid,name,token) VALUES('"+profile.id+"','"+profile.displayName+"','"+res.access_token+"') ")
		});
		
		process.nextTick(function () {
			
			// To keep the example simple, the user's Facebook profile is returned to
			// represent the logged-in user.  In a typical application, you would want
			// to associate the Facebook account with a user record in your database,
			// and return that user instead.
			return done(null, profile);
		});
	}
	));


// configure Express
app.set('views', __dirname + '/views');
app.set('view engine', 'ejs');
//app.use(logger());
app.use(cookieParser());
app.use(bodyParser());
app.use(methodOverride());
app.use(session({ secret: 'keyboard cat' }));
// Initialize Passport!  Also use passport.session() middleware, to support
// persistent login sessions (recommended).
app.use(passport.initialize());
app.use(passport.session());
app.use(express.static(__dirname + '/public'));


app.get('/', function(req, res){
	res.render('index', { user: req.user });
});
app.get('/account', ensureAuthenticated, function(req, res){
	res.render('account', { user: req.user });
});

app.get('/login', function(req, res){
	res.render('login', { user: req.user });
});

// GET /auth/facebook
//   Use passport.authenticate() as route middleware to authenticate the
//   request.  The first step in Facebook authentication will involve
//   redirecting the user to facebook.com.  After authorization, Facebook will
//   redirect the user back to this application at /auth/facebook/callback
app.get('/auth/facebook',
	passport.authenticate('facebook'),
	function(req, res){
		// The request will be redirected to Facebook for authentication, so this
		// function will not be called.
	});

// GET /auth/facebook/callback
//   Use passport.authenticate() as route middleware to authenticate the
//   request.  If authentication fails, the user will be redirected back to the
//   login page.  Otherwise, the primary route function function will be called,
//   which, in this example, will redirect the user to the home page.
app.get('/auth/facebook/callback', 
	passport.authenticate('facebook', { failureRedirect: '/login' }),
	function(req, res) {
		res.redirect('/');
	});

app.get('/logout', function(req, res){
	req.logout();
	res.redirect('/');
});
app.get('/update', function(req, res){
	storage(req.query);
	res.json('Done');
});


io.on('connection', function(socket){
	console.log("Conexión Recibida");
	socket.on('register', function(data){
		storage(data);
		
	});
	socket.on('askUpdate',function(data){
		console.log('askUpdate solicitado');
		io.emit('askUpdate',data);
	})
});
var storage = function(data){
	if(data.token === config.token){
		console.log("Token Aceptado");
		// Guardamos Datos
		valor = Number(data.value);
		id = parseInt(data.id);
		if(valor == 85 && id == 8 || id == 9 && valor == 85){
			return;
		}
		//if(valor == true){ valor = 1;}
		//else if(valor == false){ valor = 0;}
		//if(typeof valor == "string") {
		//	valor = Number(valor);
		//	valor = parseInt(valor,1);
		//}
		if(typeof valor == "int" || typeof valor == "number"){
			// console.log("Guardamos")
			connection.query("INSERT INTO `intro`.`registros` (`sensor_id`, `valor`, `fecha`) VALUES ('"+id+"', ROUND('"+valor+"',2), '"+(new Date().toISOString().slice(0, 19).replace('T', ' '))+"')");
			io.emit('update',{id: data.id,valor: valor})
			actualizarThirdParty({id: data.id,valor: valor})
		}
	}
}
var actualizarThirdParty = function(data){
	console.log("Call to thirdparty",data);
	var fbIds,
		telegramIds,
		message;
	connection.query('SELECT token,fbid FROM facebook_users', function(err, rows) {
		fbIds = rows;
		connection.query('SELECT userID FROM telegram_users', function(err, rows) {
			telegramIds = rows;
			dataReady();
		});
	});
	function dataReady(){
		if(data.valor >= 39 && data.id == 8){
			if(data.valor-oldValues.id8 >= 0.5 || !oldValues.id8){
				oldValues.id8 = data.valor;
				// Notificar de temperatura de tinaja sobre 39 grados
				message = "La temperatura de la Tinaja es de "+data.valor+" °C !";
				for (var i = 0; i < fbIds.length; i++) {
					graph.post(fbIds[i].fbid + "/notifications?href=http://temperatura.cristiannavarrete.com:8000&template="+message, function(err, res) {
					});
				}; 
				for (var i = 0; i < telegramIds.length; i++) {
					bot.sendMessage(telegramIds[i].userID, message);
				}; 
			}
		}
		else if(data.id==8){
			oldValues.id8 = data.valor;
		}
		if(data.valor >= 30 && data.id == 9){
			// Notificar de temperatura de piscina sobre 30 grados
			if(data.valor-oldValues.id9 >= 0.5 || !oldValues.id9){
				oldValues.id9 = data.valor;
				message = "La temperatura de la Piscina es de "+data.valor+" °C !";
				for (var i = 0; i < fbIds.length; i++) {
					graph.post(fbIds[i].fbid + "/notifications?href=http://temperatura.cristiannavarrete.com:8000&template="+message, function(err, res) {
					});
				}; 
				for (var i = 0; i < telegramIds.length; i++) {
					bot.sendMessage(telegramIds[i].userID, message);
				}; 
			}
		}
		else if(data.id == 9){
			oldValues.id9 = data.valor;
		}
	}
}


// Simple route middleware to ensure user is authenticated.
//   Use this route middleware on any resource that needs to be protected.  If
//   the request is authenticated (typically via a persistent login session),
//   the request will proceed.  Otherwise, the user will be redirected to the
//   login page.
function ensureAuthenticated(req, res, next) {
	if (req.isAuthenticated()) { return next(); }
	res.redirect('/login')
}
