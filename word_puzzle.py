print("Welcome to the word guessing game!")

secret = "moroni"

guess = ""
hint = ""
number_of_guess = 1

print(f"Your hint is: {hint}")

while guess != secret:
    guess = input("What is your guess? ").lower()
    number_of_guess +=1

    if len(guess) != len(secret):
        print("Sorry, the guess must have the same number of letters as the secret word  ")
    
    elif len(guess) == len(secret) and guess != secret:

        hint_list = list("_" * len(secret))

        for index, char in enumerate(guess):
            if char in secret:
                if secret[index] == char:
                    hint_list[index] = char.upper()
                else:
                    hint_list[index] = char
            else:
                hint_list[index] = "_"
        hint = "".join(hint_list)

        print(f"Your hint is: {hint}")
        print("Continue")
print("Congratulations! You guessed it!")  
print(f"It took you {number_of_guess} guesses")  

