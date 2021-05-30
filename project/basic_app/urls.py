
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
app_name = 'basic_app'
urlpatterns = [
    
    path('signup/',views.register,name='register'),
    path('login/',views.user_login,name='user_login'),
    path("password_reset", views.password_reset_request, name="password_reset"),
    

]
