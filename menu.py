from random import randint

class menu:
    def __init__(self):
        self.menu = []  
        self.cart = [] 
        self.final_amount = 0 

    # Add a new item to the menu
    def additem(self):
        item_id = randint(100, 999)
        name = input("Enter the dish name: ")
        price = float(input("Enter the price: ₹"))
        category = input("Enter the category (starter/main_course/roti/dessert/rice/chinese): ")
        veg = input("Is it Veg? (yes/no): ").lower() == "yes"

        # Add item to menu list
        self.menu.append({
            "id": item_id,
            "name": name,
            "price": price,
            "category": category,
            "veg": veg
        })
        print(f"{name} added to menu successfully.")

    # Display the current menu
    def showmenu(self):
        if not self.menu:
            print("Menu is empty.")
            return

        print("-" * 85)
        print("**** MENU ****")
        print(f"{'ID':<5} {'Name':<35} {'Price':<10} {'Category':<15} {'Type':<10}")
        print("-" * 85)
        for item in self.menu:
            veg_status = "Veg" if item["veg"] else "Non-Veg"
            print(f"{item['id']:<5} {item['name']:<35} ₹{item['price']:<9.2f} {item['category']:<15} {veg_status:<10}")
        print("-" * 85)

    # Modify menu items
    def modyfyitems(self):
        self.showmenu()
        item_id = int(input("Enter the item ID to modify: "))
        found = False
        for item in self.menu:
            if item["id"] == item_id:
                item["name"] = input("New name: ")
                item["price"] = float(input("New price: ₹"))
                item["category"] = input("New category: ")
                item["veg"] = input("Is it Veg? (yes/no): ").lower() == 'yes'
                print(f"Item with ID {item_id} updated successfully.")
                found = True
                break
        if not found:
            print("Item not found.")

    # Place an order
    def orderitem(self):
        self.showmenu()
        name = input("Enter the name of your order: ").lower()
        order_items = []
        total_price = 0

        for item in self.menu:
            if name in item["name"].lower():
                quantity = int(input("Enter the quantity: "))
                total = item["price"] * quantity
                order_items.append({
                    "name": item["name"],
                    "price": item["price"],
                    "quantity": quantity,
                    "total": total
                })
                total_price += total
                print(f"{item['name']} x {quantity} added to cart.")

        if order_items:
            # Add the order to the cart (order list)
            self.cart.append(order_items)
            print(f"Order placed successfully. Total amount: ₹{total_price:.2f}")
            self.final_amount = total_price  
        else:
            print("Item not found in menu.")

    # Show the order summary
    def showorder(self):
        if not self.cart:
            print("No orders placed yet.")
            return

        print("ORDER SUMMARY")
        print("_" * 85)
        grand_total = 0
        for order in self.cart:
            for item in order:
                print(f"{item['name']:<25} {item['quantity']:<5} ₹{item['price']:<9.2f} ₹{item['total']:<.2f}")
                grand_total += item['total']
        print("_" * 85)
        print(f"Grand Total: ₹{grand_total:.2f}")
    print("Thanks for visit our restorent")

    
    
