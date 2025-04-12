from Resturant import rest

def main_menu():
    print("Welcome to Marathi Tadaka Restaurant")
    print("-" * 50)
    print("1. Show Menu")
    print("2. Add New Item to Menu")
    print("3. Modify Menu Items")
    print("4. Place Order")
    print("5. Show Order Summary")
    print("6. Exit")
    print("-" * 50)
    choice = int(input("Enter your choice: "))
    return choice

# Initialize restaurant instance
restaurant = rest()

while True:
    choice = main_menu()

    if choice == 1:
        restaurant.showmenu()

    elif choice == 2:
        restaurant.additem()

    elif choice == 3:
        restaurant.modyfyitems()

    elif choice == 4:
        restaurant.orderitem()

    elif choice == 5:
        restaurant.showorder()

    elif choice == 6:
        print("Thank you for visiting Marathi Tadaka! Come again!")
        

    else:
        print(" Invalid choice. Please try again.")
