from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Category
from .serializers import CategoriesSerializer

# Create your views here.

@api_view(['GET'])
def categories(request):
    categories = Category.objects.all()
    serializer = CategoriesSerializer(categories, many=True)
    return Response(serializer.data)


