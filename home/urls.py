from django.urls import path, re_path
from home import views
from django.contrib.auth import views as auth_views

app_name = 'home'

urlpatterns = [

	# home main paths:

	path('', views.home, name='home'),
	path('en/', views.home_en, name='home_en'),

]