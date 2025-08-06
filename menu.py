from category import MenuCategory
from dish import Dish
import os

class Menu:
    def __init__(self):
        self.categories: list[MenuCategory] = []

    def load_from_file(self, filename: str):
        if not os.path.exists(filename):
            raise FileNotFoundError(f"Menu file '{filename}' not found.")

        with open(filename, 'r', encoding='utf-8') as file:
            current_category = None

            for line in file:
                line = line.strip()
                if not line:
                    continue

                if line.startswith("[") and line.endswith("]"):
                    category_name = line[1:-1]
                    current_category = MenuCategory(category_name)
                    self.categories.append(current_category)
                elif current_category:
                    try:
                        name, price = line.split(",")
                        dish = Dish(name.strip(), float(price.strip()))
                        current_category.add_dish(dish)
                    except ValueError:
                        print(f"error: {line}")

    def find_dish(self, name: str) -> Dish | None:
        for category in self.categories:
            for dish in category.dishes:
                if dish.name.lower() == name.lower():
                    return dish
        return None

    def display_menu(self):
        for category in self.categories:
            print(category)
            print()