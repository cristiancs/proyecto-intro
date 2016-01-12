function dashboard(){
	 $('#content').load('dashboard.html',function(){
		$('.btn-update').click(askUpdate);
	 });
}