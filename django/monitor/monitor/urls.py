"""monitor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url,include
from rest_framework import routers
from django.contrib import admin
from webmonitor import views

#API REST
router = routers.DefaultRouter()

router.register(r'api/v1/registros/(?P<sensor_id>\d+)', views.RegistrosViewSet,"sensor_id")
router.register(r'api/v1/registros', views.RegistrosViewSet,"sensor_id")

router.register(r'api/v1/related', views.RelacionesViewSet,"sensor_id")

router.register(r'api/v1/sensors', views.SensoresViewSet,"sensor_id")

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', views.index, name='index'),
    url(r'^dashboard\.html$', views.dashboard, name='dashboard'),
    url(r'^dashboard$', views.index, name='index'),

    url(r'^graficas\.html$', views.graficas, name='graficas'),
    url(r'^graficas$', views.index, name='index'),

    #API Rest
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
