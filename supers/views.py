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
        type_param = request.query_params.get('type')

        if type_param:
            if type_param != 'hero' and type_param != 'villain':
                return Response(f'Error {type_param} is invalid', status=status.HTTP_400_BAD_REQUEST)
            supers = Super.objects.filter(super_type__type = type_param) 
            serializer = SuperSerializer(supers, many=True)
            return Response(serializer.data)
        else:
            heroes = Super.objects.filter(super_type__type = 'hero')
            villains = Super.objects.filter(super_type__type = 'villain')
            heroes_serializer = SuperSerializer(heroes, many=True)
            villains_serializer = SuperSerializer(villains, many=True)
            return Response({
                'heroes': heroes_serializer.data,
                'villains': villains_serializer.data
            })

    elif request.method == 'POST':
        serializer = SuperSerializer(data=request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def supers_detail(request, pk):
    super = get_object_or_404(Super, pk=pk)
    if request.method == 'GET':
        serializer = SuperSerializer(super)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = SuperSerializer(super, data=request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        super.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
