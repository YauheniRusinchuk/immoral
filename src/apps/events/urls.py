from django.urls import path
from .views import Events, EventDetail

app_name = 'events'

urlpatterns = [
    path('', Events.as_view(), name='events_page'),
    path('<slug:slug>/', EventDetail.as_view(), name='strem_page')
]
