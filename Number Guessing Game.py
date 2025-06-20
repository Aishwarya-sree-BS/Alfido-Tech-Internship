def guess_num():
    import random

    secret_number = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("Guess the number between 1 and 100")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
        
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number.")

        
def main():
    while True:
        guess_num()
        continuee=input("Do you want to play again?:")
        if continuee.lower()!='yes':
            break

if __name__=="__main__":
     main()

    



