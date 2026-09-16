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
    path("random", views.catfact_random),
    path("fact_list",views.catfact_list_http_response, name="fact_list"),
    path("facts/delete/<int:id>", views.delete_catfact_http_response),
]

urlpatterns = format_suffix_patterns(urlpatterns)

#urlpatterns.append(path('', include(router.urls)))