from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views


urlpatterns=[
#url(r'^login/$', views.user_login,name='login'),
url(r'^login/$',auth_views.login,name='login'),
url(r'^logout/$',auth_views.logout,name='logout'),
url(r'^logout_then_login/$',auth_views.logout_then_login,name='logout_then_login'),
url(r'^$',views.dashboard,name='dashboard'),
url(r'^register/$',views.register,name='register'),
url(r'^edit/$',views.edit,name='edit'),
]