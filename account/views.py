from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import UserSerializer
from .models import User
from rest_framework.permissions import AllowAny,IsAuthenticated
from django.contrib.auth import authenticate
from rest_framework import viewsets, status
from rest_framework_simplejwt.tokens import RefreshToken,AccessToken

from django.db.models import Q
from rest_framework_simplejwt.authentication import JWTAuthentication



# Create your views here.
class Signup(viewsets.ViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    def create(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)  
        return Response(serializer.errors)


class Login(viewsets.ViewSet):
    """This class handle login functionality
    login with username and password or email and password"""
    permission_classes = [AllowAny]

    def create(self, request):

        username_or_email = request.data.get("username")
        password = request.data.get("password")
        if not username_or_email or not password:
            return Response(
                {"error": "Username or email and password are required."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        user_query = User.objects.filter(Q(username=username_or_email) | Q(email=username_or_email)).first()
        user = None
        if user_query:
            user = authenticate(username=user_query.username, password=password)
            

       
        if user:
            refresh = RefreshToken.for_user(user)
            access = AccessToken.for_user(user)
            serializer = UserSerializer(user)
            return Response({
                'refresh': str(refresh),
                'access': str(access),
                'message': 'Login successful.',
                'user_data': serializer.data
            }, status=status.HTTP_200_OK)

        return Response(
            {"error": "Invalid credentials."},
            status=status.HTTP_401_UNAUTHORIZED,
        )


class Logout(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    
    def create(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"message": "Logged out successfully."})
        except Exception:
            return Response({"error": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST)
