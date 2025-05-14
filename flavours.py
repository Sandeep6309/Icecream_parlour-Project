import sqlite3
from tkinter import messagebox
import tkinter as tk
import re

# Creating a new function to open new window for adding a new flavor.
def add_flavor():

    # New Pop_up Window  and its dimenssion creation.
    add_window = tk.Toplevel()
    add_window.title("Add New Flavor")
    add_window.geometry("300x250")
    add_window.config(bg="Yellow")

    # Lable and  giving input for Flavor Name, Season, Ingredients.

    # for Flavor Name.
    tk.Label(add_window, text="Flavor Name:",font=("Roboto", 10)).grid(row=0, column=0, pady=5)
    flavor_name = tk.Entry(add_window)
    flavor_name.grid(row=0,column=1,pady=5)
    #  for Season.
    tk.Label(add_window, text="Season:",font=("Roboto", 10)).grid(row=1, column=0, pady=5)
    season = tk.Entry(add_window)
    season.grid(row=1,column=1,pady=5)
    # for Ingredients.
    tk.Label(add_window, text="Ingredients:",font=("Roboto", 10)).grid(row=2, column=0, pady=5)
    ingredients = tk.Entry(add_window)
    ingredients.grid(row=2,column=1,pady=5)

    #  Creating function to save flavor to db.
    def save_flavor():
        # Retrieving values from Input fields.
        name = flavor_name.get()
        season_value = season.get()
        ingredients_value = ingredients.get()

        # Input Pattern mismatch Case
        pattern = r'^[a-zA-Z0-9 ,]+$'
        if not re.match(pattern, name):
            messagebox.showwarning("InvalidInput", "Flavor name should contain only letters, numbers, spaces, and commas,")
            return
        elif not re.match(pattern, season_value):
            messagebox.showwarning("Invalid Input", "Season should contain only letters and numbers.")
            return
        elif not re.match(pattern, ingredients_value):
            messagebox.showwarning("Invalid Input", "Ingredients should contain only valid charecters")
            return
        
        # Ensuring all fields are filled.
        if name and season_value and ingredients_value:
            
            #insert new flavor into falvors table in db.
            conn = sqlite3.connect("icecream.db")
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Flavors(name, season, ingredients) VALUES(?,?,?)",(name,season_value,ingredients_value))
            conn.commit()
            conn.close()
            # Shows success message and close add flavor window.
            messagebox.showinfo("Success", "New Flavor added successfully!")
            add_window.destroy()
        else:
            # shows warning  if any field is left empty.
            messagebox.showwarning("Invalid Input", "Plese fill all fields")

    # Creating save btn and giving connection to save_falvor when it is clicked.
    save_button = tk.Button(add_window, text="Save Flavor",font=("Roboto", 10), width = 20, bg="orange",command=save_flavor)
    save_button.grid(row=3, columnspan=2, pady=10)