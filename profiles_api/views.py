from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions


class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer


    def get(self, request, format=None):
        """Returns a list of APIView features"""

        an_apiview = [
            'Uses HTTP methods as functions (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Mensagem de teste!', 'an_apiview': an_apiview})

    def post (self, request):
        """Criando mensagem de HelloApiView"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            age = serializer.validated_data.get('age')
            message = f'Nome {name} e idade {age}'
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put (self, request, pk=None):
        """Update a object"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Update a partial part of object"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Delete a' object"""
        return Response({'method': 'DELETE'})



class HelloViewSet(viewsets.ViewSet):
    """Test of the viewset"""

    serializer_class = serializers.HelloSerializer

    def list(self, request):

        a_viewset = [
        'Uses actions (list, create, retrieve, update, partial_update)',
        'Automatically maps to URLS using Routers',
        'Provides more functionality with less code',
        ]

        return Response({'message': 'Hello!', 'a_viewset': a_viewset})

    def create (self, request):
        """Create new hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            age = serializer.validated_data.get('age')
            message = f'Nome {name} idade {age}'
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def retrieve (self, request, pk=None):
        """Return obj by ID"""
        return Response({'http_method': 'GET'})

    def update (self, request, pk=None):
        """Return updated object by ID"""
        return Response({'http_method': 'PUT'})

    def partial_update (self, request, pk=None):
        """Return partial updated object by ID"""
        return Response({'http_method': 'PATCH'})

    def destroy (self, request, pk=None):
        """Destroy a obj"""
        return Response({'http_method': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creanting and updating profiles"""

    serializer_class = serializers.UserProfilerSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)   
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('id', 'name', 'email',)


class UserLoginApiView (ObtainAuthToken):
    """creating user token"""
    
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
    