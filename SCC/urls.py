from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from home import views

urlpatterns = [

    path('admin-superuser/', admin.site.urls),

    path('', include('home.urls')),

    # password reset paths: 
	
    
	#path('accounts/password_reset/',
    #     auth_views.PasswordResetView.as_view(),
    #     name='password_reset'),
    
    #path('accounts/password_reset_done/',
    #     auth_views.PasswordResetDoneView.as_view(),
    #     name='password_reset_done'),
    
    #path('accounts/password_reset_confirm/<uidb64>/<token>/',
    #     auth_views.PasswordResetConfirmView.as_view(),
    #     name='password_reset_confirm'),
    
    #path('accounts/password_reset_complete/',
    #     auth_views.PasswordResetCompleteView.as_view(),
    #     name='password_reset_complete'),

    #path('recover/<signature>/', views.recover_done,
    #    name='password_reset_sent'),
    #path('recover/', views.recover, name='password_reset_recover'),
    #path('reset/done/', views.reset_done, name='password_reset_done'),
    #path('reset/<token>/', views.reset,
    #    name='password_reset_reset'),

]
