from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
	path('', views.dashboard, name='dashboard'),

	#login and logout
	path('accounts/login/', auth_views.login, name='login'),
	path('accounts/logout/', auth_views.logout,  name='logout'),

	#password change
	path('accounts/password_change', auth_views.password_change, name='password_change'),
	path('accounts/password_change/done/', auth_views.password_change_done, name='password_change_done'),

	#password reset
	path('accounts/password_reset/',auth_views.password_reset, name='password_reset'),
	path('accounts/password_reset/done/', auth_views.password_reset_done, name='password_reset_done'),
	path('accounts/reset/<uidb64>/<token>/', auth_views.password_reset_confirm, name='password_reset_confirm'),
	path('accounts/reset/done/', auth_views.password_reset_complete, name='password_reset_complete'),

	#sign up
	path('sign_up', views.register, name='sign_up'),

	#Edit Profile
	path('edit/profile', views.edit, name='edit_profile')


]