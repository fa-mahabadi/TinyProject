import argparse
import random


def guess_game(start, end, guess):
    i = 0
    number = random.randint(start, end)
    while i < guess:
        guess_number = int(input(f"Enter your guess number between {start}-{end}: "))
        i += 1
        if guess_number == number:
            print("finsh game, you win")
            break
        elif guess == i:
            print(f"finsh game, you lose. number is {number}")
            break
        elif guess_number < number:
            print("Enter higher number")
        elif guess_number > number:
            print("Enter lower number")


parser = argparse.ArgumentParser()
parser.add_argument("-s", "--start", type=int, help="lower range of number guess")
parser.add_argument("-e", "--end", type=int, help="upper range of number guess")
parser.add_argument("-g", "--guess", type=int, help="count of the guess")

args = parser.parse_args()
start, end, guess = args.start, args.end, args.guess
guess_game(start, end, guess)
