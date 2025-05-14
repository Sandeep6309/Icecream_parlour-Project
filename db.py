import sqlite3

# Creating a funtion to intialize and create all required tables in  db
def setup_database():

    # Establishing the connection to SQLite database.
    # It creates icecream.db if it not exists.
    conn = sqlite3.connect("icecream.db")
    cursor = conn.cursor()

    # Creating Flavors table to store flavors
    cursor.execute(''' CREATE TABLE IF NOT EXISTS Flavors (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT UNIQUE, season TEXT, ingredients TEXT) ''')

    # Creating Inventory table to store ingredients and quantities.
    cursor.execute(''' CREATE TABLE IF NOT EXISTS Inventory( ingredient TEXT PRIMARY KEY, quantity INTEGER)''')

    # Creating Allergens table to store Allergens.
    cursor.execute(''' CREATE TABLE IF NOT EXISTS Allergens(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT UNIQUE NOT NULL) ''' )

    # Creating Suggestions table to store Suggestions.
    cursor.execute(''' CREATE TABLE IF NOT EXISTS Suggestions(id INTEGER PRIMARY KEY AUTOINCREMENT, flavor_name TEXT, concerns TEXT)''')

    # Creating Cart table to store items in cart.
    cursor.execute (''' CREATE TABLE IF NOT EXISTS Cart(flavor_id INTEGER)''')

    # Commit and close the established connection 
    conn.commit()
    conn.close()