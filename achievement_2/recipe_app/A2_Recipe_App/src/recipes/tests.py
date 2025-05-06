from django.test import TestCase
from .models import Recipe

class RecipeModelTest(TestCase):
    def setUpTestData():
        # Sets up non-modified objects used by all test methods
        Recipe.objects.create(
            name = 'Herbal Tea',
            ingredients = 'Herbal Tea Leaves, Honey, Hot Water',
            cooking_time = 5,
        )

    # ------------------------- Name ------------------------- 
    def test_recipe_name(self):
        # Gets recipe object to test
        recipe = Recipe.objects.get(id=1)

        # Gets metadata for "name"
        field_label = recipe._meta.get_field('name').verbose_name

        # Compares value to expected result
        self.assertEqual(field_label, 'name')

    def test_recipe_name_max_length(self):
        # Gets recipe object to test
        recipe = Recipe.objects.get(id=1)

        # Gets metadata for "name"
        max_length = recipe._meta.get_field('name').max_length

        # Compares value to expected result
        self.assertEqual(max_length, 50)

    # ------------------------- Ingredients ------------------------- #
    def test_ingredients_max_length(self):
        # Gets recipe object to test
        recipe = Recipe.objects.get(id=1)

        # Gets metadata for "ingredients"
        max_length = recipe._meta.get_field('ingredients').max_length

        # Compares value to expected result
        self.assertEqual(max_length, 255)

    # ------------------------- Cooking Time ------------------------- #
    def test_cooking_time_value(self):
        # Gets recipe object to test
        recipe = Recipe.objects.get(id=1)

        # Gets the value of "cooking_time"
        cooking_time_value = recipe.cooking_time

        # Compares value to expected result
        self.assertIsInstance(cooking_time_value, int)

    # ------------------------- Difficulty ------------------------- #
    def test_difficulty_calulation(self):
        # Gets recipe object to test
        recipe = Recipe.objects.get(id=1)

        # Compares value to expected result
        self.assertEqual(recipe.calc_difficulty(), 'Easy')
