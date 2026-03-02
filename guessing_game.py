secret_number = 16


while True:
    guess_number = int(input("Guess a number: "))


    if guess_number == secret_number:
        print("You guessed right.")


        break

     
    elif guess_number <= secret_number - 5:
        print("Too low.")


    else:
        print("Too high.")

    
        
