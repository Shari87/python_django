from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Dog
from.serializers import DogSerializer


# Create your views here.
@api_view(['GET','DELETE','PUT'])
def get_delete_update_dog(request,pk):
    try:
        dog = Dog.objects.get(pk=pk)
    except Dog.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

  # get details of a single dog
    if request.method == 'GET':
        serializer = DogSerializer(dog)
        return Response(serializer.data)
    # update details of a single dog
    if request.method == 'PUT':
        serializer = DogSerializer(dog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # delete a single dog
    if request.method == 'DELETE':
        dog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def get_post_dogs(request):
    # get all dogs
    if request.method == 'GET':
        dogs = Dog.objects.all()
        serializer = DogSerializer(dogs,many=True)
        return Response(serializer.data)
    # insert a new record for a dog
    if request.method == 'POST':
        data = {
            'id' : int(request.data.get('id')),
            'env' : request.data.get('env'),
            'tests': request.data.get('tests'),
            'name': request.data.get('name'),
            'age': int(request.data.get('age')),
            'breed': request.data.get('breed'),
            'color': request.data.get('color'),
            'status':request.data.get('status')
        }
        serializer = DogSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





