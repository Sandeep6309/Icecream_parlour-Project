import sqlite3
from tkinter import messagebox
import tkinter as tk

# Creating a function to add selected flavors to cart.
def add_to_cart(flavor_name):

    # Establishing connection to the SQLite database.
    conn = sqlite3.connect("icecream.db")
    cursor = conn.cursor()

    #Get the flavor id from the flavors table by using its name.
    cursor.execute("SELECT ID FROM Flavors WHERE name = ?", (flavor_name,))
    result = cursor.fetchone()

    if result:
        flavor_id = result[0]
        # Inserting the flavor ID into cart table.
        cursor.execute("INSERT INTO Cart(flavor_id) VALUES(?)", (flavor_id,))
        conn.commit()
        # Showing success message.
        messagebox.showinfo("Success", f"{flavor_name} added to cart!")
    else:
        # showing error message if flavor not found.
        messagebox.showerror("Error",f"Flavor '{flavor_name}' not found!")

    conn.close()
    
# Creating a function to view all available flavors and add them to cart. 
def view_flavors():
    # Creating a new "Available Flavors" pop_up window and its dimmensions.
    view_window = tk.Toplevel()
    view_window.title("Available Flavors")
    view_window.geometry("500x500")
    view_window.config(bg="#a06ab4")

    #Fetching all flavor names from the database.
    conn = sqlite3.connect("icecream.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM Flavors")
    flavors = cursor.fetchall()
    conn.close()

    # Displaying each flavor with "Add to cart" button.
    row = 0
    for flavor in flavors:
        name = flavor[0]
        tk.Label(view_window, text=name).grid(row=row, column=0,padx=5,pady=5)
        # using lambda to pass current flavor names to cart.
        tk.Button(view_window, text="Add to Cart",font=("Roboto", 10), bg="chocolate", command=lambda n=name: add_to_cart(n)).grid(row=row,column=1,padx=5,pady=5)
        row +=1

# Creating function to view all the contents in the cart.
def view_cart():
    # new pop_up window creation.
    cart_window = tk.Toplevel()
    cart_window.title("Your Cart")
    cart_window.geometry("500x500")
    cart_window.config(bg="#e5c951")

    # Fetch flavor names from the cart using JOIN with flavors table.
    conn = sqlite3.connect("icecream.db")
    cursor = conn.cursor()
    cursor.execute(''' SELECT Flavors.name FROM Flavors JOIN Cart ON Flavors.id = Cart.flavor_id ''')
    items = cursor.fetchall()
    conn.close()

    # Displaying every item in cart or empty cart message.
    if items:
        for idx, item in enumerate(items):
            tk.Label(cart_window, text=f"{idx+1}. {item[0]}").pack(pady=5)
    else:
        tk.Label(cart_window, text="Cart is empty!",font=("Roboto", 10)).pack(pady=20)
