from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'menu/$', views.menu, name='menu'),
	url(r'create/$', views.create, name='create'),
	url(r'user_comp/$', views.user_comp, name='user_comp'),
]
