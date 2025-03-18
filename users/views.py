from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from users.models import User
from users.serializers import UserSerializer

@api_view(['POST'])
def create_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            "status": True, 
            "message": "User Created", 
            "data": serializer.data
            }, status=status.HTTP_201_CREATED)
    
    return Response({
        "status": False, 
        "message": "User not Created", 
        "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_users(request):
    users = User.objects.all()
    if not users.exists():
        return Response({
            "status": False, 
            "message": "No users found"
            }, status=status.HTTP_404_NOT_FOUND)
    
    serializer = UserSerializer(users, many=True)
    return Response({
        "status": True, 
        "message": "Users Retrieved", 
        "data": serializer.data
        }, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_user(request, user_id):
    user = User.objects.filter(pk=user_id).first()
    if not user:
        return Response({
            "status": False, 
            "message": "User not found"
            }, status=status.HTTP_404_NOT_FOUND)

    serializer = UserSerializer(user)
    return Response({
        "status": True, 
        "message": "User Found", 
        "data": serializer.data
        }, status=status.HTTP_200_OK)

@api_view(['PUT'])
def update_user(request, user_id):
    user = User.objects.filter(pk=user_id).first()
    if not user:
        return Response({
            "status": False, 
            "message": "User not found"
            }, status=status.HTTP_404_NOT_FOUND)
    
    serializer = UserSerializer(user, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            "status": True, 
            "message": "User Updated", 
            "data": serializer.data
            }, status=status.HTTP_200_OK)

    return Response({
        "status": False, 
        "message": "User not Updated", 
        "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_user(request, user_id):
    user = User.objects.filter(pk=user_id).first()
    if not user:
        return Response({
            "status": False, 
            "message": "User not found"
            }, status=status.HTTP_404_NOT_FOUND)
    
    user.delete()
    return Response({
        "status": True, 
        "message": "User Deleted"
        }, status=status.HTTP_204_NO_CONTENT)

