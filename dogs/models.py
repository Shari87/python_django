from django.db import models

# Create your models here.
class Dog(models.Model):
    """
    Dog model
    Defines the attributes of a Dog
    """
    id = models.IntegerField(primary_key=True)
    env = models.CharField(max_length=255)
    tests = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    breed = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    started_at = models.DateTimeField(auto_now=True)
    finished_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=255)

    def get_breed(self):
        return self.name + ' belongs to ' + self.breed + ' breed.'

    def __repr__(self):
        return self.name + ' is added.'