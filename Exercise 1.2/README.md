# Exercise 1.2
- Use data types and methods to execute Python commands that store recipes containing their own internal data.
- Enter a number of these recipes into another linear data structure.

# The data for each reciepe:
- **Name (str):** Contains the name of the recipe
- **Cooking Time (int):** Contains the cooking time in minutes
- **Ingredients (list):** Contains a number of ingredients, each of the str data type

I decided to use dictionaries for storing the above data for each recipe because of the different data types needing to be stored and the versatility of dictionaries.  Dictionaries can store the recipe names as strings, the ingredients as lists, and the cooking time as integers. Dictionaries are also mutable so each recipe can be updated or added in the future.

# The outer structure containing all reciepes:
- **all_recipes = [ ]**

I have decided to use a list as the outer structure to store the recipe dictionaries in because lists are sequential and can store multiple recipes that can be modified if needed.