# main.py

from add_view import add_item, view_inventory
from update_delete import update_item, delete_item
from low_stock import low_stock_report
from file_handler import load_inventory, save_inventory


# Show the main menu options
def show_menu():
    print("\n=== INVENTORY MENU ===")
    print("1. Add item")
    print("2. View stock")
    print("3. Update item")
    print("4. Delete item")
    print("5. Search")
    print("6. Low stock report")
    print("7. Save and exit")


# Search items by name or ID
def search_inventory():
    inventory = load_inventory()

    if not inventory:
        print("Inventory is empty.")
        return

    term = input("Enter item name or ID to search: ").strip()
    if term == "":
        print("Search term cannot be empty.")
        return

    matches = []

    # Search by ID if the user typed a number
    if term.isdigit():
        search_id = int(term)
        for item in inventory:
            if item.get("id") == search_id:
                matches.append(item)

    # Search by name (case insensitive)
    term_lower = term.lower()
    for item in inventory:
        name = str(item.get("name", "")).lower()
        if term_lower in name and item not in matches:
            matches.append(item)

    if not matches:
        print("No items found.")
        return

    print("\n=== SEARCH RESULTS ===")
    print("{:<5} | {:<20} | {:<10} | {:<10}".format("ID", "Name", "Price", "Qty"))
    print("-" * 50)

    for item in matches:
        print("{:<5} | {:<20} | {:<10} | {:<10}".format(
            item["id"],
            item["name"],
            item["price"],
            item["quantity"]
        ))

    print("-" * 50)


def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-7): ").strip()

        if choice == "1":
            add_item()
        elif choice == "2":
            view_inventory()
        elif choice == "3":
            update_item()
        elif choice == "4":
            delete_item()
        elif choice == "5":
            search_inventory()
        elif choice == "6":
            # reports menu option (low stock report)
            low_stock_report()
        elif choice == "7":
            # Exit Program
            print("Exiting program.")
            break
        else:
            print("Please enter a number between 1 and 7.")


if __name__ == "__main__":
    main()
