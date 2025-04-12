# Marathi Tadaka Restaurant Billing Application

## Overview
The **Marathi Tadaka Restaurant Billing Application** is a simple Python-based application designed for restaurant management. It allows restaurant staff to:

- View the menu with options like starters, main courses, desserts, and more.
- Add or modify menu items easily.
- Place orders and generate an order summary.
- Apply discounts based on the total order value.

## Features
- **Menu Management**: Add and modify menu items, categorize them (starter, main course, dessert, etc.), and mark them as veg or non-veg.
- **Order Management**: Place an order, view an order summary with pricing, and apply discounts for larger orders.
- **Tax Calculation**: Optionally calculate tax (can be removed based on your project configuration).
- **User-Friendly Interface**: Easy-to-use text-based interface to interact with the system.

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/RK1061/Restaurant-application.git
    ```

2. **Navigate to the project directory**:
    ```bash
    cd Restaurant-application
    ```

3. **Install required dependencies**:
    If you're using virtual environments, make sure to set it up first. For this project, no external dependencies are required unless you're planning to extend functionality.

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'
    ```

## Usage

### 1. **Run the Application**:
   To start the application, simply run the `application.py` script:
    ```bash
    python application.py
    ```

### 2. **Features Available in the Menu**:
- **Add New Item to Menu**: You can add new menu items like starters, mains, rice, etc.
- **Modify Menu Items**: Update existing menu items (name, price, category, etc.).
- **Place Order**: Choose from the menu and place orders with quantities.
- **Show Order Summary**: View the order details, including total price.
- **Apply Discount**: If the total price is over a specified threshold, a discount will be applied automatically.

### 3. **Example Flow**:
- Run the program and select menu options to add items, modify the menu, place orders, and more.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing
Feel free to fork this repository, contribute to features, or open issues. Contributions are welcome!
