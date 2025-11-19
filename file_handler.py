import json
import os


# Save the file name into a variable
inventory_file_name = "inventory.json"



# Load data from a JSON file and return a list of dictionaries
def load_inventory():

# If the file does not exist return an empty list
    if not os.path.exists(inventory_file_name):
        return []
    try:
        with open(inventory_file_name, "r") as f:
            data = f.read().strip()

# If the file is empty return an empty list
            if data == "":
                return[]
            return json.loads(data)
        
# If the file is corrupted return an empty list
    except (json.JSONDecodeError,ValueError):
        print("Warning: inventory file is corrupted!")
        return[]
    
# Save list of dictionaries into a JSON file
def save_inventory(inventory):
    with open(inventory_file_name, "w")as f:
        json.dump(inventory, f, indent=4)