from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from src.apps.events.consumers import NoseyConsumer

application = ProtocolTypeRouter({
    "websocket": URLRouter([
        path("", NoseyConsumer),
    ])
})
