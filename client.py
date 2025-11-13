import json
from tabulate import tabulate
from file_utils import load_data, save_data

# ================================
# Client Registration
# ================================
def register_client():
    clients = load_data("clients.json")

    name = input("Enter your name: ").strip()
    phone = input("Enter your phone number: ").strip()

    client_id = len(clients) + 1
    clients.append({
        "client_id": client_id,
        "name": name,
        "phone": phone
    })

    save_data("clients.json", clients)
    print(f"\n\033[1;92m✅ Registration Successful!\033[0m  Your Client ID is \033[1;96m[{client_id}]\033[0m\n")
    return client_id


# ================================
# View / Search Medicines
# ================================
def view_medicines():
    medicines = load_data("medicines.json")
    if not medicines:
        print("\n⚠️ No medicines available.\n")
        return

    table_data = [[m["med_id"], m["name"], f"₹{m['price']}", m["stock"]] for m in medicines]
    print("\n=== 💊 Available Medicines ===\n")
    print(tabulate(table_data, headers=["ID", "Name", "Price", "Stock"], tablefmt="fancy_grid"))
    print()


def search_medicine():
    medicines = load_data("medicines.json")
    if not medicines:
        print("\n⚠️ No medicines available.\n")
        return

    query = input("\nEnter medicine name to search: ").strip().lower()
    results = [m for m in medicines if query in m["name"].lower()]

    if not results:
        print(f"\n❌ No medicines found matching '{query}'.\n")
        return

    table_data = [
        [m["med_id"], m["name"], f"₹{m['price']}", m["stock"]] for m in results
    ]
    print("\n=== 💊 Search Results ===\n")
    print(tabulate(table_data, headers=["ID", "Name", "Price", "Stock"], tablefmt="fancy_grid"))
    print()


# ================================
# Place Order
# ================================
def place_order(client_id):
    medicines = load_data("medicines.json")
    if not medicines:
        print("\n⚠️ No medicines available.\n")
        return

    cart = []
    orders = load_data("orders.json")

    print("\n=== 🛒 PLACE YOUR ORDER ===\n")

    while True:
        view_medicines()
        med_input = input("Enter Medicine ID (or 0 to finish): ").strip()

        if med_input == "0":
            break

        # Validate medicine ID
        try:
            med_id = int(med_input)
        except ValueError:
            print("\033[1;91m❌ Invalid input! Please enter a numeric Medicine ID.\033[0m\n")
            continue

        medicine = next((m for m in medicines if m["med_id"] == med_id), None)
        if not medicine:
            print("\033[1;91m❌ Invalid Medicine ID! Please try again.\033[0m\n")
            continue

        try:
            qty = int(input(f"Enter quantity for {medicine['name']}: "))
        except ValueError:
            print("\033[1;91m❌ Invalid input! Quantity must be a number.\033[0m\n")
            continue

        if qty <= 0:
            print("\033[1;91m❌ Quantity must be positive!\033[0m\n")
            continue

        if qty > medicine["stock"]:
            print(f"\033[1;91m❌ Not enough stock! Available: {medicine['stock']}\033[0m\n")
            continue

        # Add to cart
        cart.append({
            "med_id": medicine["med_id"],
            "med_name": medicine["name"],
            "qty": qty,
            "unit_price": medicine["price"],
            "total_bill": medicine["price"] * qty
        })

        # Reduce stock immediately
        medicine["stock"] -= qty
        print(f"\033[1;92m✅ Added {qty} x {medicine['name']} to cart.\033[0m\n")

    if not cart:
        print("\n⚠️ No items were added to your cart.\n")
        return

    # Save updated stock
    save_data("medicines.json", medicines)

    # Generate bill
    print("\n" + "=" * 50)
    print("🧾  YOUR RECEIPT")
    print("=" * 50)

    total_amount = sum(item["total_bill"] for item in cart)
    table_data = [
        [item["med_name"], item["qty"], item["unit_price"], item["total_bill"]]
        for item in cart
    ]
    print(tabulate(table_data, headers=["Medicine", "Quantity", "Unit Price", "Total"], tablefmt="fancy_grid"))
    print(f"\n💰 Grand Total: ₹{total_amount}\n")

    # Save each item as an order
    for item in cart:
        orders.append({
            "order_id": len(orders) + 1,
            "client_id": client_id,
            "med_id": item["med_id"],
            "med_name": item["med_name"],
            "qty": item["qty"],
            "unit_price": item["unit_price"],
            "total_bill": item["total_bill"],
            "status": "Placed"
        })
    save_data("orders.json", orders)

    print("\033[1;92m✅ Order placed successfully!\033[0m\n")


# ================================
# View & Cancel Orders
# ================================
def view_orders(client_id):
    orders = load_data("orders.json")
    user_orders = [o for o in orders if o["client_id"] == client_id]

    if not user_orders:
        print("\n⚠️ You have not placed any orders yet.\n")
        return

    print("\n=== 📦 Your Orders ===\n")
    table_data = [
        [o["order_id"], o["med_name"], o["qty"], o["unit_price"], o["total_bill"], o["status"]]
        for o in user_orders
    ]
    print(tabulate(table_data, headers=["Order ID", "Medicine", "Qty", "Price", "Total", "Status"], tablefmt="fancy_grid"))
    print()


def cancel_order(client_id):
    orders = load_data("orders.json")
    user_orders = [o for o in orders if o["client_id"] == client_id]

    if not user_orders:
        print("\n⚠️ You have no orders to cancel.\n")
        return

    table_data = [
        [o["order_id"], o["med_name"], o["qty"], o["total_bill"], o["status"]]
        for o in user_orders
    ]
    print("\n=== 📦 Your Orders ===\n")
    print(tabulate(table_data, headers=["Order ID", "Medicine", "Qty", "Total", "Status"], tablefmt="fancy_grid"))

    try:
        cancel_id = int(input("\nEnter Order ID to cancel: "))
    except ValueError:
        print("\033[1;91m❌ Invalid input! Please enter a valid Order ID.\033[0m\n")
        return

    order = next((o for o in orders if o["order_id"] == cancel_id and o["client_id"] == client_id), None)
    if not order:
        print("\033[1;91m❌ Order not found.\033[0m\n")
        return

    if order["status"] == "Cancelled":
        print("\033[1;93m⚠️ Order already cancelled.\033[0m\n")
        return

    # Mark as cancelled
    order["status"] = "Cancelled"
    save_data("orders.json", orders)
    print(f"\033[1;92m✅ Order ID {cancel_id} cancelled successfully!\033[0m\n")


# ================================
# Client Menu
# ================================
def client_menu(client_id):
    while True:
        print("\n" + "=" * 40)
        print("👤  CLIENT MENU")
        print("=" * 40)
        print("1. Search Medicine")
        print("2. Place Order")
        print("3. View Orders")
        print("4. Cancel Order")
        print("5. Logout")

        choice = input("\nEnter choice: ").strip()

        if choice == "1":
            search_medicine()
        elif choice == "2":
            place_order(client_id)
        elif choice == "3":
            view_orders(client_id)
        elif choice == "4":
            cancel_order(client_id)
        elif choice == "5":
            print("\n👋 Logged out successfully!\n")
            break
        else:
            print("\033[1;91m❌ Invalid choice! Please try again.\033[0m\n")
