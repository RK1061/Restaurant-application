from menu import menu

class rest(menu):
    def __init__(self):
        super().__init__()  # Initialize the parent class (menu)

    def get(self):
        # Calling the methods from the parent (menu) class
        super().additem()    # Add item to the menu
        super().showmenu()   # Show the menu
        super().modyfyitems()  # Modify a menu item
        super().orderitem()  # Place an order
        super().showorder()  # Show the order summary
        
