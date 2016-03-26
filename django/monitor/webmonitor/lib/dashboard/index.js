function dashboard(){
	 $('#content').load('dashboard.html',function(){
		$('.btn-update').click(askUpdate);
		$('#menu').find('li').removeClass('active');
		$('#menu').find('[data-action="dashboard"]').addClass('active');
	 });
}