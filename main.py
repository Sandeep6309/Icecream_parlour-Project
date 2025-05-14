#Importing Modules
import tkinter as tk                                        # Importing tkinter
from db import setup_database                               # Importing Db.py
from flavours import add_flavor                             # calling the add_flavor window function
from allergen import add_allergen                           # calling the add_allergen window function
from cart import view_cart, view_flavors                    # calling the view_cart, view_flavors window function
from search import search_flavors                           # calling the search_flavors window function
from suggestion import open_suggestions_window              # calling the open_suggestions_window function

#setting up the database
setup_database()



#main window dimensions and it's background color
app = tk.Tk()
app.title("Ice Cream Parlor")
app.geometry("1000x1000")
app.config(bg="skyblue")

#Welcome lable
label = tk.Label(app, text="Welcome to Summer Cool Ice Cream Parlour!...", font=("Comic Sans Ms", 20),bg="gold")
label.pack(pady=10)


# Adding main window buttons

# Search Flavors Button to open "Search Flavors" window
tk.Button(app, text="Search Flavors", font=("Roboto", 10),width=30, bg="White", command=search_flavors).pack(pady=20)

# Add Flavors Button to open "Add Flvors" Window
tk.Button(app, text = "Add Flavor", font=("Roboto", 10), width=30, bg="orange", command=add_flavor).pack(pady=20)

#Add Allergen Button to open "Add Allergen" window
tk.Button(app, text = "Add Allergen", font=("Roboto", 10), width=30, bg="chocolate", command=add_allergen).pack(pady=20)

#View Flavors and View Cart Buttons to open "View Flavors" and "View Cart"
tk.Button(app, text="View Flavors", font=("Roboto", 10), width=30, bg="gold", command=view_flavors).pack(pady=20)
tk.Button(app, text="View Cart", font=("Roboto", 10), width=30, bg="lightGreen", command=view_cart).pack(pady=20)

# Suggest Flavor Button to open "Suggest Flavor" window
tk.Button(app, text="Suggest Flavor", font=("Roboto", 10), width=30, bg="cyan", command=open_suggestions_window).pack(pady=20)

# main event loop starts from here 
app.mainloop()