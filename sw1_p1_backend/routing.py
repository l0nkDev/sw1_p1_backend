from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from sw1_p1_backend import consumers

websocket_urlpatterns = [
    path('ws/session/<session_name>', consumers.DiagramConsumer.as_asgi()),
]

application = ProtocolTypeRouter({
    'websocket': URLRouter(websocket_urlpatterns),
})
