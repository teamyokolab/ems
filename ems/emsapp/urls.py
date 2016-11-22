from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'menu/$', views.menu, name='menu'),
	url(r'create/$', views.create, name='create'),
	url(r'user_comp/$', views.user_comp, name='user_comp'),
	url(r'eq_search/$', views.eq_search, name='eq_search'),
	url(r'logout/$', views.logout, name='logout'),
]
