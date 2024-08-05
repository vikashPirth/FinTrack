import tkinter as tk
from tkinter import ttk, messagebox
import csv
from datetime import datetime

# Constants
CSV_FILE_PATH = '/Users/vikashpirthiani/FinTrack/data/transactions.csv'

# Functions
def validate_date(date_str):
    """Validate the date format (DD/MM/YYYY)."""
    try:
        datetime.strptime(date_str, "%d/%m/%Y")
        return True
    except ValueError:
        return False

def validate_amount(amount_str):
    """Validate that the amount is a number."""
    try:
        float(amount_str)
        return True
    except ValueError:
        return False

def add_transaction():
    """Add a new transaction based on user input."""
    date = date_entry.get()
    description = description_entry.get()
    amount = amount_entry.get()
    category = category_entry.get()

    # Input validation
    if not date or not description or not amount or not category:
        messagebox.showerror("Input Error", "All fields must be filled out.")
        return

    if not validate_date(date):
        messagebox.showerror("Input Error", "Date must be in the format DD/MM/YYYY.")
        return

    if not validate_amount(amount):
        messagebox.showerror("Input Error", "Amount must be a number.")
        return

    try:
        with open(CSV_FILE_PATH, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([date, description, amount, category])
    except Exception as e:
        messagebox.showerror("File Error", f"Failed to write to CSV file: {e}")
        return

    messagebox.showinfo("Success", "Transaction added successfully!")
    
    # Clear the entry fields
    date_entry.delete(0, tk.END)
    description_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)
    category_entry.delete(0, tk.END)

    # Refresh transaction list
    refresh_transactions()

def edit_transaction():
    """Edit the selected transaction."""
    selected_item = transaction_tree.selection()
    if not selected_item:
        messagebox.showerror("Error", "No transaction selected.")
        return

    item = transaction_tree.item(selected_item)
    transaction = item['values']

    edit_window = tk.Toplevel(root)
    edit_window.title("Edit Transaction")

    labels = ["Date", "Description", "Amount", "Category"]
    entries = {}

    for i, (field, value) in enumerate(zip(labels, transaction)):
        tk.Label(edit_window, text=field).grid(row=i, column=0)
        entry = tk.Entry(edit_window)
        entry.insert(0, value)
        entry.grid(row=i, column=1)
        entries[field] = entry

    def save_changes():
        new_transaction = {}
        for field in labels:
            new_value = entries[field].get()
            if not new_value:
                messagebox.showerror("Input Error", "All fields must be filled out.")
                return

            if field == "Date" and not validate_date(new_value):
                messagebox.showerror("Input Error", "Date must be in the format DD/MM/YYYY.")
                return

            if field == "Amount" and not validate_amount(new_value):
                messagebox.showerror("Input Error", "Amount must be a number.")
                return

            new_transaction[field.lower()] = new_value

        transactions[int(selected_item[0])] = new_transaction
        update_transaction_in_csv(CSV_FILE_PATH, transactions)
        populate_treeview(transactions)
        edit_window.destroy()
        messagebox.showinfo("Success", "Transaction updated successfully.")

    tk.Button(edit_window, text="Save", command=save_changes).grid(row=len(labels), column=0, columnspan=2)

def delete_transaction():
    """Delete the selected transaction."""
    selected_item = transaction_tree.selection()
    if not selected_item:
        messagebox.showerror("Error", "No transaction selected.")
        return

    del transactions[int(selected_item[0])]
    update_transaction_in_csv(CSV_FILE_PATH, transactions)
    populate_treeview(transactions)
    messagebox.showinfo("Success", "Transaction deleted!")

def update_transaction_in_csv(file_path, transactions):
    """Update the CSV file with the modified transactions."""
    if not transactions:
        with open(file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['date', 'description', 'amount', 'category'])
        return

    fieldnames = transactions[0].keys()
    with open(file_path, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(transactions)

def load_transactions_from_csv(file_path):
    """Load transactions from the CSV file."""
    transactions = []
    try:
        with open(file_path, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                transactions.append(row)
    except Exception as e:
        messagebox.showerror("File Error", f"Failed to read CSV file: {e}")
    return transactions

def populate_treeview(transactions):
    """Populate the Treeview with transactions."""
    transaction_tree.delete(*transaction_tree.get_children())
    
    for i, transaction in enumerate(transactions):
        # Ensure all necessary keys are present in the transaction
        for key in ['date', 'description', 'amount', 'category']:
            if key not in transaction:
                transaction[key] = ''
        
        transaction_tree.insert("", "end", iid=i, values=(
            transaction['date'],
            transaction['description'],
            transaction['amount'],
            transaction['category']
        ))

def refresh_transactions():
    """Refresh the transaction list from the CSV file."""
    global transactions
    transactions = load_transactions_from_csv(CSV_FILE_PATH)
    populate_treeview(transactions)

def create_gui():
    """Create the main GUI window."""
    global root
    root = tk.Tk()
    root.title("Transaction Manager")

    # Create and place widgets
    tk.Label(root, text="Date (DD/MM/YYYY)").grid(row=0, column=0, sticky="ew", padx=10, pady=5)
    global date_entry
    date_entry = tk.Entry(root)
    date_entry.grid(row=0, column=1, sticky="ew", padx=10, pady=5)

    tk.Label(root, text="Description").grid(row=1, column=0, sticky="ew", padx=10, pady=5)
    global description_entry
    description_entry = tk.Entry(root)
    description_entry.grid(row=1, column=1, sticky="ew", padx=10, pady=5)

    tk.Label(root, text="Amount").grid(row=2, column=0, sticky="ew", padx=10, pady=5)
    global amount_entry
    amount_entry = tk.Entry(root)
    amount_entry.grid(row=2, column=1, sticky="ew", padx=10, pady=5)

    tk.Label(root, text="Category").grid(row=3, column=0, sticky="ew", padx=10, pady=5)
    global category_entry
    category_entry = tk.Entry(root)
    category_entry.grid(row=3, column=1, sticky="ew", padx=10, pady=5)

    add_button = tk.Button(root, text="Add Transaction", command=add_transaction)
    add_button.grid(row=4, column=0, columnspan=2, pady=10)

    # Treeview
    global transaction_tree
    columns = ("date", "description", "amount", "category")
    transaction_tree = ttk.Treeview(root, columns=columns, show='headings')
    for col in columns:
        transaction_tree.heading(col, text=col.capitalize())
    transaction_tree.grid(row=5, column=0, columnspan=2, sticky="nsew", padx=10, pady=5)

    edit_button = tk.Button(root, text="Edit Transaction", command=edit_transaction)
    edit_button.grid(row=6, column=0, pady=10)

    delete_button = tk.Button(root, text="Delete Transaction", command=delete_transaction)
    delete_button.grid(row=6, column=1, pady=10)

    # Configure row and column weights for responsive resizing
    root.grid_rowconfigure(5, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)

    # Load and display transactions
    refresh_transactions()

    root.mainloop()