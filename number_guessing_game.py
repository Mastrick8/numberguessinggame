import random                               #python module to generate random numbers

play = "Y"                                  #variable to store the user input for playing again
while play == "Y":
                                    # for the repitition of the game if usser wants to play again

          #Generate a random number between 1 and 10
    print()
    name = input("Hello gamer whats your name? ")                #user input for name
    print("Hello", name, "!")
    print()
    print("Choose your difficulty level: ")
    print("1. Easy (1 - 10)")
    print("2. Medium (1 - 50)")
    print("3. Hard (1 - 100)")
    difficulty = input("Enter your choice (1/2/3): ")
    

    if difficulty == "1":
       max_number = 10                                #stores the maximum number based on the difficulty level
       secret_number = random.randint(1, max_number)
    elif difficulty == "2":
       max_number = 50
       secret_number = random.randint(1, max_number)
    elif difficulty == "3":
       max_number = 100
       secret_number = random.randint(1, max_number)
    



    guess = int(input(f"Guess a number between 1 and {max_number}: "))   # f string for a neater code, to display max number based on the difficulty
    attempts = 1                                #stores the number of attempts made by the user
    while guess != secret_number:               #loops until the user guesses the correct number
       if guess > secret_number:
        print("Your guess is too high.")
       elif guess < secret_number:
        print("Your guess is too low.")
       guess = int(input(f"Guess again (between 1 and {max_number}): "))
       attempts += 1                           #increases the number of attempts made by the user
    print()
    print("You got the Secret Number!, It is", secret_number, "in ", attempts, "attempts.")
    print()
    print()
    play = input("Do you want to play again? (Y/N): ").upper()






