from django.urls import path
from . import views

app_name=('userauth')
urlpatterns = [
    path('', views.home, name='home'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
]