from file_handler import load_inventory, save_inventory

# Function to generate the next unique ID without duplicates
def generate_next_id(inventory):
    if not inventory:
        return 1
    
    existing_ids = sorted(item["id"] for item in inventory)

    expected = 1
    for id_value in existing_ids:
        if id_value != expected:
            return expected
        expected += 1

    return expected


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
        if price <= 0:
            print("Error: Price must be greater than 0.")
            return
    except ValueError:
        print("Error: Price must be a number.")
        return
    
    # --- QUANTITY VALIDATION ---
    try:
        quantity = int(input("Enter item quantity: "))
        if quantity < 0:
            print("Error: Quantity cannot be negative.")
            return
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