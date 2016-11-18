from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'menu/$', views.menu, name='menu'),
	url(r'create/$', views.create, name='create'),
	url(r'user_comp/$', views.user_comp, name='user_comp'),
	url(r'eq_search/$', views.eq_search, name='eq_search'),
	url(r'logout/$', views.logout, name='logout'),
	url(r'eq_list/$', views.eq_list, name='eq_list'),
	url(r'disposal_search/$', views.disposal_search, name='disposal_search'),
	url(r'eq_disposal/$', views.eq_disposal, name='eq_disposal'),
	url(r'restore_search/$', views.restore_search, name='restore_search'),
 	url(r'eq_restore/$', views.eq_restore, name='eq_restore'),
]
