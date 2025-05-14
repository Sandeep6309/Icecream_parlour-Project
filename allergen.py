import sqlite3
from tkinter import messagebox
import tkinter as tk
import re

# Creating a function to open "Add Allergen Window" that allows user to add new allergens.
def add_allergen():

    # New "Add New Allergen" pop_up window ant its Dimenssions creation.
    allergen_window = tk.Toplevel()
    allergen_window.title("Add New Allergen")
    allergen_window.geometry("300x250")
    allergen_window.config(bg="#d07987")

    # Lableing and input entry field for new allergen name
    tk.Label(allergen_window, text="Allergen Name:",font=("Roboto", 10)).grid(row=0, column=0, pady=10)
    allergen_name = tk.Entry(allergen_window)
    allergen_name.grid(row=0, column=1,pady=10)

    # Creating a function to save alleregen to the database.
    def save_allergen():
        name = allergen_name.get() # Getting input from the entry field.

        # Input Pattern mismatch Case
        pattern = r'^[a-zA-Z0-9 ,]+$'
        if not re.match(pattern,name):
            messagebox.showwarning("Invalid Input", "Allergen name must contain letters, numbers, and spaces.")
            return
        if name:
            try:
                # Establishing connection to SQLlite and insert Allergens.
                conn = sqlite3.connect("icecream.db")
                cursor = conn.cursor()
                cursor.execute("INSERT INTO Allergens(name) VALUES(?)", (name,))
                conn.commit()
                conn.close()

                # Showing success message and close the window.
                messagebox.showinfo("Success", "Allergen added successfully.")
                allergen_window.destroy()

            except sqlite3.IntegrityError:
                # Handles duplicate entry's.
                messagebox.showwarning("Duplicate", "This allergen already exists.")
        else:
            # Showing warning message if the field is left empty.
            messagebox.showwarning("Invalid Input", "Please enter an alergen name.")

    # Creating Save allergen button to save the data into database.
    tk.Button(allergen_window, text="Save Allergen",font=("Roboto", 10), width = 20, bg="orange",command=save_allergen).grid(row=3, columnspan=2, pady=10)
