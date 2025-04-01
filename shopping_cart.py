print("Welcome to the Shopping Cart Program!")

cart = []
actions = ["Add item", "View cart", "Remove item", "Compute total", "Quit"]


selected_action = None

while selected_action != 5:

    print("Please select one of the following:")
    for i in range(len(actions)):
        print(f"{i+1}. {actions[i]}")
    selected_action = int(input("Please enter an action: "))

    if selected_action == 1:
        added_item = input("What item would you like to add? ").lower()
        cart.append(added_item)
        print(f"{added_item} has been added to the cart.")
        print()
    elif selected_action == 2:
        print("The contents of the shopping cart are:")
        for item in cart:
            print(item)
        print()
print("Thank you. Goodbye")