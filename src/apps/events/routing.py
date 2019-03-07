from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from src.apps.events.consumers import PostConsumer, CommentCunsumer

application = ProtocolTypeRouter({
    "websocket": URLRouter([
        path('author/<slug:slug>/id<int:pk>/', CommentCunsumer),
        path("", PostConsumer),
    ])
})
