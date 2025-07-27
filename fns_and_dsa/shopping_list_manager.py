# manager.py

# Step 1: Define the array
shopping_list = []

# Step 2: Define the display_menu function
def display_menu():
    print("\nShopping List Manager")
    print("1. Add item")
    print("2. View list")
    print("3. Exit")

# Step 3: Use a loop to call display_menu and take input
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
        print(f"{item} added to the shopping list.")
    elif choice == 2:
        print("Your Shopping List:")
        for idx, item in enumerate(shopping_list, start=1):
            print(f"{idx}. {item}")
    elif choice == 3:
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
