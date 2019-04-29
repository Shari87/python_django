import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import  reverse
from ..models import Dog
from ..serializers import DogSerializer

# Initialize the client app
client = Client()

class GetAllDogsTest(TestCase):
    """Test module for GET ALL Dogs API"""
    def setUp(self):
        Dog.objects.create(
            id=1, env='venv', tests='dog_tests', name='Dollar', age=3, breed='Bull Dog', color='Black', status='True')
        Dog.objects.create(
            id=2, env='venv', tests='dog_tests', name='Rookie', age=1, breed='Gradane', color='Brown',status='True')
        Dog.objects.create(
            id=3, env='venv', tests='dog_tests', name='Casper', age=1, breed='Labrador', color='Black',status='True')
        Dog.objects.create(
            id=4, env='venv', tests='dog_tests', name='Ricky', age=1, breed='German Shepherd', color='Brown',status='True')

    def test_get_all_puppies(self):
        # get API response
        response = client.get(reverse('get_post_dogs'))
        # get data from db
        dogs = Dog.objects.all()
        serializer = DogSerializer(dogs, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetSingleDogTest(TestCase):
    """Test module for GET SINGLE DOG API"""

    def setUp(self):
        self.dollar = Dog.objects.create(
            id=1, env='venv', tests='dog_tests', name='Dollar', age=3, breed='Bull Dog', color='Black',status='True')
        self.rookie = Dog.objects.create(
            id=2, env='venv', tests='dog_tests', name='Rookie', age=1, breed='Gradane', color='Brown',status='True')
        self.casper = Dog.objects.create(
            id=3, env='venv', tests='dog_tests', name='Casper', age=4, breed='Labrador', color='Black',status='True')
        self.ricky = Dog.objects.create(
            id=4, env='venv', tests='dog_tests', name='Ricky', age=5, breed='German Shepherd', color='Brown',status='True')

    def test_get_valid_single_dog(self):
        response = client.get(
            reverse('get_delete_update_dog', kwargs={'pk': self.ricky.pk}))
        dog = Dog.objects.get(pk=self.ricky.pk)
        serializer = DogSerializer(dog)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_dog(self):
        response = client.get(
            reverse('get_delete_update_dog', kwargs={'pk': 100}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class CreateNewDogTest(TestCase):
    """Test module for inserting a new dog"""

    def setUp(self):
        self.valid_payload = {
            'id': 5,
            'env':'venv',
            'tests':'dog_tests',
            'name': 'Romeo',
            'age': 8,
            'breed':'Golden Retriever',
            'color':'Brown',
            'status':'True'
        }

        self.invalid_payload = {
            'id': 5,
            'env': 'venv',
            'tests': 'dog_tests',
            'name': '',
            'age': 8,
            'breed': 'Golden Retriever',
            'color': 'Brown',
            'status': 'True'
        }

    def test_create_valid_dog(self):
        response = client.post(
            reverse('get_post_dogs'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_dog(self):
        response = client.post(
            reverse('get_post_dogs'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class UpdateSingleDogTest(TestCase):
    """Test module for updating an existing dog record"""
    def setUp(self):
        self.dollar = Dog.objects.create(
            id=1, env='venv', tests='dog_tests', name='Dollar', age=3, breed='Bull Dog', color='Black',status='True')
        self.rookie =Dog.objects.create(
            id=2, env='venv', tests='dog_tests', name='Rookie', age=1, breed='Gradane', color='Brown',status='True')
        self.valid_payload ={
            'id': 2,
            'env': 'venv',
            'tests': 'dog_tests',
            'name': 'Rookie',
            'age': 6,
            'breed': 'Pamerion',
            'color': 'White',
            'status':'True'
        }

        self.invalid_payload = {
            'id': 2,
            'env': 'venv',
            'tests': 'dog_tests',
            'name': '',
            'age': 6,
            'breed': 'German Shepherd',
            'color': 'White',
            'status':'True'
        }

    def test_valid_update_dog(self):
        response = client.put(
            reverse('get_delete_update_dog', kwargs={'pk': self.rookie.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_update_dog(self):
        response = client.put(
            reverse('get_delete_update_dog', kwargs={'pk': self.rookie.pk}),
            data=json.dumps(self.invalid_payload),
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class DeleteSinglePuppyTest(TestCase):
    """Test module for deleting an existing dog record"""
    def setUp(self):
        self.dollar = Dog.objects.create(
            id=1, env='venv', tests='dog_tests', name='Dollar', age=3, breed='Bull Dog', color='Black')
        self.rookie = Dog.objects.create(
            id=2, env='venv', tests='dog_tests', name='Rookie', age=1, breed='Gradane', color='Brown')

    def test_valid_delete_dog(self):
        response = client.delete(
            reverse('get_delete_update_dog', kwargs={'pk': self.rookie.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_dog(self):
        response = client.delete(
            reverse('get_delete_update_dog', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)