import random
from rest_framework import viewsets
from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import CatFact
from .serializers import CatFactSerializer

class CatFactViewSet(viewsets.ModelViewSet):
	queryset = CatFact.objects.all()
	serializer_class = CatFactSerializer

	@action(detail=False, methods=['get'])
	def random(self, request):
		count = self.queryset.count()
		if count == 0:
			return Response({"error":"No facts available"}, status=404)

		random_index = random.randint(0, count-1)
		fact=self.queryset[random_index]
		serializer = self.get_serializer(fact)
		return Response(serializer.data)

def frontend_view(request):
	return render(request, 'index.html')
