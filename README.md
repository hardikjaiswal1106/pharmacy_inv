

---

# 💊 Pharmacy Inventory & Prescription System 💊

A Python-based Command-Line Interface (CLI) project designed to manage medicines, clients, and sales records efficiently in a pharmacy environment.

This system provides two roles — Admin and Client — to handle medicine stock, generate reports, and manage customer prescriptions, all stored securely in JSON files.

---

# Overview

This project simulates a real-world pharmacy management system using Python.

* **Admins** can control inventory, monitor stock levels, and generate detailed reports.
* **Clients** can browse medicines, place orders, and view purchase history.

---

# Key Features

## Admin Functionalities

* Add, update, or delete medicines
* View all medicines in a formatted table
* Generate detailed inventory reports:

  * Low stock medicines
  * Medicines nearing expiry
  * Total stock value
* Robust input validation to prevent system crashes
* Automatic handling of invalid or empty JSON files

## Client Functionalities

* Register as a new client and receive a unique Client ID
* Login with client ID
* View available medicines
* Place multiple orders in a single session
* Generate professional receipts with total bill
* View purchase history
* Cancel pending orders
* Smooth navigation with colored success/error prompts

---

# Project Structure

```
pharmacy-system/
│
├── main.py            # Main entry point (CLI menu)
├── admin_module.py    # Admin functions (CRUD, reports)
├── client.py          # Client functions (orders, view, register)
├── file_utils.py      # File I/O and JSON management
├── medicines.json     # Medicine data file
├── clients.json       # Client data file
└── README.md          # Project documentation
```

---

# Tech Stack

| Component | Technology Used                  |
| --------- | -------------------------------- |
| Language  | Python 3.x                       |
| Storage   | JSON (local file-based database) |
| Libraries | json, os, tabulate, datetime     |
| Interface | Command-Line (CLI)               |

---

# Use Case

This project can be used as:

* A college-level Python project to demonstrate CRUD operations
* A mini pharmacy management system for academic or simulation use
* A foundation project to expand later with GUI (Tkinter/Flask) or SQL database integration

---

# Sample CLI Flow

**💊 Pharmacy Inventory & Prescription System 💊**

1. Admin Login
2. Client Login
3. Register as New Client
4. Exit

---

# Admin Menu

```
=== Admin Menu ===
1. Add Medicine
2. Update Medicine
3. Delete Medicine
4. View Medicines
5. Generate Report
6. Logout
```

---

# Client Menu

```
=== Client Menu ===
1. Search Medicine
2. Place Order
3. View Orders
4. Cancel Order
5. Logout
```

---

# How to Run

## 1. Clone the Repository

```bash
git clone https://github.com/hardikjaiswal1106/pharmacy_inv.git
cd pharmacy_inv
```

## 2. Install Required Library

```bash
pip install tabulate
```

## 3. Run the Program

```bash
python main.py
```

## 4. Admin Login

* **Username:** admin
* **Password:** admin123

## 5. Client Usage

* Register as a new client → receive a client ID
* Login using that client ID → browse medicines & place orders

---

# Public Sources

These resources were used for reference and simulation of realistic pharmacy data:

* Drugs.com – Official Drug Database
* National Library of Medicine – DailyMed
* U.S. FDA – Drug Approvals and Databases
* World Health Organization (WHO) – Essential Medicines List
* Kaggle – Medicine & Pharmacy Datasets

---

# Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new branch (`feature-improvement`)
3. Commit your changes
4. Submit a pull request

Suggestions and feature ideas are always appreciated.

If you found this project helpful, consider giving it a star ⭐!

---

# Acknowledgment

Developed with 💊 by dedicated students to promote learning and innovation in Python-based Inventory Management Systems.

---

