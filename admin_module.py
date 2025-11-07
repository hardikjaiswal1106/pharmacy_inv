from file_utils import load_data, save_data
from tabulate import tabulate
from datetime import datetime
import json

def add_medicine():
    medicines = load_data('medicines.json')
    med_id = len(medicines) + 1
    name = input("Enter medicine name: ")
    category = input("Enter category: ")
    price = float(input("Enter price: "))
    stock = int(input("Enter stock: "))
    expiry = input("Enter expiry date (YYYY-MM-DD): ")

    medicines.append({
        "med_id": med_id,
        "name": name,
        "category": category,
        "price": price,
        "stock": stock,
        "expiry": expiry
    })
    save_data('medicines.json', medicines)
    print("✅ Medicine added successfully!\n")

def view_medicines():
    medicines = load_data('medicines.json')
    if not medicines:
        print("No medicines found.\n")
        return
    print(tabulate(medicines, headers="keys", tablefmt="grid"))

def update_medicine():
    medicines = load_data('medicines.json')
    view_medicines()
    med_id = int(input("Enter Medicine ID to update: "))
    for med in medicines:
        if med["med_id"] == med_id:
            med["price"] = float(input("New Price: "))
            med["stock"] = int(input("New Stock: "))
            print("✅ Medicine updated successfully!\n")
            save_data('medicines.json', medicines)
            return
    print("❌ Medicine not found!\n")

def delete_medicine():
    medicines = load_data('medicines.json')
    view_medicines()
    med_id = int(input("Enter Medicine ID to delete: "))
    medicines = [m for m in medicines if m["med_id"] != med_id]
    save_data('medicines.json', medicines)
    print("✅ Medicine deleted!\n")

def generate_report():
    medicines = load_data('medicines.json')
    today = datetime.date.today()
    low_stock = [m for m in medicines if m["stock"] < 5]
    near_expiry = [
        m for m in medicines if 
        (datetime.datetime.strptime(m["expiry"], "%Y-%m-%d").date() - today).days <= 30
    ]
    print("\n📦 Low Stock Medicines:")
    print(tabulate(low_stock, headers="keys", tablefmt="grid"))
    print("\n⏰ Near Expiry Medicines:")
    print(tabulate(near_expiry, headers="keys", tablefmt="grid"))
    print()

def admin_menu():
    while True:
        print("""
=== Admin Menu ===
1. Add Medicine
2. Update Medicine
3. Delete Medicine
4. View Medicines
5. Generate Report
6. Logout
""")
        choice = input("Enter choice: ")
        if choice == '1': add_medicine()
        elif choice == '2': update_medicine()
        elif choice == '3': delete_medicine()
        elif choice == '4': view_medicines()
        elif choice == '5': generate_report()
        elif choice == '6': break
        else: print("Invalid choice!\n")
