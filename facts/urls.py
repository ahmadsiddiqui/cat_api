from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CatFactViewSet

router = DefaultRouter()
router.register(r'facts', CatFactViewSet)

urlpatterns = [
    path('', include(router.urls)),
]