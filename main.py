from menu import Menu
from order import Order

def show_main_menu():
    print("\n Main menu")
    print("1. Check the menu")
    print("2. Make an order")
    print("0. Exit")

def main():
    menu = Menu()

    try:
        menu.load_from_file("menu.txt")
    except FileNotFoundError as e:
        print(e)
        return

    while True:
        show_main_menu()
        choice = input("Choose an action: ").strip()

        if choice == "1":
            menu.display_menu()

        elif choice == "2":
            order = Order()
            print("\nEnter name of dish (one at a time).")
            print("Press Enter on empty line to finish.")

            while True:
                dish_name = input("Dish: ").strip()
                if dish_name == "":
                    break

                dish = menu.find_dish(dish_name)
                if dish:
                    order.add_dish(dish)
                    print(f"Added: {dish.name}")
                else:
                    print("Error! Choose from menu.")

            if order.items:
                order.print_receipt()
            else:
                print("Order is empty! Back to menu.")

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print(" Invalid input!")

if __name__ == "__main__":
    main()