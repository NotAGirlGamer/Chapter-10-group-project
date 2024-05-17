import os
import pickle
from Retail import RetailItem
from Cashregister import CashRegister

INVENTORY_FILE = 'inventory.dat'
PASSWORD = 'password'

def main_menu():
    while True:
        print("\nMain Menu:")
        print("1. Access inventory system")
        print("2. Access retail system")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            if inventory_login():
                inventory_menu()
        elif choice == '2':
            retail_menu()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

def inventory_login():
    password = input("Enter the inventory system password: ")
    if password == PASSWORD:
        return True
    else:
        print("Incorrect password.")
        return False

def inventory_menu():
    inventory = load_inventory()
    while True:
        print("\nInventory Menu:")
        print("1. Display inventory")
        print("2. Add to inventory")
        print("3. Save inventory data")
        print("4. End")
        choice = input("Enter your choice: ")
        if choice == '1':
            display_inventory(inventory)
        elif choice == '2':
            add_inventory(inventory)
        elif choice == '3':
            save_inventory(inventory)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

def display_inventory(inventory):
    if not inventory:
        print("Inventory is empty.")
    for item in inventory:
        print(item)

def add_inventory(inventory):
    description = input("Enter item description: ")
    units = input("Enter number of units: ")
    while not units.isdigit():
        print("Invalid input. Please enter an integer.")
        units = input("Enter number of units: ")
    units = int(units)
    price = input("Enter price per unit: ")
    while not is_float(price):
        print("Invalid input. Please enter a float.")
        price = input("Enter price per unit: ")
    price = float(price)
    inventory.append(RetailItem(description, units, price))

def save_inventory(inventory):
    with open(INVENTORY_FILE, 'wb') as file:
        pickle.dump(inventory, file)
    print("Inventory data saved.")

def load_inventory():
    if os.path.exists(INVENTORY_FILE):
        with open(INVENTORY_FILE, 'rb') as file:
            return pickle.load(file)
    return []

def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def retail_menu():
    inventory = load_inventory()
    if not inventory:
        print("No items in inventory. Please add items first.")
        return
    
    cash_register = CashRegister()
    while True:
        print("\nRetail Menu:")
        print("1. Display Cart")
        print("2. Display Items")
        print("3. Purchase Item")
        print("4. Empty Cart and Start over")
        print("5. Check-out")
        print("6. EXIT to main")
        choice = input("Enter your choice: ")
        if choice == '1':
            cash_register.show_cart()
        elif choice == '2':
            display_inventory(inventory)
        elif choice == '3':
            purchase_item(cash_register, inventory)
        elif choice == '4':
            cash_register.empty()
            print("Cart is now empty.")
        elif choice == '5':
            checkout(cash_register)
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

def purchase_item(cash_register, inventory):
    item_description = input("Enter the item description to purchase: ")
    for item in inventory:
        if item.get_description().lower() == item_description.lower():
            cash_register.purchase_item(item)
            print(f"Added {item_description} to cart.")
            return
    print("Item not found.")

def checkout(cash_register):
    print("Your cart contains the following items:")
    cash_register.show_cart()
    total = cash_register.get_total()
    print(f"Total amount due: ${total:.2f}")
    cash_register.empty()
    print("Thank you for your purchase!")

if __name__ == "__main__":
    main_menu()