from file_handler import load_inventory, save_inventory

# Function to generate the next unique ID
def generate_next_id(inventory):
    if not inventory:   # If list is empty
        return 1
    # Get highest existing ID
    max_id = max(item["id"] for item in inventory)
    return max_id + 1


# Function to add a new item to the inventory
def add_item():
    inventory = load_inventory()

    # --- NAME VALIDATION ---
    name = input("Enter item name: ").strip()
    if name == "":
        print("Error: Name cannot be empty.")
        return
    
    # --- PRICE VALIDATION ---
    try:
        price = float(input("Enter item price: "))
    except ValueError:
        print("Error: Price must be a number.")
        return
    
    # --- QUANTITY VALIDATION ---
    try:
        quantity = int(input("Enter item quantity: "))
    except ValueError:
        print("Error: Quantity must be a number.")
        return

    # --- CREATE ITEM ---
    item = {
        "id": generate_next_id(inventory),
        "name": name,
        "price": price,
        "quantity": quantity
    }

    # Add to list and save
    inventory.append(item)
    save_inventory(inventory)
    print("Item added successfully!")


# Function to display inventory as a table
def view_inventory():
    inventory = load_inventory()

    if not inventory:
        print("Inventory is empty.")
        return

    print("\n=== INVENTORY LIST ===")
    print("{:<5} | {:<20} | {:<10} | {:<10}".format("ID", "Name", "Price", "Qty"))
    print("-" * 50)

    for item in inventory:
        print("{:<5} | {:<20} | {:<10} | {:<10}".format(
            item["id"],
            item["name"],
            item["price"],
            item["quantity"]
        ))

    print("-" * 50)
