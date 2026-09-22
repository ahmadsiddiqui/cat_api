from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
# from .views import CatFactViewSet
from facts import views
from .views import CatFactListCreateView, CatFactDetailView, RandomCatFactView

router = DefaultRouter()
# router.register(r'facts', CatFactViewSet)

urlpatterns = [

    # path("facts", views.ProtectedDataView.catfact_list.as_view()),
    # path("facts/<int:pk>", views.ProtectedDataView.catfact_detail.as_view()),
    # path("random", views.ProtectedDataView.catfact_random.as_view()),
    path("facts/",CatFactListCreateView.as_view(), name='facts'),
    path('facts/<int:pk>/', CatFactDetailView.as_view(), name='fact_detail'),
    path('random/', RandomCatFactView.as_view(), name='random_fact'),

    
]

urlpatterns = format_suffix_patterns(urlpatterns)
handler404 = 'facts.views.custom_404_redirect'

#urlpatterns.append(path('', include(router.urls)))