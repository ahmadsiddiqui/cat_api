import random
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.parsers import JSONParser
from .models import CatFact
from .serializers import CatFactSerializer

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
	return render(request, 'index.html')

def submit_view(request):
	return render(request, 'submit.html')




@api_view(['GET','POST'])
@authentication_classes([]) # Removes SessionAuthentication and its CSRF check
@permission_classes([AllowAny])
@csrf_exempt
def catfact_list(request):
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
@csrf_exempt
def catfact_detail(request,pk):
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
@csrf_exempt
def catfact_random(request):
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


