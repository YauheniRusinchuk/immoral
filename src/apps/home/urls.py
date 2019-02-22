from django.urls import path
from .views import Home
from src.apps.login.views import Login

app_name = 'home'

urlpatterns = [
    path('', Home.as_view(), name='home_page'),
    path('login/', Login.as_view(), name='login_page'),
]
