from file_utils import *
from client import *
from admin_module import *


def main():
    while True:
        print("""
=== Pharmacy Inventory & Prescription System ===
1. Admin Login
2. Client Login
3. Register as New Client
4. Exit
""")
        choice = input("Enter choice: ")

        if choice == '1':
            password = input("Enter Admin Password: ")
            if password == "admin123":
                admin_menu()
            else:
                print("❌ Wrong password!\n")

        elif choice == '2':
            clients = load_data('clients.json')
            client_id = int(input("Enter Client ID: "))
            if any(c["client_id"] == client_id for c in clients):
                client_menu(client_id)
            else:
                print("❌ Invalid Client ID!\n")

        elif choice == '3':
            register_client()

        elif choice == '4':
            print("Thank you! Exiting program...")
            break
        else:
            print("Invalid choice!\n")

if __name__ == "__main__":
    main()
