from django.shortcuts import render
from rest_framework.respone import Response
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
    request.user.firstname = request.data.firstname
    request.user.lastname = request.data.lastname
    request.user.phone = request.data.phone
    request.user.save()
    return Response('updated profile:' + request.user.username)
    
