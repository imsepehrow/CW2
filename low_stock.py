from file_handler import load_inventory

# This will show items with how of them left in stock below a user-defined threshold
def low_stock_report():
    inventory = load_inventory()

    if not inventory:
        print("This inventory is empty.")
        return

    
    # Geting the threshold from the user
    try:
        threshold = int(input("Please enter the low-stock threshold: "))
        if threshold < 0:
            print("Threshold can not be negative.")
            return
    except ValueError:
        print("Error: Please enter an valid number.")
        return


    #Filtering the low-stock items
    low_stock_items = [item for item in inventory if item.get("quantity", 0) < threshold]

    if not low_stock_items:
        print("There are isn't any items with quantity below the {threshold}.")
        return

    # Displaying the low-stock items
    print(f"\n=== LOW STOCK ITEMS (Below {threshold}) ===")
    print("{:<5} | {:<20} | {:<10}".format("ID", "Name", "Quantity"))
    print("-" * 40)

    for item in low_stock_items:
        print("{:<5} | {:<20} | {:<10}".format(
            item["id"],
            item["name"],
            item["quantity"]
        ))
    print("-" * 40)