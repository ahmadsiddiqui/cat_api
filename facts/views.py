from django.shortcuts import render, redirect
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import CatFact
from .serializers import CatFactSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication



# class CatFactViewSet(viewsets.ModelViewSet):
# 	queryset = CatFact.objects.all()
# 	serializer_class = CatFactSerializer
# 	permission_classes = [IsAuthenticatedOrReadOnly]

# 	@action(detail=False, methods=['get'])
# 	def random(self, request):
# 		count = self.queryset.count()
# 		if count == 0:
# 			return Response({"error":"No facts available"}, status=404)

# 		random_index = random.randint(0, count-1)
# 		fact=self.queryset[random_index]
# 		serializer = self.get_serializer(fact)
# 		return Response(serializer.data)

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

def delete_catfact_http_response(request, id):
	obj = get_object_or_404(CatFact, pk=id)
	obj.delete()
	return redirect("fact_list")
'''
	@api_view(['GET','POST'])

	# @authentication_classes([]) # Removes SessionAuthentication and its CSRF check
	# @permission_classes([AllowAny])
	# @csrf_exempt

def catfact_list(self, request):
	if request.method == "GET":
		cat_facts = CatFact.objects.all()
		serializer = CatFactSerializer(cat_facts, many = True)
		return JsonResponse(serializer.data, safe = False)
	elif request.method == "POST":
		#data = JSONParser().parse(request)
		serializer = CatFactSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status=201)
		return JsonResponse(serializer.errors, status=400)

@api_view(['GET','PUT','DELETE'])

# @csrf_exempt

def catfact_detail(self, request,pk):
	try:
		fact = CatFact.objects.get(pk=pk)
	except CatFact.DoesNotExist:
		return HttpResponse(status=404)

	if request.method == "GET":
		serializer = CatFactSerializer(fact)
		return JsonResponse(serializer.data)
	elif request.method == "PUT":
		data = JSONParser().parse(request)
		serializer = CatFactSerializer(fact, data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data)
		return JsonReposne(serializer.errors, status=400)
	elif request.method == "DELETE":
		fact.delete()
		return HttpResponse(status=204)

@api_view(['GET'])
# @authentication_classes([SessionAuthentication, BasicAuthentication])
# @permission_classes([IsAuthenticated])
# @csrf_exempt
def catfact_random(self, request):
	cat_facts = CatFact.objects.all()
	if request.method == "GET":
		count = cat_facts.count()
		if count==0:
			return HttpResponse("Error: No cat facts found",status=404)

		random_index = random.randint(0, count-1)
		fact = cat_facts[random_index]
		serializer = CatFactSerializer(fact)
		return JsonResponse(serializer.data)
	return JsonReposne(serializer.errors, status=400) 
'''
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

