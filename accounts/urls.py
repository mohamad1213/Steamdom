from django.urls import path
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.loginPage, name="login"),  
	path('register/', views.registerPage, name="register"),
	path('logout/', views.logoutUser, name="logout"),
	path('reset_password/',auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html"), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_sent.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_form.html"), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_done.html"), name="password_reset_complete"),


	# path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
	# path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
	# path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
	# path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),


# 	path('lupa/', views.lupa, name="lupa"),
# 	path('lupaada/', views.lupaada, name="lupaada"),
# 	path('lupatidak/', views.lupatidak, name="lupatidak"),
# 	path('GantiPassword/', views.GantiPassword, name="GantiPassword"),
]