"""
URL configuration for cat_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
	https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
	1. Add an import:  from my_app import views
	2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
	1. Add an import:  from other_app.views import Home
	2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
	1. Import the include() function: from django.urls import include, path
	2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from facts.views import (
	frontend_view, 
	submit_view, 
	catfact_list_http_response, 
	delete_catfact_http_response
	)
from rest_framework_simplejwt.views import (
	TokenObtainPairView,
	TokenRefreshView,
)
from accounts.views import RegisterView

urlpatterns = [
	path('admin/', admin.site.urls),
	path('api/', include('facts.urls')),
	path('', include('accounts.urls')),
	path('', frontend_view, name='home'),
	path('submit/',submit_view, name='submit'),
	path('register/', RegisterView.as_view(), name='register'),
	path("fact_list",catfact_list_http_response, name="fact_list"),
	#path("facts/delete/<int:id>", delete_catfact_http_response),
	path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
	path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
	
]
