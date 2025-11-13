from file_utils import *
from client import *
from admin_module import *
import os

# --- Default medicines ---
default_medicines = [
    {"med_id": 1, "name": "Paracetamol", "category": "Pain Relief", "price": 50.0, "stock": 100, "expiry": "2026-12-31"},
    {"med_id": 2, "name": "Amoxicillin", "category": "Antibiotic", "price": 120.0, "stock": 50, "expiry": "2025-11-30"},
    {"med_id": 3, "name": "Cetirizine", "category": "Antihistamine", "price": 30.0, "stock": 75, "expiry": "2026-06-30"},
    {"med_id": 4, "name": "Ibuprofen", "category": "Pain Relief", "price": 80.0, "stock": 60, "expiry": "2025-12-15"},
    {"med_id": 5, "name": "Metformin", "category": "Diabetes", "price": 100.0, "stock": 40, "expiry": "2027-01-01"}
]

def main():
    # --- Create JSON files if not present and populate default medicines ---
    if not os.path.exists("medicines.json") or not load_data("medicines.json"):
        save_data("medicines.json", default_medicines)
        print("\033[1;92m✅ Default medicines added to inventory!\033[0m\n")

    if not os.path.exists("clients.json"):
        save_data("clients.json", [])
    if not os.path.exists("orders.json"):
        save_data("orders.json", [])

    while True:
        print("""
=============================================
💊 Pharmacy Inventory & Prescription System 💊
=============================================
1. Admin Login
2. Client Login
3. Register as New Client
4. Exit
""")
        choice = input("Enter choice: ").strip()

        # --- Admin Login ---
        if choice == '1':
            password = input("Enter Admin Password: ").strip()
            if password == "admin123":
                print("\n\033[1;92m✅ Admin logged in successfully!\033[0m\n")
                admin_menu()
            else:
                print("\n\033[1;91m❌ Wrong password!\033[0m\n")

        # --- Client Login ---
        elif choice == '2':
            clients = load_data('clients.json')
            if not clients:
                print("\n\033[1;91m❌ No registered clients found. Please register first.\033[0m\n")
                continue

            try:
                client_id = int(input("Enter Client ID: ").strip())
            except ValueError:
                print("\n\033[1;91m❌ Invalid input! Please enter a valid Client ID number.\033[0m\n")
                continue

            if any(c["client_id"] == client_id for c in clients):
                print("\n\033[1;92m✅ Client logged in successfully!\033[0m\n")
                client_menu(client_id)
            else:
                print("\n\033[1;91m❌ Invalid Client ID!\033[0m\n")

        # --- New Client Registration ---
        elif choice == '3':
            register_client()

        # --- Exit Program ---
        elif choice == '4':
            print("\n\033[1;92m✅ Logged out successfully. Thank you for using our system!\033[0m\n")
            break

        # --- Invalid Menu Choice ---
        else:
            print("\n\033[1;91m❌ Invalid choice! Please select a valid option (1-4).\033[0m\n")


if __name__ == "__main__":
    main()
