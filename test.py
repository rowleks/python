friends = []

user_input = ""

while user_input != "End":

    user_input = input("Type the name of a friend: ").capitalize()
    if user_input != "End":
        friends.append(user_input)

print()
if not friends:
    print("You have no friends")
else:
    print("Your friends are:")
    for friend in friends:
        print(friend)
