import random

def guess(x):
    while True:
        try:
            input_str = input("Type 'go' to start or 'exit' to quit): ")  
            if input_str.lower() == 'exit':
                break
            elif input_str.lower()== 'go':
                random_number = random.randint(1, x)
                guess = 0
                while guess != random_number:
                    guess = int(input(f"Guess a number between 1 and {x}: "))
                    if guess < random_number:
                        print("Sorry, guess again. Too low")
                    elif guess > random_number:
                        print("Sorry, guess again. Too high")
                print(f"Congrats. You have guessed the number {random_number} correctly!")
        except ValueError:
            print("Please, insert a valid number or type 'exit' to quit.")

def computer_guess(x):
    low = 1
    high = x 
    fb = ''
    while fb != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        fb = input(f"Is {guess} too high (H), too low (L), or correctly (C)? ")
        if fb == 'h':
            high = guess - 1
        elif fb == low:
            low = guess + 1
    print(f"The computer guessed your number, {guess}, correctly!")

computer_guess(100000)