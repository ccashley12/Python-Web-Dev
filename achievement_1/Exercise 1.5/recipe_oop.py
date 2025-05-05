class Recipe:
    def __init__(self, name, cooking_time):
        self.name = name
        self.ingredients = []
        self.cooking_time = cooking_time
        self.difficulty = None
    
    #GETS recipe name
    def get_name(self):
        return self.name
    
    #SETS recipe name
    def set_name(self, name):
        self.name = name

    #SETS class variable to store ALL ingredients
    all_ingredients = set()

    #GETS ingredients list
    def get_ingredients(self):
        return self.ingredients
    
    #ADDS ingredients to recipe
    def add_ingredients(self, *ingredients):
        for ingredient in ingredients:
            self.ingredients.append(ingredient)

            self.update_all_ingredients()

    #SEARCH for an ingredient
    def search_ingredient(self, ingredient):
        return ingredient in self.ingredients
    
    #UPDATE list of ALL ingredients
    def update_all_ingredients(self):
        for ingredient in self.ingredients:
            Recipe.all_ingredients.add(ingredient)

    #GETS recipe cooking time
    def get_cooking_time(self):
        return self.cooking_time
    
    #SETS recipe cooking time
    def set_cooking_time(self, cooking_time):
        self.cooking_time = cooking_time

    #CALCULATES recipe difficulty
    def calc_difficulty(self):
        if self.cooking_time < 10 and len(self.ingredients) < 4:
            self.difficulty = "Easy"
        elif self.cooking_time < 10 and len(self.ingredients) >= 4:
            self.difficulty = "Medium"
        elif self.cooking_time >= 10 and len(self.ingredients) < 4:
            self.difficulty = "Intermediate"
        elif self.cooking_time >= 10 and len(self.ingredients) >= 4:
            self.difficulty = "Hard"
    
    #GETS recipe difficulty
    def get_difficulty(self):
        if not self.difficulty:
            self.calc_difficulty()
        return self.difficulty
    
    #STRING Representation
    def __str__(self):
        return f"Recipe: {self.name}\nIngredients: {', '.join(self.ingredients)}\nCooking Time (in minutes): {self.cooking_time}\nDifficulty: {self.get_difficulty()}\n"
    
#SEARCH for recipe with specific ingredient
def recipe_search(data, ingredient):
    for recipe in data:
        if recipe.search_ingredient(ingredient):
            print(recipe)

#Int obj "Drip Coffee"
coffee = Recipe("Drip Coffee", 5)
coffee.add_ingredients("Ground Coffee", "Water", "Cream")
print(coffee)

#Int obj "Focaccia"
focaccia = Recipe("Focaccia Bread", 240)
focaccia.add_ingredients("All Purpose Flour", "Active Dry Yeast", "Salt", "Sugar", "Water", "Olive Oil")
print(focaccia)

#Int obj "Tea"
tea = Recipe("Herbal Tea", 5)
tea.add_ingredients("Herbal Tea", "Water", "Honey")
print(tea)

#Int obj "Guacamole"
guac = Recipe("Guacamole", 15)
guac.add_ingredients("Avocado", "White Onion", "Fresh Jalapeno", "Cilantro", "Salt", "Garlic Powder", "Paprika", "Cumin", "Black Pepper")
print(guac)

#Int list for recipes
recipes_list = [coffee, focaccia, tea, guac]

#Int recipe_search() to find ingredients in recipes_list
print("\nRecipes with Water:")
print("---------------------")
recipe_search(recipes_list, "Water")

print("\nRecipes with Salt:")
print("--------------------")
recipe_search(recipes_list, "Salt")

print("\nRecipes with Cilantro:")
print("------------------------")
recipe_search(recipes_list, "Cilantro")

