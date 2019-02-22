from django.urls import path, include
from .views import Home
from src.apps.login.views import Login
from src.apps.registration.views import Registration

app_name = 'home'

urlpatterns = [
    path('', Home.as_view(), name='home_page'),
    path('login/', Login.as_view(), name='login_page'),
    path('registration/', Registration.as_view(), name='registration_page'),
    path('accounts/', include('django.contrib.auth.urls')),
]
