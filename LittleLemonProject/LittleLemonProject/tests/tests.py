from django.test import TestCase
from ...reservations.models import *

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        # Verify the __str__ method
        self.assertEqual(str(item), "IceCream 80 100")