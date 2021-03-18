from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Category, Subcategory, Ad
from .serializers import CategoriesSerializer, AdSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

# Create your views here.

@api_view(['GET'])
def categories(request):
    categories = Category.objects.all()
    serializer = CategoriesSerializer(categories, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def post_ad(request):
    owner = request.user
    title = request.data['title']
    category = request.data['category']
    category = Category.objects.get(id=category)
    ##subcategory = request.data['subcategory']
    ##subcategory = Subcategory.objects.get(id=subcategory)
    location = request.data['location']
    description = request.data['description']
    image1 = request.data['image1']
    image2 = request.data['image2']
    phone = request.data['phone']
    ad = Ad.objects.create(
        owner=owner,
        title=title, 
        category=category, 
        ##subcategory=subcategory,
        location=location,
        description=description,
        image1=image1,
        image2=image2,
        phone=phone
    )
    return Response('created ad: ' + ad.title)

@api_view(['GET'])
def myads(request):
    ads = Ad.objects.get(owner=request.user)
    serializer = AdSerializer(ads, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def ads(request, category_id):
    ads = Ad.objects.filter(category=category_id)
    serializer = AdSerializer(ads, many=True)
    return Response(serializer.data)
