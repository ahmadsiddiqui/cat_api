from datetime import timedelta
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .serializers import RegisterSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import AccessToken
from .tokens import PersistentAPIToken

class RegisterView(generics.CreateAPIView):
	queryset = User.objects.all()
	permission_classes = (AllowAny,)
	serializer_class = RegisterSerializer
# --- FRONT END VIEWS ---
def login_view(request):
	return render(request, 'accounts/login.html')

def register_view(request):
	return render(request, 'accounts/register.html')

def token_view(request):
	return render (request, 'accounts/token.html')


class UserProfileView(APIView):
	authentication_classes = [JWTAuthentication]
	permission_classes = [IsAuthenticated]

	def get(self, request):
		return Response({
			"username": request.user.username,
			"id": request.user.id
		})


class GenerateAPITokenView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Generate the long-lived token for the logged-in user
        token = PersistentAPIToken.for_user(request.user)
        
        return Response({
            'api_token': str(token),
            'expires_at': (request.user.date_joined + token.lifetime).isoformat() 
            # Note: You can calculate precise math using datetime.now() instead
        })