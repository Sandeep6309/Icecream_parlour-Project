import tkinter as tk
from tkinter import messagebox
import sqlite3
import re

# creating function to open a window for Searching Flavors by name adn season.
def search_flavors():
    # Creation of pop_up window for search.
    search_window = tk.Toplevel()
    search_window.title("Search Flavours")
    search_window.geometry("500x500")
    search_window.config(bg="#15819a")

    # Creation of input field for flvor name.
    tk.Label(search_window, text="Search by Name:",font=("Roboto", 10)).pack()
    name_entry = tk.Entry(search_window)
    name_entry.pack(pady=5)

    # Creation of Listbox to show search results.
    tk.Label(search_window, text="Filter by season:",font=("Roboto", 10)).pack()
    season_entry = tk.Entry(search_window)
    season_entry.pack(pady=5)
    result_box = tk.Listbox(search_window, width=50)
    result_box.pack(pady=10)

    # Creating a function to perform search operation using filters.
    def perform_search():
        name = name_entry.get()         # Getting name input
        season = season_entry.get()     # Getting season input

        #Input Pattern mismatch Case
        pattern = r'^[a-zA-Z0-9 ,]+$'
        if (name and not re.match(pattern, name)) or (season and not re.match(pattern, season)):
            messagebox.showwarning("Invalid Input", "Search fields can only contain, numbers and spaces")
            return
        
        # Connecting to database.
        conn = sqlite3.connect("icecream.db")
        cursor = conn.cursor()
        query = "SELECT name, season, ingredients FROM Flavors WHERE 1=1"
        params = []

        # Adding condition for name if it is provided.
        if name:
            query += " AND name LIKE ?"
            params.append(f"%{name}%")

        # Adding condition for season if it is provided.
        if season:
            query += " AND season LIKE ?"
            params.append(f"%{season}%")

        # Executing the dynamic query with different parameters.
        cursor.execute(query, params)
        results = cursor.fetchall()
        conn.close()

        # Clearing previous results
        result_box.delete(0, tk.END)

        # Displaying results in listbox.
        if results:
            for row in results:
                result_box.insert(tk.END, f"{row[0]} | {row[1]} | {row[2]}")
        else:
            result_box.insert(tk.END, "No matching flavors found.")
    
    # Creating Search button and providing action to it to perform searching.
    tk.Button(search_window, text="Search",font=("Roboto", 10), bg= "orange", fg="black", command=perform_search).pack(pady=10)

