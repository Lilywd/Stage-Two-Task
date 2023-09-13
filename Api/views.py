from django.shortcuts import render
from .models import Person
from .serializers import PersonSerializer
from rest_framework import status,viewsets
from rest_framework.response import Response
# Create your views here.

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def create(self, request):
        person = Person(
            name=request.data['name'], 
            

        )

        # Validate the parameters.
       
        person.save()
        return Response(PersonSerializer(person).data)

    def retrieve(self, request, pk):
        person = Person.objects.get(pk=pk)
        return Response(PersonSerializer(person).data)

    def update(self, request, pk):
        person = Person.objects.get(pk=pk)
        person.name = request.data['name']
    
        person.save()
        return Response(PersonSerializer(person).data)

    def delete(self, request, pk):
        person = Person.objects.get(pk=pk)
        person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
