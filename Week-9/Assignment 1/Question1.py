from random import randint

def play_bounded_guessing_game():
    random_number = randint(1, 10)
    for i in range(3):
        guess = int(input("Guess a number between 1 and 10: "))
        if guess == random_number:
            print("Congratulations! You won!")
            return
        else:
            print("Wrong guess! Try again.")
    print(f"Game Over! The secret number was {random_number}.")     

play_bounded_guessing_game()