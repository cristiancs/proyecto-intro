function graficas(){
	$('#menu li').removeClass('active');
	$('#menu li[data-action="graficas"]').addClass('active');
	$('#content').load('graficas.html',function(){
		$.each($('.Graficas-box'), function(index, val) {
			id = $(val).attr('data-id')
			generateGraph(id);
		});

	function generateGraph(id){
		$.get('http://intro.cristiannavarrete.com:8000/api/v1/registros/'+id+'/', function(data) {
			console.log(data);
			var grafica = new google.visualization.DataTable();
			grafica.addColumn('datetime','Hora')
			grafica.addColumn('number','Temperatura')

			$.each(data, function(index, val) {
				grafica.addRows([
					[new Date(val.fecha),val.valor]
				])
			});
			var chart = new google.visualization.LineChart(document.getElementById('graficas_'+id));
			chart.draw(grafica);
		});
	}
		
	});
}