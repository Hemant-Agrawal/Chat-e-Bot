from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.Homepage, name="Index"),
    path('register', views.register, name="register"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
    path('get-response/', views.get_response, name="response"),
    path('ChatBot', views.ChatBot, name="ChatBot"),
]
