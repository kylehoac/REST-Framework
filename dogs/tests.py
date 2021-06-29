from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Dog

class DogTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(username='testuser1', password='pass')
        testuser1.save()

        test_dogs = Dog.objects.create(
            user = testuser1,
            name = 'Dog',
            breed = "poodle",
            description = "woof",
        )
        test_dogs.save()

    def test_dogs_content(self):
        dog = Dog.objects.get(id=1)
        actual_user = str(dog.user)
        actual_name = str(dog.name)
        actual_breed = str(dog.breed)
        actual_description = str(dog.description)

        expected_user = 'testuser1'
        expected_name = 'Dog'
        expected_breed = 'poodle'
        expected_description = 'woof'

        assert actual_user == expected_user
        assert actual_name == expected_name
        assert actual_breed == expected_breed
        assert actual_description == expected_description