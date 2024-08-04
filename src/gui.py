# gui.py
import tkinter as tk
from tkinter import messagebox
import csv

def add_transaction():
    date = date_entry.get()
    description = description_entry.get()
    amount = amount_entry.get()
    category = category_entry.get()
    # Validate and save the transaction

    if not date or not description or not amount or not category:
        messagebox.showerror("Input Error", "All fields must be filled out")
        return 

    try:
        float(amount)
    except ValueError:
        messagebox.showerror("Input Error", "Amount must be a number.")
        return
    
    # Save to CSV
    try:
        with open('/Users/vikashpirthiani/FinTrack/data/transactions.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([date, description, amount, category])
    except Exception as e:
        messagebox.showerror("File Error", f"Failed to write to CSV file: {e}")
        return

    # Notify user
    messagebox.showinfo("Success", "Transaction added successfully!")

def edit_transaction():
    selected_index = transaction_list.curselection()
    if selected_index:
        # Get selected transaction details and populate the entry fields
        pass

def delete_transaction():
    selected_index = transaction_list.curselection()
    if selected_index:
        # Remove selected transaction from CSV or database
        messagebox.showinfo("Success", "Transaction deleted!")

def create_gui():
    root = tk.Tk()
    root.title("Transaction Manager")
    root.geometry("1000x600")  # Set initial window size

    # Configure grid rows and columns to expand
    root.grid_rowconfigure(4, weight=1)  # Row with the Listbox
    root.grid_columnconfigure(1, weight=1)  # Column with Entry widgets

    # Create and place widgets
    tk.Label(root, text="Date").grid(row=0, column=0, sticky="ew", padx=10, pady=5)
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

    global transaction_list
    transaction_list = tk.Listbox(root)
    transaction_list.grid(row=5, column=0, columnspan=2, sticky="nsew", padx=10, pady=5)

    edit_button = tk.Button(root, text="Edit Transaction", command=edit_transaction)
    edit_button.grid(row=6, column=0, columnspan=2, pady=10)

    delete_button = tk.Button(root, text="Delete Transaction", command=delete_transaction)
    delete_button.grid(row=7, column=0, columnspan=2, pady=10)

    # Configure row and column weights
    root.grid_rowconfigure(5, weight=1)  # Row with the Listbox
    root.grid_columnconfigure(0, weight=1)  # Column with labels

    root.mainloop()