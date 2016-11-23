from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'menu/$', views.menu, name='menu'),
	url(r'user_regist/$', views.user_regist, name='user_regist'),
	url(r'user_regist_comp/$', views.user_regist_comp, name='user_regist_comp'),
	url(r'eq_search/$', views.eq_search, name='eq_search'),
	url(r'logout/$', views.logout, name='logout'),
	url(r'eq_list/$', views.eq_list, name='eq_list'),
	url(r'eq_disposal_search/$', views.eq_disposal_search, name='eq_disposal_search'),
	url(r'eq_disposal/$', views.eq_disposal, name='eq_disposal'),
	url(r'eq_restore_search/$', views.eq_restore_search, name='eq_restore_search'),
 	url(r'eq_restore/$', views.eq_restore, name='eq_restore'),
	url(r'eq_regist/$', views.eq_regist, name='eq_regist'),
	url(r'eq_comp/$', views.eq_regist_comp, name='eq_comp'),
]
