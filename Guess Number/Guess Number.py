import random

def guess_the_number():
    print("Welcome to the Guess the Number game!")
    lower_bound = 1
    upper_bound = 100
    number_to_guess = random.randint(lower_bound, upper_bound)
    attempts = 0

    print(f"I'm thinking of a number between {lower_bound} and {upper_bound}.")

    while True:
        try:
            guess = int(input("Take a guess: "))
            attempts += 1

            if guess < number_to_guess:
                print("Your guess is too low.")
            elif guess > number_to_guess:
                print("Your guess is too high.")
            else:
                print(f"Your guess is correct! You guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input! Please enter a numerical value.")

if __name__ == "__main__":
    guess_the_number()
