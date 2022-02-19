from django.test import TestCase
from movies.models import Actor

class ActorTestCase(TestCase):
    def setUp(self):
        Actor.objects.create(name="Vikram", age=25, married=False, address="India")

    def test_Actors_can_speak(self):
        """Actors have name"""
        vikram = Actor.objects.get(name="Vikram")
        self.assertEqual(vikram.name, 'Vikram')