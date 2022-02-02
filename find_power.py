#!/usr/bin/env python3
# Created By: Keiden
# Date: 2 / 2 / 2022
# This program takes user input and displays 0, 1, 2, 3, etc. to the power of
# two until it reaches the user's number.


def main():
    print("Hi! Insert a number, and find out the power of all the numbers that"
          " come before it.")

    user_num = input(">")

    try:
        user_num_int = int(user_num)

        for loop_num in range((user_num_int + 1)):
            print(str(loop_num) + "^2 =", (loop_num * loop_num))

    except ValueError:
        print("Invalid input!")


if __name__ == "__main__":
    main()
