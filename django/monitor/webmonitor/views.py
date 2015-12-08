from django.http import HttpResponse
from django.template import RequestContext, loader
# Create your views here.
def index(request):
	template = loader.get_template('webmonitor/index.html')
	return HttpResponse(template.render())
def dashboard(request):
	template = loader.get_template('webmonitor/dashboard.html')
	return HttpResponse(template.render())