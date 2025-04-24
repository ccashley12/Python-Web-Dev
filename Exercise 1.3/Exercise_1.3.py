def recipes():
    recipes_list = []
    ingredients_list = []

    def take_recipe():
        name = input("Enter recipe name: ")
        cooking_time = int(input("Enter cooking time (in minutes): "))
        ingredients = list(input("Enter the ingredients (separated by a comma): ").split(", "))
        recipe = { 
            "name": name, 
            "cooking_time": cooking_time, 
            "ingredients": ingredients
        }
        return recipe

    num = int(input("Enter number of recipes: "))
    for i in range(num):
        recipe = take_recipe()

        for ingredient in recipe["ingredients"]:
            if not ingredient in ingredients_list:
                ingredients_list.append(ingredient)

        recipes_list.append(recipe)

    for recipe in recipes_list:
        if recipe["cooking_time"] < 10 and len(recipe["ingredients"]) < 4:
            recipe["difficulty"] = "easy"
        elif recipe["cooking_time"] < 10 and len(recipe["ingredients"]) >= 4:
            recipe["difficulty"] = "medium"
        elif recipe["cooking_time"] >= 10 and len(recipe["ingredients"]) < 4:
            recipe["difficulty"] = "intermediate"
        elif recipe["cooking_time"] >= 10 and len(recipe["ingredients"]) >= 4:
            recipe["difficulty"] = "hard"

    for recipe in recipes_list:
        print("Recipe:", recipe["name"])
        print("Cooking time (min):", recipe["cooking_time"])
        print("Ingredients:")
        for ingredient in recipe["ingredients"]:
            print(ingredient)
        print("Difficulty:", recipe["difficulty"])

    def print_ingredients():
        print("All Ingredients from All Recipes")
        print("_______________")
        ingredients_list.sort()
        for ingredient in ingredients_list:
            print(ingredient)

    print_ingredients()

recipes()