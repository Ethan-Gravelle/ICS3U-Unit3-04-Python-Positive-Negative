#!/usr/bin/env python3

# Created by: Ethan Gravelle
# Created on: May 6, 2020
# This program determines the sign of a number.

def main():
    # this function determines the sign of a number.

    # input
    number = int(input("Enter an integer: "))
    # process & output
    if number > 0:
        print("{0} is a positive number.".format(number))
    elif number < 0:
        print("{0} is a negative number.".format(number))
    elif number == 0:
        print("{0} is a zero.".format(number))
    else:
        print("{0} is an invalid answer.".format(number))

    print("")
    print("Done.")


if __name__ == "__main__":
    main()
