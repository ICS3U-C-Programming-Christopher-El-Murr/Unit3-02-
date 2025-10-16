#!/usr/bin/env python3
# Created By: Christopher El-Murr
# Date: 10 16, 2025
# This program asks the user to guess the correct number
import constants


def main():
    # ask user for their number guess
    number_guess = int(input("Enter the number:"))
    # is the number = to 9
    if number_guess == constants.number:
        print("Congratulation, you guessed correctly")
    if number_guess != constants.number:
        print("Guess again")


if __name__ == "__main__":

    main()
