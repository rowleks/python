#I added a condition to check if the user typed in a valid number when selecting an action and handled the case if they typed a string instead.

#I also added a condition to handle the case where the user selects an action that is not in the list of available actions

print("\nWelcome to the Shopping Cart Program!\n")

cart = []
prices = []
actions = ["Add item", "View cart", "Remove item", "Compute total", "Quit"]
selected_action = None

while selected_action != 5:
    
    print("Please select one of the following")
    for i in range(len(actions)):
        print(f"{i+1}. {actions[i]}")

    selected_action = input("Please enter an action: ")

    if not selected_action.isnumeric():
        print("Please select an action by typing the corresponding number\n")

    else:
        selected_action = int(selected_action)

        if selected_action == 1:

            added_item = input("What item would you like to add? ").capitalize()
            item_price = float(input(f"What is the price of '{added_item}'? "))

            cart.append(added_item)
            prices.append(item_price)

            print(f"'{added_item}' has been added to the cart.")
            print()

        elif selected_action == 2:
            print("The contents of the shopping cart are:")
            for i in range(len(cart)):
                print(f"{i+1}. {cart[i]} - ${prices[i]:.2f}")
            print()

        elif selected_action == 3:
            print("The contents of the shopping cart are:")
            for i in range(len(cart)):
                print(f"{i+1}. {cart[i]} - ${prices[i]:.2f}")
            print()

            removed = int(input("Which item would you like to remove? "))
            removed_index = removed - 1
            removed_item = cart.pop(removed_index)
            prices.pop(removed_index)

            print(f"{removed_item} has been removed from the cart.\n")

        elif selected_action == 4:
            total = 0
            for price in prices:
                total += price
            print(f"The total price of the items in the shopping cart is ${total:.2f}\n")

        elif selected_action > 4 or selected_action < 1:
            print("Selected action does not exist.\n")

print("Thank you. Goodbye")