from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.Homepage, name="Index"),
    path('home', views.Homepage, name="Index"),
    path('register', views.register, name="register"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
    path('get-response/', views.get_response, name="response"),
    path('ChatBot', views.ChatBot, name="ChatBot"),
    path('temp', views.temp, name="temp"),
    path('ChatRoom', views.ChatRoom, name="ChatRoom"),
    path('get-response/live/', views.live_response, name="live-response"),
]
