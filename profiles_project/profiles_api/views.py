from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from .serializers import HelloSerializer

class HelloApiView(APIView):

    """ Test API view """
    serializer_class = HelloSerializer

    def get(self, request, format=None):
        """ returns a list of APIView features """
        an_apiview = [
            'Uses HTTp methods such as function(get, post, put',
            'Is similar to a traditional django view',
            'Gives you the most control over your application logic',
            'is mapped manually to URLs'
        ]

        return Response({'message':'success','an_apiview':an_apiview})

    def post(self, request):
        """ create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk=None):
        """ updates an object """
        return Response({'method':'PUT'})
    
    def patch(self, request, pk=None):
        """ handles a partial update of an object """
        return Response({'method':'PATCH'})

    def delete(self, request, pk=None):
        """ deletes an object """
        return Response({'method':'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """ Test of view set"""
    serializer_class = HelloSerializer

    def list(self, request):
        a_viewset = [
            'Uses HTTp methods such as function(get, post, put',
            'Is similar to a traditional django view',
            'Automatic maps to urls using routers',
            'is mapped manually to URLs'
        ]
        return Response({'success':True, 'a_viewset':a_viewset})
    
    def create(self, request):
        """ creates a new hello message"""
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST
            )
    
    def retrieve(self, request, pk=None):
        """ Handle getting an object by its id """
        return Response({'Http method':'GET'})

    def update(self, request, pk=None):
        """ Handle updating an object by its id """
        return Response({'Http method':'PUT'})

    def partial_update(self, request, pk=None):
        """ Handle updating part of an object by its id """
        return Response({'Http method':'PATCH'})

    def destroy(self, request, pk=None):
        """ Handle deleting an object by its id """
        return Response({'Http method':'DELETE'})