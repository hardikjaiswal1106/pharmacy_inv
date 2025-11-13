# admin_module.py
from file_utils import load_data, save_data
from tabulate import tabulate
import datetime
import json

def add_medicine():
    medicines = load_data('medicines.json')
    try:
        med_id = len(medicines) + 1
        name = input("Enter medicine name: ").strip()
        category = input("Enter category: ").strip()
        price = float(input("Enter price: "))
        stock = int(input("Enter stock: "))
        expiry = input("Enter expiry date (YYYY-MM-DD): ").strip()

        medicines.append({
            "med_id": med_id,
            "name": name,
            "category": category,
            "price": price,
            "stock": stock,
            "expiry": expiry
        })
        save_data('medicines.json', medicines)
        print("\n\033[1;92m✅ Medicine added successfully!\033[0m\n")
    except Exception as e:
        print("\033[1;91m❌ Invalid input. Please try again carefully.\033[0m\n")


def view_medicines():
    try:
        medicines = load_data('medicines.json')
    except json.JSONDecodeError:
        print("\033[1;91m❌ Data file corrupted. Please recheck medicines.json.\033[0m\n")
        return

    if not medicines:
        print("\033[1;91m❌ No medicines found.\033[0m\n")
        return

    print("\n" + "="*60)
    table = [
        [m["med_id"], m["name"], m["category"], m["price"], m["stock"], m["expiry"]]
        for m in medicines
    ]
    print(tabulate(table, headers=["ID", "Name", "Category", "Price", "Stock", "Expiry"], tablefmt="fancy_grid"))
    print("="*60 + "\n")
    print(f"\033[1;94mTotal medicines listed: {len(medicines)}\033[0m\n")


def update_medicine():
    medicines = load_data('medicines.json')
    if not medicines:
        print("\033[1;91m❌ No medicines available to update.\033[0m\n")
        return

    view_medicines()
    try:
        med_id = int(input("Enter Medicine ID to update: "))
        for med in medicines:
            if med["med_id"] == med_id:
                med["price"] = float(input("New Price: "))
                med["stock"] = int(input("New Stock: "))
                save_data('medicines.json', medicines)
                print("\033[1;92m✅ Medicine updated successfully!\033[0m\n")
                return
        print("\033[1;91m❌ Medicine not found.\033[0m\n")
    except:
        print("\033[1;91m❌ Invalid input. Please enter valid numbers.\033[0m\n")


def delete_medicine():
    medicines = load_data('medicines.json')
    if not medicines:
        print("\033[1;91m❌ No medicines available to delete.\033[0m\n")
        return

    view_medicines()
    try:
        med_id = int(input("Enter Medicine ID to delete: "))
        new_meds = [m for m in medicines if m["med_id"] != med_id]

        if len(new_meds) == len(medicines):
            print("\033[1;91m❌ Medicine not found.\033[0m\n")
            return

        for idx, m in enumerate(new_meds, start=1):
            m["med_id"] = idx
        save_data('medicines.json', new_meds)
        print("\033[1;92m✅ Medicine deleted successfully!\033[0m\n")
    except:
        print("\033[1;91m❌ Invalid input. Please try again.\033[0m\n")


def generate_report():
    medicines = load_data('medicines.json')
    if not medicines:
        print("\033[1;91m❌ No medicines available to generate report.\033[0m\n")
        return

    today = datetime.date.today()
    low_stock = []
    near_expiry = []

    for m in medicines:
        try:
            # Low stock threshold: less than 20
            if int(m.get("stock", 0)) < 20:
                low_stock.append(m)
            
            # Near expiry check (within next 30 days)
            expiry_str = m.get("expiry", "")
            exp_date = datetime.datetime.strptime(expiry_str, "%Y-%m-%d").date()
            days_left = (exp_date - today).days
            if days_left <= 30:
                temp = m.copy()
                temp["days_left"] = days_left
                near_expiry.append(temp)
        except:
            continue

    # === Report Output ===
    print("\n📦 \033[1;94mLow Stock Medicines (< 20 units):\033[0m")
    if low_stock:
        print(tabulate(
            [[m["med_id"], m["name"], m["stock"]] for m in low_stock],
            headers=["ID", "Name", "Stock"],
            tablefmt="fancy_grid"
        ))
    else:
        print("\033[1;91m❌ No low stock medicines.\033[0m\n")

    print("\n⏰ \033[1;94mNear Expiry Medicines (<= 30 days):\033[0m")
    if near_expiry:
        print(tabulate(
            [[m["med_id"], m["name"], m["expiry"], m["days_left"]] for m in near_expiry],
            headers=["ID", "Name", "Expiry Date", "Days Left"],
            tablefmt="fancy_grid"
        ))
    else:
        print("\033[1;91m❌ No medicines near expiry.\033[0m\n")

    # Total stock value
    total_value = sum(
        m.get("price", 0) * m.get("stock", 0)
        for m in medicines if isinstance(m.get("price", 0), (int, float))
    )
    print(f"\n\033[1;94m📊 Total Stock Value: ₹{total_value}\033[0m\n")


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
        choice = input("Enter choice: ").strip()
        if choice == '1':
            add_medicine()
        elif choice == '2':
            update_medicine()
        elif choice == '3':
            delete_medicine()
        elif choice == '4':
            view_medicines()
        elif choice == '5':
            generate_report()
        elif choice == '6':
            print("\033[1;92m👋 Logged out from Admin Menu.\033[0m\n")
            break
        else:
            print("\033[1;91m❌ Invalid choice. Please try again.\033[0m\n")
