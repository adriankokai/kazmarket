from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET'])
def current_user(request):
    """
    returns user
    """
    print('currnet')
    serializer = UserSerializer(request.user)
    return Response(serializer.data)

@api_view(['POST'])
def update_profile(request):
    request.user.first_name = request.data["first_name"]
    request.user.last_name = request.data["last_name"]
    request.user.email = request.data["email"]
    request.user.save()
    return Response('updated profile:' + request.user.username)
    
