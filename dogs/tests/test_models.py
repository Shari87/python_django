from django.test import TestCase
from ..models import Dog


class DogTest(TestCase):
    """ Test module for Puppy model """

    def setUp(self):
        Dog.objects.create(
            id=1, env='venv',tests='dog_tests',name='Dollar', age=3, breed='Bull Dog', color='Black')
        Dog.objects.create(
            id=2, env='venv',tests='dog_tests',name='Rookie', age=1, breed='Gradane', color='Brown')

    def test_dog_breed(self):
        dog_dollar = Dog.objects.get(name='Dollar')
        dog_rookie = Dog.objects.get(name='Rookie')
        self.assertEqual(
            dog_dollar.get_breed(), "Dollar belongs to Bull Dog breed.")
        self.assertEqual(
            dog_rookie.get_breed(), "Rookie belongs to Gradane breed.")

