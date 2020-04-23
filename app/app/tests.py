from django.test import TestCase

from app.calc import *

class CalcTests(TestCase):

    def test_add_numbers(self):
        """
        Test that two numbers area added together
        """
        self.assertEqual(add(3,8), 11)

    def test_substract_numbers(self):
        """Test that values are substract and returned"""
        self.assertEqual(substract(8,1), 7)
