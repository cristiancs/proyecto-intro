// Jquery
// @codekit-prepend "../../bower_components/jquery/dist/jquery.min.js"
// Page
// @codekit-prepend "../../bower_components/page/page.js"
// Router
// @codekit-prepend "../../lib/js/router.js"
// Actions
// @codekit-prepend "../../lib/js/index.js"
// @codekit-prepend "../../lib/dashboard/index.js"
// @codekit-prepend "../../lib/graficas/index.js"

// Webapp Hacks
window.addEventListener("load", function() { window. scrollTo(0, 0); });
// document.addEventListener("touchmove", function(e) { e.preventDefault(); });
var body = document.documentElement;
if (body.requestFullscreen) {
  body.requestFullscreen();
} else if (body.webkitrequestFullscreen) {
  body.webkitrequestFullscreen();
} else if (body.mozrequestFullscreen) {
  body.mozrequestFullscreen();
} else if (body.msrequestFullscreen) {
  body.msrequestFullscreen();
}

var socket = io('//temperatura.cristiannavarrete.com:3000');


function notfound(){
	console.log('No existe');
}

// Socket Data
// Actualizar el último registro de temperatura
socket.on('update', function(datos){
	$('[data-id="'+datos.id+'"]').find('span').html(datos.valor);
});

//Solicitar actualizar información al servidor
function askUpdate(event){
	event.preventDefault();
	var ids = $(this).attr('data-id');
	//ids = ids.split(',');
	console.log(ids);
	//$.each(ids, function(index, val) {
	 socket.emit('askUpdate');
	//});
}