#I added more hint to help the user figure out the secret quicker

#I also handled the case where the user submits an empty guess

print("Welcome to the word guessing game!")

secret = "lemuel"

guess = ""
hint = "_ " * len(secret) 
number_of_guess = 0



print("HINT: One of the sons of Lehi in the book of Mormon")
print(f"Your hint is: {hint}")

while guess != secret:
    guess = input("What is your guess? ").lower()
    number_of_guess +=1

    if len(guess) == 0:
        print("Please input your guess")

    elif len(guess) != len(secret):
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
        hint = " ".join(hint_list)

        print(f"Your hint is: {hint}")
        print("Continue")
print("Congratulations! You guessed it!")  
print(f"It took you {number_of_guess} guesses")  

