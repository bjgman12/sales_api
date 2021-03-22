from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Orders

class BlogTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(username='testuser1', password='pass')
        testuser1.save()

        test_post = Posts.objects.create(
            owner = testuser1,
            specail_instructions = 'Make it Blue and Red',
            price = 9.99
        )
        test_post.save()

    def test_order_content(self):
        order = Posts.objects.get(id=1)
        actual_owner = str(post.owner)
        actual_specail_instructions = str(post.specail_instructions)
        actual_price = str(post.price)
        self.assertEqual(actual_author, 'testuser1')
        self.assertEqual(actual_title, 'GasGo')
        self.assertEqual(actual_price, 9.99')