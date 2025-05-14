import tkinter as tk
from tkinter import messagebox
import sqlite3
import re

# Function to open add suggestions window to add suggestions and allergy concerns.
def open_suggestions_window():
    # Creating new pop_up window and it's dimenssions
    window = tk.Toplevel()
    window.title("Suggest a Flavour")
    window.geometry("500x500")
    window.config(bg="lavender")

    # Lable and input entry for suggested flavor name.
    tk.Label(window, text="Flavour Name:",font=("Roboto", 10), bg="lavender").grid(row=0,column=0, pady=10,padx=10)
    flavor_entry = tk.Entry(window, width=30)
    flavor_entry.grid(row=0, column=1, pady=10)

    # Lable and input entry for Allergy Concerns.
    tk.Label(window, text="Allergy Concerns:", font=("Roboto", 10),bg="light green").grid(row=1, column=0,pady=10, padx=10)
    concerns_entry = tk.Entry(window, width=30)
    concerns_entry.grid(row=1, column=1,pady=10)

    # creating function to save the added suggestions and allergy concerns to database.
    def save_suggestion():
        flavor = flavor_entry.get()         # Getting flavor name from input.
        concerns = concerns_entry.get()     # Getting Allergy Concerns from input.

        # Input Pattern mismatch Case
        pattern = r'^[a-zA-Z0-9 ,]+$'
        if not re.match(pattern, flavor):
            messagebox.showwarning("Invalid Input", "Flavor name must contain only letters, numbers, and spaces.")
            return
        elif not re.match(pattern, concerns):
            messagebox.showwarning("Invalid Input", "Concerns must contain valid charecters.")
            return
        
        # condtion that both fields are filled, to insert data into suggestions table.
        if flavor and concerns:
            conn = sqlite3.connect("icecream.db")
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Suggestions(flavor_name, concerns) VALUES (?,?)", (flavor, concerns))
            conn.commit()
            conn.close()
            # Shows success message and close "add Suggestions" window.
            messagebox.showinfo("Success", "Thanks for giving your suggestion!")
            window.destroy()
            # Shows warning message if any field is left empty.
        else:
            messagebox.showwarning("Invalid Input", "Please fill all the fields")

    # Creating "Submit" button to submit the data to add in suggestions table.
    tk.Button(window, text="Submit Suggestion", command=save_suggestion, bg="orange", width=20).grid(row=2, columnspan=2, pady=20)