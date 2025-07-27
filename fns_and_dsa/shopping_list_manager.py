# manager.py

# ✅ Step 1: Define a global array to store items
shopping_list = []

# ✅ Step 2: Define the display_menu function
def display_menu():
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. View List")
    print("3. Exit")

# ✅ Step 3: Main loop to interact with user
def main():
    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice (1-3): "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 1:
            item = input("Enter item to add: ")
            shopping_list.append(item)
            print(f"'{item}' has been added to your shopping list.")
        elif choice == 2:
            print("\nYour Shopping List:")
            for i, item in enumerate(shopping_list, 1):
                print(f"{i}. {item}")
        elif choice == 3:
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please select between 1 and 3.")

# ✅ Step 4: Call main function
if __name__ == "__main__":
    main()
