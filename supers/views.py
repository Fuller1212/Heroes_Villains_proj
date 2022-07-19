from rest_framework.decorators import api_view
from rest_framework.response import Response
from supers.models import Super
from supers.serializers import SuperSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404

# Create your views here.


@api_view(['GET', 'POST'])
def supers_list(request):
    if request.method == 'GET':
        heroes = Super.objects.filter(super_type_id = 1)
        villains = Super.objects.filter(super_type_id = 2)
        hero_or_villain = request.query_params.get('type')
        supers = Super.objects.all()
        
        if hero_or_villain:
            supers = supers.filter(super_type__type = hero_or_villain) 
            serializer = SuperSerializer(supers, many=True)
            return Response(serializer.data)
        else:
            heroes_serializer = SuperSerializer(heroes, many=True)
            villains_serializer = SuperSerializer(villains, many=True)
            custom_response = {
                'heroes': heroes_serializer.data,
                'villains': villains_serializer.data
            }         
            return Response(custom_response)

    elif request.method == 'POST':
        serializer = SuperSerializer(data=request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def supers_detail(request, pk):
    supers = get_object_or_404(Super, pk=pk)
    if request.method == 'GET':
        serializer = SuperSerializer(supers)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = SuperSerializer(supers, data=request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        supers.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
