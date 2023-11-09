from django.urls import path, include
from .views import MyMessageViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r'my-message', MyMessageViewSet, 'my-message')


urlpatterns = [
    path('', include(router.urls)),
]