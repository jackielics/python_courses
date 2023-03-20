from django.test import TestCase

# Create your tests here.
class Dog:
    def __init__(self):
        print('I am init')

    def __call__(self, *args, **kwargs):
        print('I am call')

dog=Dog()

dog()