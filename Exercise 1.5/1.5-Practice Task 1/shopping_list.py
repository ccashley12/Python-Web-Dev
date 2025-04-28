class ShoppingList(object):
    def __init__(self, list_name):
        self.list_name = list_name
        self.shopping_list = []

    def add_item(self, item):
        if not item in self.shopping_list:
            self.shopping_list.append(item)
            print("Item added to shopping list!")
        else:
            print("Item already on shopping list!")

    def remove_item(self, item):
        if item in self.shopping_list:
            self.shopping_list.remove(item)
            print("Item removed from shopping list!")
        else:
            print("Item not found on shopping list.")

    def view_list(self):
        if not self.shopping_list:
            print("The shopping list is empty!")
        else:
            print("Shopping List:")
            print("--------------")
            for item in self.shopping_list:
                print(item)
    
    def merge_lists(self, obj):
        merged_lists_name = "MergedList - " + str(self.list_name) + "+" + str(obj.list_name)

        merged_lists_obj = ShoppingList(merged_lists_name)

        merged_lists_obj.shopping_list = self.shopping_list.copy()

        for item in obj.shopping_list:
            if not item in merged_lists_obj.shopping_list:
                merged_lists_obj.shopping_list.append(item)
        return merged_lists_obj
    
grocery_store_list = ShoppingList("Grocery Store Shopping List")
pet_store_list = ShoppingList("Pet Store List")

for item in ["tofu", "mushrooms", "garlic", "onions", "tomatoes", "basil"]:
    grocery_store_list.add_item(item)

for item in ["cat food", "litter", "clawing tower", "toys", "Robo Litter Box"]:
    pet_store_list.add_item(item)

grocery_store_list.merge_lists(pet_store_list)

merged_list = ShoppingList.merge_lists(grocery_store_list, pet_store_list)

merged_list.view_list()

# grocery_store_list.add_item("tofu")
# grocery_store_list.add_item("mushrooms")
# grocery_store_list.add_item("garlic")
# grocery_store_list.add_item("onions")
# grocery_store_list.add_item("tomatoes")
# grocery_store_list.add_item("basil")

# grocery_store_list.remove_item("basil")

# grocery_store_list.add_item("oat milk")

# grocery_store_list.view_list()