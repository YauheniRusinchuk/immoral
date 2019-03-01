# from channels.routing import ProtocolTypeRouter, URLRouter
# from django.urls import path
# from django.conf.urls import url
# from channels.auth import AuthMiddlewareStack
# from channels.security.websocket import AllowedHostsOriginValidator, OriginValidator
# from .comsumers import VideoConsumer
#
#
# application = ProtocolTypeRouter({
#     'websocket': AllowedHostsOriginValidator(
#         AuthMiddlewareStack(
#             URLRouter(
#                 [
#                     url(r"^events/(?P<stream>\w+)/$", VideoConsumer),
#                 ]
#             )
#         )
#     )
# })
