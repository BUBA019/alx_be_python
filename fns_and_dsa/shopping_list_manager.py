def display_menu():
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []

    while True:
        display_menu()

        try:
            choice = int(input("Enter your choice (1-4): "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 1:
            item = input("Enter item to add: ").strip()
            if item:
                shopping_list.append(item)
                print(f"{item} added to shopping list.")
            else:
                print("Item cannot be empty.")

        elif choice == 2:
            item = input("Enter item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"{item} removed from shopping list.")
            else:
                print(f"{item} not found in the list.")

        elif choice == 3:
            if shopping_list:
                print("Shopping List:")
                for idx, item in enumerate(shopping_list, 1):
                    print(f"{idx}. {item}")
            else:
                print("Your shopping list is empty.")

        elif choice == 4:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
