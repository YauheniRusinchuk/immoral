from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from src.apps.events.consumers import PostConsumer, CommentCunsumer
from channels.auth import AuthMiddlewareStack

application = ProtocolTypeRouter({
    "websocket": AuthMiddlewareStack(
            URLRouter([
            path('author/<slug:slug>/id<int:pk>/', CommentCunsumer),
            path("", PostConsumer),
        ])
    )
})
