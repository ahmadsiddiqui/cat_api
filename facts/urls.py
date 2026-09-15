from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
# from .views import CatFactViewSet
from facts import views

router = DefaultRouter()
# router.register(r'facts', CatFactViewSet)

urlpatterns = [
    path("facts", views.catfact_list),
    path("facts/<int:pk>", views.catfact_detail),
    path("random", views.catfact_random)
]

urlpatterns = format_suffix_patterns(urlpatterns)

#urlpatterns.append(path('', include(router.urls)))