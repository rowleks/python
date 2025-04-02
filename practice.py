print()
print("Welcome to the Shopping Cart Program!")
print()

cart = []
selected_action = None

while selected_action != 5:

    print("Please select one of the following:")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")
    
    selected_action = int(input("Please enter an action: "))

    if selected_action == 1:

        added_item = input("What item would you like to add? ")

        cart.append(added_item)

        print(f"'{added_item}' has been added to the cart.")
        print()
        
    elif selected_action == 2:

        for item in cart:
            print(item)
    


