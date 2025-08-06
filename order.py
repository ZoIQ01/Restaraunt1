from dish import Dish

class Order:
    def __init__(self):
        self.items: list[Dish] = []

    def add_dish(self, dish: Dish):
        self.items.append(dish)

    def total(self) -> float:
        return sum(dish.price for dish in self.items)

    def is_empty(self) -> bool:
        return len(self.items) == 0  # ← Вот это то, чего не хватало

    def print_receipt(self):
        print("\n🧾 Чек:")
        for dish in self.items:
            print(f"- {dish.name}: {dish.price} UAH")
        print(f"\n💰 Итого: {self.total()} UAH\n")