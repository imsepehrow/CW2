from file_handler import load_inventory, save_inventory

# Get numeric input
# Returns None if user enters invalid data
def get_number(prompt, number_type):
    try:
        return number_type(input(prompt))
    except ValueError:
        print(f"Error: {number_type.__name__.title()} expected.")
        return None

# Find an item in the inventory list by its ID
# Returns the item dict if it is found otherwise None
def find_item(inv, item_id):
    return next((i for i in inv if i["id"] == item_id), None)

# Update an inventory item
def update_item():
    inv = load_inventory() # Load saved inventory from file
    if not inv:            # Checks inf inventory exists or if it is empty
        return print("Inventory is empty.")
# Ask the user which item they want to update
    item_id = get_number("Enter item ID to update: ", int)
    if item_id is None:
        return
     
    item = find_item(inv, item_id)   # Look up the item by its ID   
    if not item:
        return print("Item not found.")

    print("Selected:", item)
    print("1. Name  |  2. Price  |  3. Quantity")
    choice = input("Choose (1/2/3): ")   # Choose field you want to update

    if choice == "1":   # Update name
        new = input("New name: ").strip()
        return print("Name updated!") if new and not (item.update({"name": new}) or False) else print("Invalid name.")

    if choice in ("2", "3"):  # Update price or quantity
        val_type = float if choice == "2" else int      # Price uses Float and quantity uses Int
        new_val = get_number("New value: ", val_type)   # Get the new value
        if new_val is None:
            return
        item["price" if choice == "2" else "quantity"] = new_val  # Apply update
        save_inventory(inv)                                       # Save the updated inventory
        return print("Item updated!")

    print("Invalid choice.") # If the user enters an invalid menu option

# Delete an item from the inventory
def delete_item():
    inv = load_inventory()   # Load current inventory
    if not inv:
        return print("Inventory is empty.")
# Ask the user for the ID to delete the item
    item_id = get_number("Enter item ID to delete: ", int)
    if item_id is None:
        return

    item = find_item(inv, item_id)
    if not item:
        return print("Item not found.")
# Confirm before deleting item
    if input(f"Delete {item}? (y/n): ").lower() == "y":
        inv.remove(item)     # Remove item from inventory
        save_inventory(inv)  # Save updated list
        print("Item deleted.")
    else:
        print("Cancelled.")