from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .serializers import RegisterSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication

class RegisterView(generics.CreateAPIView):
	queryset = User.objects.all()
	permission_classes = (AllowAny,)
	serializer_class = RegisterSerializer
# --- FRONT END VIEWS ---
def login_view(request):
	return render(request, 'accounts/login.html')

def register_view(request):
	return render(request, 'accounts/register.html')


class UserProfileView(APIView):
	authentication_classes = [JWTAuthentication]
	permission_classes = [IsAuthenticated]

	def get(self, request):
		return Response({
			"username": request.user.username,
			"id": request.user.id
		})