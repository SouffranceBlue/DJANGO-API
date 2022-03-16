from http.client import BAD_REQUEST
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status 
from profiles_api import serializer

class HelloApiView(APIView):
    """ API VIEW DE PRUEBA """

    serializer_class = serializer.HelloSerializer

    def get(self,request, format= None):
        an_apiview = [
            "Usamos metodos HTTP como funciones (get, post, put, delete)",
            "Es similar a una vista tradicional de Django",
            "Nos da el mayor control sobre la logica de nuestra aplicacion",
            "Esta mapeado con los URLS",
        ]
        return Response({"mesagge":"Hello", "an_apiview": an_apiview})

    def post(self, request):
        """ Crea un mensaje con nuestro nombre """
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({"message":message})
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """ Maneja actualizar un objeto"""
        return Response({"method":'PUT'})

    def patch(self,request, pk=None):
        """Maneja la actualizacion parcial de un objeto """
        return Response({"method":'PATCH'})

    def delete(self,request,pk=None):
        return Response({"method":'DELETE'})


    
