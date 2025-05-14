# Ice Cream Parlor Application

## Overview

This is a Python-based Ice Cream Parlor application designed to manage various aspects of an ice cream shop, including:

- Seasonal flavor offerings
- Ingredient inventory management
- Customer flavor suggestions and allergy concerns
- A shopping cart for customer favorites

The application uses a **SQLite** database to store data about ice cream flavors, allergens, and customer suggestions. It also provides a **Tkinter** GUI for user interaction.

## Features

- **Add New Flavors**: Add new ice cream flavors with name, season, and ingredients.
- **Add Allergens**: Add allergens to the database and prevent users from choosing allergenic ingredients.
- **Search & Filter**: Search for ice cream flavors based on season, ingredients, and name.
- **Suggestions**: Allow customers to provide feedback on flavors and suggest improvements.
- **Cart Management**: Users can add and manage their favorite flavors in a virtual cart.

## Requirements

1. **Python 3.8+**  
2. **SQLite3** (for database management)
3. **Tkinter** (for GUI)
4. **Docker** (optional but recommended for containerization)

## How to Run the Application

### Without Docker:

1. Clone the repository:
    ```bash
    git clone https://github.com/Sandeep6309/icecream-parlor.git
    cd icecream-parlor
    ```

2. Install the required Python libraries:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the application:
    ```bash
    python main.py
    ```

### With Docker:

1. Build the Docker image:
    ```bash
    docker build -t icecream-parlor .
    ```

2. Run the container:
    ```bash
    docker run -p 5000:5000 icecream-parlor
    ```

### Database Initialization:
The application will automatically create the required tables in the SQLite database (`icecream.db`) when it starts.

## File Structure

- `main.py`: Main Python script that launches the GUI and integrates with the database.
- `db.py`: Handles database setup and queries.
- `flavor.py`: Manages flavor-related functions.
- `allergen.py`: Manages allergen-related functions.
- `suggestion.py`: Handles customer suggestions.
- `search.py`: Provides search and filter functionality.
- `Dockerfile`: Docker configuration for containerizing the application.
- `requirements.txt`: Python dependencies.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the **Tkinter** documentation for GUI examples.
- Thanks to **SQLite3** for lightweight database management.
