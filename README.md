

---

# Pharmacy Inventory & Prescription System 💊

A **Python-based Command-Line Interface (CLI)** project designed to manage medicines, clients, and sales records efficiently in a pharmacy environment. This system provides a structured and secure way to handle inventory, prescriptions, and customer data using JSON files.

---

## Features

### Admin Role

* **Manage Medicines**: Add, update, and delete medicine details.
* **Stock Management**: Track quantity and availability of medicines.
* **Generate Reports**: View sales, stock levels, and client activity.

### Client Role

* **Register & Login**: Secure client registration.
* **Browse Medicines**: View available medicines and their details.
* **Place Orders**: Order medicines with prescription tracking.
* **View Orders**: Track order history.

---

## Data Storage

The system uses **JSON files** to securely store all data:

* `medicines.json` – Stores medicine details.
* `clients.json` – Stores registered client information.
* `orders.json` – Stores client orders and prescriptions.

---

## Project Structure

```
pharmacy-system/
│
├── main.py              # Main entry point (CLI menu)
├── admin_module.py      # Admin functions (CRUD, reports)
├── client.py            # Client functions (register, order, view)
├── file_utils.py        # File I/O and JSON management
├── medicines.json       # Medicine data file
├── clients.json         # Client data file
├── orders.json          # Orders data file
└── README.md            # Project documentation
```

---

## Installation

1. **Clone the repository**:

```bash
git clone https://github.com/hardikjaiswal1106/pharmacy_inv/
cd pharmacy-system
```

2. **Install required packages** (if any):

```bash
pip install -r requirements.txt
```

3. **Run the program**:

```bash
python main.py
```

---

## Usage

1. Launch the system using `python main.py`.
2. Select your role: **Admin** or **Client**.
3. Follow on-screen instructions to manage medicines, clients, or orders.

---

## Technologies Used

* Python 3.x
* JSON for data storage
* Command-Line Interface (CLI)

---

## Future Enhancements

* GUI-based interface using Tkinter or PyQt.
* Integration with a database (SQLite/MySQL) for large-scale deployment.
* Email/SMS notifications for order confirmation.

---


