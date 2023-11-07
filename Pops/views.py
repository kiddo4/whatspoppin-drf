from django.http import JsonResponse
from .models import Pop
from .seializers import PopSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def pop_list(request, format=None):
    # get pops
    if request.method == 'GET':
        # get all pops
        pops = Pop.objects.all()
        # serialize the pops
        serializer = PopSerializer(pops, many=True)
        # return json
        return Response(serializer.data)
    
    # post pops
    if request.method == 'POST':
        serializer = PopSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def pop_detail(request, id, format=None):

    try:
        # get pop with id
        pop = Pop.objects.get(pk=id)
    except Pop.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    # get condintion
    if request.method == 'GET':
        serializer = PopSerializer(pop)
        return Response(serializer.data)
    # put pod condition
    elif request.method == 'PUT':
        serializer = PopSerializer(pop, data=request.data)
        if serializer.is_valid():
            serializer.save
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # delete pod condition
    elif request.method == 'DELETE':
        pop.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    