from django.urls import path
from .views import Events

app_name = 'events'

urlpatterns = [
    path('', Events.as_view(), name='events_page'),
]
