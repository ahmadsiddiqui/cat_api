from django.shortcuts import render, redirect
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import CatFact
from .serializers import CatFactSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes




def frontend_view(request):
	authentication_classes = [JWTAuthentication]
	permission_classes = [IsAuthenticated]
	return render(request,  'index.html')

def submit_view(request):
	return render(request, 'submit.html')

def catfact_list_http_response(request):
	context = {}
	if len(CatFact.objects.all()) == 0:
		context['nofacts'] = True
	context['facts'] = CatFact.objects.all()

	return render(request, "fact_list.html", context)

def dashboard_view(request):
	return render(request, 'dashboard.html')

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def catfact_List_filtered_json(request):
	
	facts = CatFact.objects.filter(author=request.user)
	serializer = CatFactSerializer(facts, many=True)
	return Response(serializer.data)

def delete_catfact_http_response(request, id):
	obj = get_object_or_404(CatFact, pk=id)
	obj.delete()
	return redirect("fact_list")

# Handles GET (List all facts) and POST (Create a new fact)

class CatFactListCreateView(generics.ListCreateAPIView):
	queryset = CatFact.objects.all()
	serializer_class = CatFactSerializer
	authentication_classes = [JWTAuthentication]
	permission_classes = [IsAuthenticated]

# Handles GET (Read one), PUT/PATCH (Update), and DELETE (Destroy)
class CatFactDetailView(generics.RetrieveUpdateDestroyAPIView):
	queryset = CatFact.objects.all()
	serializer_class = CatFactSerializer
	authentication_classes = [JWTAuthentication]
	permission_classes = [IsAuthenticated]

class RandomCatFactView(APIView):
	authentication_classes = [JWTAuthentication]
	permission_classes = [IsAuthenticated]
	def get(self, request):
		# order_by('?') randomly sorts the queryset, and .first() grabs the top one
		random_fact	 = CatFact.objects.order_by('?').first()
		
		if not random_fact:
			return Response({"detail": "No facts available."}, status=status.HTTP_404_NOT_FOUND)
			
		serializer = CatFactSerializer(random_fact)
		return Response(serializer.data) 

