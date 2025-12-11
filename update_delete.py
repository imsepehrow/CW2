from file_handler import load_inventory, save_inventory

# Prints in a table format when the user has chosen to update or delete an item and entered the item ID
def print_table_header():
    print("\nID   | Name                 | Price     | Quantity")
    print("-------------------------------------------------------")

# Print one item in table row format
def print_item_row(item):
    print(f"{item['id']:<4} | {item['name']:<20} | £{item['price']:<8.2f} | {item['quantity']}")

#Get a numeric input from the user and returns none if the user enters invalid data
def get_number(prompt, number_type):
    try:
        return number_type(input(prompt))
    except ValueError:
        print(f"Error: {number_type.__name__.title()} expected.")
        return None

# Find an item in the inventory list by its ID
#Returns the item if it is found otherwise none
def find_item(inv, item_id):
    return next((i for i in inv if i.get("id") == item_id), None)

# Update an item in the inventory, loads data from inventory file and checks if inventory exists or if it's empty
def update_item():
    inv = load_inventory()
    if not inv:
        print("Inventory is empty.")
        return

#Looks up the item by its ID
    item_id = get_number("Enter item ID to update: ", int)
    if item_id is None:
        return

#If the item ID doesn't exist the progam returns 'item not found'
    item = find_item(inv, item_id)
    if not item:
        print("Item not found.")
        return

# Show the table with the item selected by the user
    print_table_header()
    print_item_row(item)

#Prints in a table format clearly showing the user the options available when updating an item
    print("\n1. Name  |  2. Price  |  3. Quantity")
    print("----------------------------------------")
    userchoice = input("Choose (| 1 |---| 2 |---| 3 |): ").strip()

#User can update the name of a product
    if userchoice == "1":
        new_name = input("New name: ").strip()
        if not new_name:
            print("Invalid name: name cannot be blank.")
            return

#Saves name changes and returns ' Name updated' if criteria are met.
        item["name"] = new_name
        save_inventory(inv)
        print("Name updated!")
        return

#User can update the price or quantity of an item.
    if userchoice in ("2", "3"):
        value_type = float if userchoice == "2" else int
        new_val = get_number("New value: ", value_type)

        if new_val is None:
            return
        if new_val < 0:
            print("Invalid value: must not be negative.")
            return

        field = "price" if userchoice == "2" else "quantity"
        item[field] = new_val
        save_inventory(inv)
        print("Item updated!")
        return

#Price and quantity must be a positive number or program returns 'Invalid Choice'
    print("Invalid choice.")

#User can choose to delete a product from the inventory
def delete_item():
    inv = load_inventory()
    if not inv:
        print("Inventory is empty.")
        return

    item_id = get_number("Enter item ID to delete: ", int)
    if item_id is None:
        return

#If user enters an ID that doesn't exist or leaves field empty, program returns 'item not found'
    item = find_item(inv, item_id)
    if not item:
        print("Item not found.")
        return

# Show table row for selected item
    print_table_header()
    print_item_row(item)

#Confirms if user wants to delete an item and is given the options yes or no to confirm or cancel the decision
    confirm = input("\nDelete this item? (|Y|/|N|): ").strip().lower()
    if confirm == "y":
        inv.remove(item)
        save_inventory(inv)
        print("Item deleted.")
    else:
        print("Item deletion cancelled.")