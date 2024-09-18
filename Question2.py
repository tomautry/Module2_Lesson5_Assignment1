# The Shopping List Maker

def add_item(shopping_list):
    item = input("Enter an item to add: ")
    if item:
        shopping_list.append(item)
        print(f"{item} has been added to the list.")
    else:
        print("Invalid input. No item added.")

def remove_item(shopping_list):
    item = input("Enter the item to remove: ")
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"{item} has been removed from the list.")
    else:
        print(f"{item} not found in the list.")

def print_list(shopping_list):
    if shopping_list:
        print("Your shopping list:")
        for item in shopping_list:
            print(item)
    else:
        print("Your shopping list is empty.")

def main():
    shopping_list = []

    while True:
        print("Options:")
        print("1. Add item")
        print("2. Remove item")
        print("3. Print list")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_item(shopping_list)
        elif choice == "2":
            remove_item(shopping_list)
        elif choice == "3":
            print_list(shopping_list)
        elif choice == "4":
            print("Goodbye.")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 4.")

main()
