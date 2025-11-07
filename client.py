from file_utils import *
from admin_module import view_medicines
import json
import os


def register_client():
    clients = load_data('clients.json')
    client_id = len(clients) + 1
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    contact = input("Enter contact number: ")

    clients.append({"client_id": client_id, "name": name, "age": age, "contact": contact})
    save_data('clients.json', clients)
    print(f"✅ Registered successfully! Your Client ID is {client_id}\n")

def search_medicine():
    medicines = load_data('medicines.json')
    term = input("Enter medicine name or category: ").lower()
    results = [m for m in medicines if term in m["name"].lower() or term in m["category"].lower()]
    if results:
        print(tabulate(results, headers="keys", tablefmt="grid"))
    else:
        print("❌ No results found.\n")

def place_order(client_id):
    medicines = load_data('medicines.json')
    orders = load_data('orders.json')
    if not os.path.exists('medicines.json'):
        print("No medicines available.\n")
        return
    else:
        
        view_medicines()
    med_id = input("Enter Medicine name to order: ")


    qty = int(input("Enter quantity: "))

    for med in medicines:
        if med["med_id"] == med_id:
            if med["stock"] >= qty:
                med["stock"] -= qty
                order = {
                    "order_id": len(orders) + 1,
                    "client_id": client_id,
                    "med_id": med_id,
                    "qty": qty,
                    "status": "Placed"
                }
                orders.append(order)
                save_data('orders.json', orders)
                save_data('medicines.json', medicines)
                print("✅ Order placed successfully!\n")
                return
            else:
                print("❌ Not enough stock!\n")
                return
    print("❌ Medicine not found!\n")

def view_orders(client_id):
    orders = load_data('orders.json')
    client_orders = [o for o in orders if o["client_id"] == client_id]
    if client_orders:
        print(tabulate(client_orders, headers="keys", tablefmt="grid"))
    else:
        print("No orders found.\n")

def cancel_order(client_id):
    orders = load_data('orders.json')
    view_orders(client_id)
    order_id = int(input("Enter Order ID to cancel: "))
    for o in orders:
        if o["order_id"] == order_id and o["client_id"] == client_id:
            if o["status"] == "Placed":
                o["status"] = "Cancelled"
                save_data('orders.json', orders)
                print("✅ Order cancelled!\n")
                return
            else:
                print("❌ Order already processed.\n")
                return
    print("❌ Order not found!\n")


def client_menu(client_id):
    while True:
        print("""
=== Client Menu ===
1. Search Medicine
2. Place Order
3. View Orders
4. Cancel Order
5. Logout
""")
        choice = input("Enter choice: ")
        if choice == '1': search_medicine()
        elif choice == '2': place_order(client_id)
        elif choice == '3': view_orders(client_id)
        elif choice == '4': cancel_order(client_id)
        elif choice == '5': break
        else: print("Invalid choice!\n")
