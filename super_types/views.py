from django.shortcuts import render
from rest_framework.decorators import api_view
# Create your views here.


@api_view(['GET'])
def supers_list(request):
    if request.method == 'GET':
        
        pass
